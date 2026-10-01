# Monthly commit chart measurement — October 1, 2026

## Result

The homepage chart covers August 2025 through September 2026. August 2026 has
9,837 unique commits and September 2026 has 3,820.

| Month | Unique commits |
| --- | ---: |
| August 2025 | 1,302 |
| September 2025 | 866 |
| October 2025 | 711 |
| November 2025 | 1,807 |
| December 2025 | 2,418 |
| January 2026 | 2,170 |
| February 2026 | 2,843 |
| March 2026 | 1,240 |
| April 2026 | 2,549 |
| May 2026 | 3,368 |
| June 2026 | 3,653 |
| July 2026 | 7,747 |
| August 2026 | 9,837 |
| September 2026 | 3,820 |

## Method

Scanned `.git` directory roots at depth five or less beneath `/Users/ianzepp/work`,
excluding `xai-org`. This found 225 metadata directories: one coordination
directory and two empty repositories were excluded, leaving 222 histories with
commits. Linked worktrees represented by `.git` files were not counted as
separate repository roots.

For each history, all commits reachable from local refs were considered across
all authors. Commit SHAs were deduplicated globally across repositories. Each
commit was assigned to its recorded author-date month, preserving the date
written in the commit metadata. The snapshot includes complete September; no
October commits are included.

The July 28 chart receipt described a 214-repository scan with the same broad
rules. Using the current local refs, the reconstructed method exactly matches
the August–December 2025 values, but not January–July 2026. No tested timestamp,
ref, or cutoff variant reproduced all twelve original values. The chart therefore
recalculates all months against the current snapshot rather than mixing the two
repository inventories. The difference reflects current local history/ref
coverage; it is not an adjusted estimate of the old July 28 snapshot.

## Current vector

`1302, 866, 711, 1807, 2418, 2170, 2843, 1240, 2549, 3368, 3653, 7747, 9837, 3820`
