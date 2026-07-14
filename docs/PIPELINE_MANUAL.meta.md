# PIPELINE_MANUAL.md — metadoc

_Created: 11-07-2026 · Last updated: 11-07-2026_

Companion record for
[docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/MD/blob/main/docs/PIPELINE_MANUAL.md).

## Purpose

The runbook over MD's workflows: the deva↔IAST comparison pipeline (steps
0–2b, with its tutorial layer and the generated-then-hand-reviewed
change-file gate), verbs01 verb identification, the per-issue correction
pattern, and the completed prefaces OCR.

## Audience

- An operator running a new comparison round or applying a reviewed change
  file.
- A contributor picking up the open issues (#1 verbs01, #5 mapping edges,
  #11 tooltips, #12 subheadwords).
- A newcomer using the tutorial layer (steps 0–1) to learn the codebase —
  the manual tells them which parts are teaching artifacts.

## Provenance

Authored 11-07-2026 by Fable 5 (`claude-fable-5`) under handoff
[H513-Fable_MD_correction_and_deva_iast_manual_10.07.26](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H513-Fable_MD_correction_and_deva_iast_manual_10.07.26.md)
(the H501–H531 per-repo manuals programme, Litpam-Indexator MANUAL.md gold
standard). Content read from the step readmes (working logs), the scripts'
usage lines, `verbs01/redo.sh`, README/CLAUDE.md, and the issue tracker —
none invented. The five §7 quirks were observed in the committed files.

## Ranked improvement backlog

| # | Item | Status |
|---|---|---|
| 1 | Fix the "step3" naming drift in [deva_iast_comp/readme.txt](https://github.com/sanskrit-lexicon/MD/blob/main/deva_iast_comp/readme.txt) (dirs are step2a/2b) | open |
| 2 | Parameterize verbs01's csl-orig-relative paths (a variable at the top of `redo.sh`, like GRA's) | open |
| 3 | Clean the copy-paste residue in the step2a readme (wrong script name, truncated sentences) — annotate, don't rewrite history | open |
| 4 | Special-case the ḻ/ḻh/m̐/hiatus mapping edges ([issue #5](https://github.com/sanskrit-lexicon/MD/issues/5)) so comparison reruns stop re-flagging them | open (owned by issue) |
| 5 | A one-command comparison rerun (fetch inputs + regenerate mismatch list) — today it is per-step manual | open |

## Known limitations

- The scholarly adjudication of each mismatch (deva right vs IAST right) is
  outside scope — the manual documents the mechanics and the review gate.
- `digentry.py`/`slp1iast.py` internals are not decoded; usage lines and
  the step2 readme remain the reference.
- Step readmes carry their own mojibake (logs, not data) — quoted only
  where legible.

## Related documents

- [README.md](https://github.com/sanskrit-lexicon/MD/blob/main/README.md) — repo overview, issue typology, prefaces status
- [CLAUDE.md](https://github.com/sanskrit-lexicon/MD/blob/main/CLAUDE.md) — architecture + command reference
- [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MD/blob/main/DATA_DICTIONARY.md) — markup tag reference
- Working logs: [deva_iast_comp/readme.txt](https://github.com/sanskrit-lexicon/MD/blob/main/deva_iast_comp/readme.txt) + per-step readmes · [verbs01/readme.txt](https://github.com/sanskrit-lexicon/MD/blob/main/verbs01/readme.txt)
- [csl-corrections correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md) — canonical delivery path
- Sibling verbs01-family manuals: [GRA SUBWORKFLOW_MANUAL](https://github.com/sanskrit-lexicon/GRA/blob/main/docs/SUBWORKFLOW_MANUAL.md) · [VCP COMPARISON_MANUAL](https://github.com/sanskrit-lexicon/VCP/blob/main/docs/COMPARISON_MANUAL.md)

## Revision history

| Date | Change | By |
|---|---|---|
| 11-07-2026 | Initial version (H513) | Fable 5 (`claude-fable-5`) |

---

_Dr. Mārcis Gasūns_
