# ianzepp.dev

Static GitHub Pages site for `ianzepp.dev`.

This repo serves two purposes:

1. Host the landing page at `https://ianzepp.dev/`
2. Host static per-project install scripts such as `https://ianzepp.dev/cassio/install.sh`

## Repository Layout

- `index.html`: the entire website, including markup, styles, project listings, and client-side search
- `ranking.sh`: fetches live repository metadata from GitHub and prints a ranked report
- `cassio/install.sh`: static install script served from the site
- `CNAME`: GitHub Pages custom domain configuration

## How The Site Works

The site is intentionally simple:

- There is no framework, build step, or data pipeline
- The project list is hardcoded directly in `index.html`
- The search bar is plain client-side JavaScript in `index.html`
- GitHub Pages serves the repo as static files

That means the page itself is not generated automatically today. The ranking data is generated separately, then applied manually to `index.html`.

## Live Repo Data Workflow

`ranking.sh` is the live-data discovery script.

It currently:

- uses `gh repo list` to fetch repositories for `ianzepp`
- skips a small hardcoded set of repos that should not appear on the site
- ignores forks
- uses the GitHub API to estimate commit counts from pagination headers
- reads repo descriptions and privacy status from GitHub
- sorts repos by commit count descending
- prints three tiers:
  - `Featured Work`: top 5 repos
  - `Previous Projects`: remaining repos with more than 20 commits
  - `Other`: remaining repos with at least 5 commits

This script is the source of truth for ranking logic, but not for HTML generation.

## Rebuilding The Website From Live Data

Current rebuild process:

1. Run `./ranking.sh`
2. Review the ranked output
3. Update the hardcoded project entries in `index.html`
4. Commit and push
5. GitHub Pages serves the updated static site

Example:

```bash
./ranking.sh
```

## Important History

The intended workflow was reconstructed from archived transcripts in `~/github/ianzepp/personal/transcripts/`.

Those transcripts show:

- the repo was originally created as a GitHub Pages site for both the landing page and install-script hosting
- `ranking.sh` originally used local cloning to count commits
- that clone-based approach was later replaced with GitHub API calls because cloning every repo wasted local disk space
- the site content remained manual even after the ranking script was improved

So today the correct mental model is:

- `ranking.sh` discovers and ranks live repo data
- `index.html` remains the hand-authored presentation layer

## Dependencies

`ranking.sh` expects:

- `gh` authenticated against GitHub
- `jq`

## Known Limitation

There is currently no generator that writes project data back into `index.html`.

If full automation is desired, the next step would be to split:

- repo discovery/data collection
- a machine-readable data file
- an HTML template or generator

Until then, the rebuild flow is intentionally manual.
