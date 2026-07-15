#!/usr/bin/env python3
"""Fetch GitHub repository metadata and regenerate the portfolio region."""

from __future__ import annotations

import html
import json
import os
import stat
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


OWNER = "ianzepp"
SKIP = {
    "archived-projects",
    "personal",
    "ianzepp.dev",
    "dotfiles",
    "homebrew-tap",
    "0-prework-assignment",
}
BEGIN_MARKER = "<!-- BEGIN GENERATED PROJECTS -->"
END_MARKER = "<!-- END GENERATED PROJECTS -->"


def run(*args: str) -> str:
    return subprocess.check_output(args, text=True)


def fetch_repos() -> list[dict[str, Any]]:
    """Fetch the metadata used by the existing ranking policy."""

    cursor: str | None = None
    repos: list[dict[str, Any]] = []

    while True:
        after = "null" if cursor is None else json.dumps(cursor)
        query = f"""
        query {{
          repositoryOwner(login: {json.dumps(OWNER)}) {{
            repositories(first: 100, after: {after}, orderBy: {{field: NAME, direction: ASC}}, isFork: false) {{
              pageInfo {{ hasNextPage endCursor }}
              nodes {{
                name
                description
                isPrivate
                defaultBranchRef {{
                  target {{
                    ... on Commit {{
                      history(first: 1) {{ totalCount }}
                    }}
                  }}
                }}
              }}
            }}
          }}
        }}
        """
        payload = json.loads(run("gh", "api", "graphql", "-f", f"query={query}"))
        if not isinstance(payload, dict):
            raise RuntimeError("GitHub response was not a JSON object")
        if payload.get("errors"):
            raise RuntimeError(f"GitHub GraphQL error: {payload['errors']}")

        owner = (payload.get("data") or {}).get("repositoryOwner")
        if not isinstance(owner, dict):
            raise RuntimeError("GitHub response did not contain repository owner data")
        repositories = owner.get("repositories")
        if not isinstance(repositories, dict):
            raise RuntimeError("GitHub response did not contain repository data")

        nodes = repositories.get("nodes")
        if not isinstance(nodes, list) or any(not isinstance(node, dict) for node in nodes):
            raise RuntimeError("GitHub response contained malformed repository nodes")
        repos.extend(nodes)

        page_info = repositories.get("pageInfo")
        if not isinstance(page_info, dict):
            raise RuntimeError("GitHub response did not contain pagination data")
        if not page_info.get("hasNextPage"):
            return repos

        cursor = page_info.get("endCursor")
        if not isinstance(cursor, str) or not cursor:
            raise RuntimeError("GitHub response reported a page without an end cursor")


