# v0.4 to public v1.0

The mathematical definitions, sections 1-4, every theorem, lemma, proposition and proof, all mathematical expressions, all finite values and witnesses, and all seven bibliography entries are unchanged from the canonical v0.4 manuscript.

Editorial changes only:

1. Remove the author's correspondence email.
2. Change the private draft/HOLD version display and publication paragraph to Preprint v1.0 with the authorized public-release status and scoped AI/Windows status.
3. Change the abstract's word "draft" to "preprint".
4. Describe the public packaging as eight unchanged extracted source files and a separate runner, with frozen original research archives retained privately.
5. Update the obsolete claim that the original Windows result archive was unavailable: it has now been supplied, its integrity and six payload hashes independently checked, and its saved results compared with the evidence audit. The author performed the Windows execution; the publication auditor inspected the saved evidence.
6. Set the PDF title metadata to the complete title and allow extra line-breaking flexibility in the preamble to keep the long verification filename inside the text margins. No mathematical text is edited.

All eight `src/` files are byte-identical to their frozen originals. `run_reproduce.py` is a new public execution wrapper that handles portable paths, compilation, result checks and manifest checks without changing the mathematical source files. Private archives and raw logs are excluded. Source comments retaining older version numbers describe their original creation and do not override the release status.

NOVELTY INCONCLUSIVE. REFERENCES PARTIAL. Human peer review not performed. All rights reserved.
