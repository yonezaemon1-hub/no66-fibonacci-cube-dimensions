# Expected finite results

These are expected-output specifications, not redistributed private execution logs.

| n | dim | odim | md |
| --- | ---: | ---: | ---: |
| 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 |
| 3 | 2 | 2 | 3 |
| 4 | 2 | 3 | 3 |
| 5 | 3 | 3 | 3 |
| 6 | 3 | 4 | 4 |
| 7 | 4 | 5 | 5 |
| 8 | 4 | 5 | 5 |
| 9 | 4 | 7 | 7 |

The original outer enumeration must report NONE at each pair below, with exactly the stated number of tested subsets.

| n | k | Subsets |
| --- | ---: | ---: |
| 7 | 2 | 561 |
| 7 | 3 | 5,984 |
| 7 | 4 | 46,376 |
| 8 | 2 | 1,485 |
| 8 | 3 | 26,235 |
| 8 | 4 | 341,055 |
| 9 | 2 | 3,916 |
| 9 | 3 | 113,564 |
| 9 | 4 | 2,441,626 |
| 9 | 5 | 41,507,642 |
| 9 | 6 | 581,106,988 |

Other required outputs:

```text
MD n=8 k=5 tested=3478761 successes=2
DIM n=8 k=4 tested=84280 successes=1
INDEPENDENT_BFS_FINITE_REPLAY_PASS
INDEPENDENT_BASE7 n=9 N=89 k=6 found=0 tested=581106988
ORDERED_METRIC_DIM n=9 k=3 result=NONE tested=113564
METRIC4_FOUND
NO66_GAMMA9_FULL_MULTISET_PASS vertices=89 landmarks=7 unique_signatures=89 outside_unique=82
NONMONOTONE_CERTIFICATE_PASS
NO66_PUBLIC_FULL_REPLAY_PASS
```

Elapsed times vary and are not checked. `METRIC4_FOUND` is followed by the witness integers. The public runner also checks all witness and model-verification success markers. It tests no lower bound at n>=10. Quick mode has a PARTIAL final marker and omits the two longest exhaustive runs.

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
