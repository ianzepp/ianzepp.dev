# ianzepp.dev

Static GitHub Pages site for `ianzepp.dev`.

This repo serves two purposes:

1. Host the autobiographical portfolio at `https://ianzepp.dev/`
2. Host static per-project install scripts such as `https://ianzepp.dev/cassio/install.sh`

## Repository Layout

- `index.html`: the hand-authored career narrative, evidence ledger, selected-work folio, generated project archive, styles, and client-side search
- `content/CAREER-HISTORY.md`: comprehensive factual source material for timelines, project drill-downs, case studies, and future site content
- `ranking.sh`: the documented, non-interactive regeneration command
- `sitegen.py`: GitHub discovery, ranking policy, escaping, and generated-region renderer
- `cassio/install.sh`: static install script served from the site
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

Public repositories are linked to their GitHub page and all generated names and descriptions are HTML-escaped. Private repositories remain in their ranked tier as non-linked text with a `private` badge; no private GitHub URL is generated. Only the existing display fields (name, description, privacy, and commit count) are used.

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

After a live regeneration, inspect `git diff -- index.html`; the page shell, `CNAME`, and `cassio/install.sh` should remain untouched. This task does not deploy or push changes.

## Important History

The intended workflow was reconstructed from archived transcripts in `~/github/ianzepp/personal/transcripts/`.

Those transcripts show:

- the repo was originally created as a GitHub Pages site for both the landing page and install-script hosting
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
