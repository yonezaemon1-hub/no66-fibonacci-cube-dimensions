# Research No.66 - Preprint v1.0

**Exact Outer Multiset Dimensions of Fibonacci Cubes Through Dimension Nine: An Exact Three-Landmark Ordered--Unordered Gap**

Ryutaro Yonezu - Independent Researcher. 13 November 2026.

The Fibonacci cube Gamma_n has the binary words of length n avoiding adjacent ones as its vertices, with an edge for a one-bit change. This computer-assisted preprint determines the following finite values.

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vertices | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 |
| Ordinary metric dimension dim | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 4 |
| Outer multiset dimension odim | 1 | 1 | 2 | 3 | 3 | 4 | 5 | 5 | 7 |
| Full multiset dimension md | 1 | 1 | 3 | 3 | 3 | 4 | 5 | 5 | 7 |

In particular, **dim(Gamma_9)=4 and odim(Gamma_9)=md(Gamma_9)=7**. The full unordered versus ordered gap is three. The Gamma_6 nonmonotonicity example is included: S={001010,010001,010010,010101} resolves outside vertices, while S union {000001} does not; 001001 and 010100 then share the multiset {1,2,2,3,4}.

These are finite conclusions for n=1..9. The supplied witnesses at n=10 and n=11 prove upper bounds only, respectively odim<=7 and odim<=9. No arbitrary-n formula, lower bound for n>=10, general trend or historical priority is asserted.

## Verification and scholarly status

- Independent AI audit: PASS within the documented mathematical and computational scope. This is not institutional certification or human peer review.
- Windows 10 / PowerShell 5.1 reproduction: PASS, performed on the author's computer. The saved evidence ZIP and all six payload hashes were independently checked and agree with the independent evidence-audit report. The auditor did not operate the author's PC.
- Original and independent base-seven searches each tested all 581,106,988 six-landmark subsets for Gamma_9, finding zero resolving sets. The seven-landmark witness distinguishes all 89 vertices.
- Complete BFS enumeration at n=8 tests all 3,478,761 five-landmark subsets and finds two full multiset resolving sets. Ordered Gamma_9 checks reject all 113,564 three-landmark subsets and verify a four-landmark witness.
- Publication preparation: a fresh complete Linux run of the public portable wrapper passed, including both 581,106,988-subset Gamma_9 searches, all smaller cardinalities, the n<=8 BFS enumeration and the explicit certificates.
- Earlier integrated Linux attempts interrupted by a time limit remain PARTIAL records. They are distinct from the complete saved Windows evidence and any separately documented publication replay.
- **NOVELTY INCONCLUSIVE. REFERENCES PARTIAL. Human peer review: NOT PERFORMED.** Literature implications have not been exhaustively excluded. In particular, dim(Gamma_9)=4 is a computational comparator, with no independent historical-novelty claim.

## Public files

- `No66_v1.0_PREPRINT.pdf`: English preprint.
- `No66_v1.0_SOURCE.tex`: matching LaTeX source.
- `No66_v1.0_REPRODUCIBILITY.zip`: eight unchanged mathematical source files, a separate portable runner, expected results and checksums.
- `SHA256SUMS.txt`: checksums for the public release assets and README.

The public bundle excludes the private research archives, Windows raw logs, workstation paths, contact email, internal audit reports and previous drafts. Its code is extracted byte-for-byte from the frozen sources; packaging and execution are handled by a separate wrapper. See `repro/EDITORIAL_CHANGES.md` and `repro/FROZEN_CODE_SHA256.txt`.

## Reproduce

Requires Python 3.10 or newer (standard library only), a C++17/C++20 compiler and OpenMP. GCC/MinGW g++ is supported; no paid service or network access is used by the verifier. LaTeX with geometry, lmodern, AMS packages, booktabs, enumitem, hyperref and microtype is needed only to rebuild the PDF.

Extract the reproducibility ZIP and enter its `No66_v1.0_REPRODUCIBILITY` directory, then run:

```text
python -B run_reproduce.py --threads 4
```

Expected final marker: `NO66_PUBLIC_FULL_REPLAY_PASS`. The two Gamma_9 six-landmark exhaustions may take several minutes or longer, depending on hardware. All smaller outer cardinalities are checked individually; upward monotonicity is not assumed. Binaries are built in a temporary directory and removed when the runner finishes.

For a shorter, explicitly incomplete replay:

```text
python -B run_reproduce.py --quick --threads 4
```

The quick mode omits both Gamma_9 six-landmark exhaustive runs and ends with `NO66_PUBLIC_QUICK_REPLAY_PARTIAL`; it does not independently reproduce the lower bound seven. Source hashes and manifest coverage are checked by both modes. On Linux, `python3` may be substituted for `python`. If needed use `--compiler` with the installed compiler path.

## Rights

Copyright (c) 2026 Ryutaro Yonezu. **All rights reserved.** This applies to the manuscript, verification sources and accompanying materials. No MIT, Apache, GPL or Creative Commons permission is granted by this release.
