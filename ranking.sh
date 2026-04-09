#!/usr/bin/env python3
import json
import subprocess
import sys


OWNER = "ianzepp"
SKIP = {
    "archived-projects",
    "personal",
    "ianzepp.dev",
    "dotfiles",
    "homebrew-tap",
    "0-prework-assignment",
}


def run(*args: str) -> str:
    return subprocess.check_output(args, text=True)


def fetch_repos() -> list[dict]:
    cursor = None
    repos: list[dict] = []

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
        repositories = payload["data"]["repositoryOwner"]["repositories"]
        repos.extend(repositories["nodes"])
        if not repositories["pageInfo"]["hasNextPage"]:
            return repos
        cursor = repositories["pageInfo"]["endCursor"]


def main() -> int:
    print("Fetching repo data from GitHub API...")

    rows: list[dict] = []
    for repo in fetch_repos():
        name = repo["name"]
        if name in SKIP:
            continue

        branch = repo.get("defaultBranchRef") or {}
        target = branch.get("target") or {}
        history = target.get("history") or {}
        count = history.get("totalCount") or 0
        desc = repo.get("description") or name
        private = bool(repo["isPrivate"])

        rows.append(
            {
                "name": name,
                "count": count,
                "desc": desc,
                "private": private,
            }
        )
        print(f"  {name}: {count} commits")

    rows.sort(key=lambda row: (-row["count"], row["name"].lower()))

    featured: list[str] = []
    previous: list[str] = []
    other: list[str] = []
    listed = 0

    for row in rows:
        if row["count"] < 5:
            continue

        listed += 1
        prefix = "[private] " if row["private"] else ""
        entry = f"{prefix}{row['name']} ({row['count']} commits) - {row['desc']}"

        if listed <= 5:
            featured.append(entry)
        elif row["count"] > 20:
            previous.append(entry)
        else:
            other.append(entry)

    print("\n=== Featured Work (top 5) ===")
    for entry in featured:
        print(f"  {entry}")

    print("\n=== Previous Projects (>20 commits) ===")
    if previous:
        for entry in previous:
            print(f"  {entry}")
    else:
        print("  (none)")

    print("\n=== Other (5+ commits) ===")
    if other:
        for entry in other:
            print(f"  {entry}")
    else:
        print("  (none)")

    print(
        f"\nTotal repos: {len(rows)} | Listed: {listed} | "
        f"Skipped (<5 commits): {len(rows) - listed}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