def rank_repos(repos: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    """Apply the existing ranking and tier policy to repository metadata."""

    rows: list[dict[str, Any]] = []
    for repo in repos:
        # GitHub metadata is a publication boundary: missing or non-boolean
        # visibility is not safe to publish, so only an explicit public value
        # may enter the rendered dataset.
        if repo.get("isPrivate") is not False:
            continue

        name = repo.get("name")
        if not isinstance(name, str) or not name:
            raise ValueError("repository metadata is missing a name")
        if name in SKIP:
            continue

        branch = repo.get("defaultBranchRef") or {}
        target = branch.get("target") if isinstance(branch, dict) else {}
        history = target.get("history") if isinstance(target, dict) else {}
        count = history.get("totalCount", 0) if isinstance(history, dict) else 0
        if not isinstance(count, int) or isinstance(count, bool) or count < 0:
            raise ValueError(f"repository {name!r} has an invalid commit count")

        description = repo.get("description") or name
        if not isinstance(description, str):
            raise ValueError(f"repository {name!r} has an invalid description")

        rows.append(
            {
                "name": name,
                "count": count,
                "desc": description,
                "private": False,
            }
        )

    rows.sort(key=lambda row: (-row["count"], row["name"].lower()))

    sections: dict[str, list[dict[str, Any]]] = {
        "Featured Work": [],
        "Previous Projects": [],
        "Other": [],
    }
    listed = 0
    for row in rows:
        if row["count"] < 5:
            continue

        listed += 1
        if listed <= 5:
            sections["Featured Work"].append(row)
        elif row["count"] > 20:
            sections["Previous Projects"].append(row)
        else:
            sections["Other"].append(row)

    return rows, sections


def render_project(row: dict[str, Any], compact: bool) -> str:
    """Render one explicitly public project."""

    if row.get("private") is not False:
        raise ValueError("private repository metadata cannot be rendered")

    name = html.escape(row["name"])
    url = html.escape(f"https://github.com/{OWNER}/{row['name']}", quote=True)
    project_name = f'<a href="{url}">{name}</a>'

    count = str(row["count"]) if compact else f'{row["count"]} commits'
    indent = "    " if compact else "  "
    return "\n".join(
        [
            f'{indent}<div class="project">',
            f'{indent}  <div class="project-name">{project_name} <span class="badge-commits">{count}</span></div>',
            f'{indent}  <div class="project-desc">{html.escape(row["desc"])}</div>',
            f"{indent}</div>",
        ]
    )


def render_section(label: str, rows: list[dict[str, Any]], compact: bool = False) -> str:
    lines = [f'  <div class="section-label">{label}</div>', ""]
    if compact:
        lines.append('  <div class="compact">')
    for index, row in enumerate(rows):
        lines.append(render_project(row, compact))
        if index != len(rows) - 1:
            lines.append("")
    if compact:
        lines.extend(["  </div>"])
    return "\n".join(lines)


def render_projects(sections: dict[str, list[dict[str, Any]]]) -> str:
    parts = [
        render_section("Featured Work", sections["Featured Work"]),
        render_section("Previous Projects", sections["Previous Projects"]),
        render_section("Other", sections["Other"], compact=True),
    ]
    rendered = "\n\n".join(parts)
    local_path_markers = ("/" + "Users/", "/" + "private/")
    if "badge-private" in rendered or any(marker in rendered for marker in local_path_markers):
        raise ValueError("generated project data failed the public-only publication gate")
    return rendered


def _marker_positions(document: str, marker: str) -> list[int]:
    positions: list[int] = []
    start = 0
    while True:
        position = document.find(marker, start)
        if position == -1:
            return positions
        positions.append(position)
        start = position + len(marker)


def _assert_standalone_marker(document: str, marker: str, position: int) -> None:
    line_start = document.rfind("\n", 0, position) + 1
    line_end = document.find("\n", position)
    if line_end == -1:
        line_end = len(document)
    before = document[line_start:position].strip()
    after = document[position + len(marker) : line_end].strip()
    if before or after:
        raise ValueError(f"{marker} must appear alone on its line")


def replace_generated_region(document: str, generated: str) -> str:
    """Replace exactly one supported generated region, or fail loudly."""

    begin_positions = _marker_positions(document, BEGIN_MARKER)
    end_positions = _marker_positions(document, END_MARKER)
    if len(begin_positions) != 1 or len(end_positions) != 1:
        raise ValueError("index.html must contain exactly one generated-region marker pair")

    begin = begin_positions[0]
    end = end_positions[0]
    _assert_standalone_marker(document, BEGIN_MARKER, begin)
    _assert_standalone_marker(document, END_MARKER, end)
    if begin >= end:
        raise ValueError("generated-region markers are out of order")

    content_start = begin + len(BEGIN_MARKER)
    line_start = document.rfind("\n", 0, end) + 1
    end_indent = document[line_start:end]
    replacement = f"\n{generated.rstrip()}\n{end_indent}"
    return document[:content_start] + replacement + document[end:]


def update_index(index_path: Path, generated: str) -> bool:
    current = index_path.read_text(encoding="utf-8")
    updated = replace_generated_region(current, generated)
    if updated == current:
        return False

    mode = stat.S_IMODE(index_path.stat().st_mode)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=index_path.parent, prefix=f".{index_path.name}.", delete=False
    ) as temporary:
        temporary.write(updated)
        temporary.flush()
        os.fsync(temporary.fileno())
        temporary_path = Path(temporary.name)
    try:
        os.chmod(temporary_path, mode)
        os.replace(temporary_path, index_path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise
    return True


def main() -> int:
    print("Fetching repo data from GitHub API...")
    rows, sections = rank_repos(fetch_repos())
    for row in rows:
        print(f'  {row["name"]}: {row["count"]} commits')

    print("\n=== Featured Work (top 5) ===")
    for row in sections["Featured Work"]:
        print(f'  {row["name"]} ({row["count"]} commits) - {row["desc"]}')
    print("\n=== Previous Projects (>20 commits) ===")
    for row in sections["Previous Projects"]:
        print(f'  {row["name"]} ({row["count"]} commits) - {row["desc"]}')
    if not sections["Previous Projects"]:
        print("  (none)")
    print("\n=== Other (5+ commits) ===")
    for row in sections["Other"]:
        print(f'  {row["name"]} ({row["count"]} commits) - {row["desc"]}')
    if not sections["Other"]:
        print("  (none)")
    listed = sum(len(section) for section in sections.values())
    print(f"\nTotal repos: {len(rows)} | Listed: {listed} | Skipped (<5 commits): {len(rows) - listed}")

    index_path = Path(__file__).with_name("index.html")
    if update_index(index_path, render_projects(sections)):
        print(f"Updated {index_path.name}.")
    else:
        print(f"{index_path.name} is already up to date.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
