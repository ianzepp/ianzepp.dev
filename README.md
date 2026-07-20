# ianzepp.dev

Static GitHub Pages site for `ianzepp.dev`.

This repo hosts the autobiographical portfolio at `https://ianzepp.dev/`.

Private source material and executable installers are intentionally kept out of
this publication repository unless a separate review proves they are safe to
publish.

## Repository Layout

- `index.html`: the hand-authored career narrative, evidence ledger, selected-work folio, generated project archive, styles, and client-side search
- `fonts/`: self-hosted woff2 faces (Cinzel, IBM Plex Mono; both SIL OFL). They are vendored because the publication policy bans third-party font fetches from the served page.
- `ranking.sh`: the documented, non-interactive regeneration command
- `sitegen.py`: GitHub discovery, ranking policy, escaping, and generated-region renderer
- `CNAME`: GitHub Pages custom domain configuration
- `tests/test_sitegen.py`: deterministic renderer and seam validation

## How The Site Works

The site is intentionally simple:

- There is no framework or dependency-heavy build step
- The project list is generated inside the marked region in `index.html`
- The search bar is plain client-side JavaScript in `index.html`
- GitHub Pages serves the repo as static files

The HTML outside `BEGIN GENERATED PROJECTS` and `END GENERATED PROJECTS` is hand-authored and is never rewritten by the generator. The generated region lives inside the collapsed repository archive, so repository refreshes cannot reorder or redefine the autobiographical narrative. The generator fails instead of guessing if either marker is missing, duplicated, out of order, or embedded in another line.

## Live Repo Data Workflow

`ranking.sh` fetches live repository data and regenerates the project region.

It currently:

- uses the GitHub GraphQL API through authenticated `gh`
- skips a small hardcoded set of repos that should not appear on the site
- ignores forks
- reads default-branch commit totals from GitHub
- reads repo descriptions and privacy status from GitHub
- sorts repos by commit count descending
- renders three tiers:
  - `Featured Work`: top 5 repos
  - `Previous Projects`: remaining repos with more than 20 commits
  - `Other`: remaining repos with at least 5 commits

The ranking policy is unchanged: skipped repositories and forks are excluded, repositories with fewer than five commits are not listed, the first five listed repositories are featured, later repositories over twenty commits are previous projects, and the rest are other projects. Ties sort by repository name case-insensitively.

Only repositories with explicit public visibility metadata are published. Public repositories are linked to their GitHub page and all generated names and descriptions are HTML-escaped. Missing or private visibility metadata is excluded fail-closed. Only the existing public display fields (name, description, and commit count) are used.

## Rebuilding The Website From Live Data

The unattended rebuild command is:

```bash
./ranking.sh
```

It requires an authenticated `gh` session and updates only `index.html` when the generated content changes. It uses an atomic replacement and exits nonzero on GitHub/API errors or unsupported HTML seams. Running it again with unchanged GitHub data produces no diff.

The deterministic validation suite is:

```bash
python3 -m unittest discover -s tests
```

After a live regeneration, inspect `git diff -- index.html`; the page shell and `CNAME` should remain untouched. Run the publication-safety tests before committing. This task does not deploy or push changes.

## Important History

The intended workflow was reconstructed from archived transcripts.

Those transcripts show:

- the repo was originally created as a GitHub Pages site for the landing page and later accumulated an install-script surface
- `ranking.sh` originally used local cloning to count commits
- that clone-based approach was later replaced with GitHub API calls because cloning every repo wasted local disk space
- the site content remained manual even after the ranking script was improved

So today the correct mental model is:

- `ranking.sh` discovers and ranks live repo data
- `sitegen.py` renders only the explicit generated project region
- `index.html` remains the hand-authored presentation layer around that region

## Dependencies

`ranking.sh` expects:

- `gh` authenticated against GitHub
- `python3`
