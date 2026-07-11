# MD Pipeline Manual

_Created: 11-07-2026 · Last updated: 11-07-2026_

The operator manual for the MD (Macdonell 1893) working repo: the
Devanāgarī↔IAST comparison pipeline (`deva_iast_comp/`, steps 0–2b), the
verb-identification chain (`verbs01/`), the per-issue correction pattern
(`mdissues/`), and the prefaces OCR — one runbook over workflows whose
detail lives in per-directory `readme.txt` working logs.

Companion metadoc: [docs/PIPELINE_MANUAL.meta.md](https://github.com/sanskrit-lexicon/MD/blob/main/docs/PIPELINE_MANUAL.meta.md).

---

## 1. Cheat-sheet

```sh
# deva↔IAST comparison — the two mechanical change-file generators:
cd deva_iast_comp/step2
curl https://raw.githubusercontent.com/sanskrit-lexicon/COLOGNE/master/iast/slp1_iast.txt -o temp_slp1_iast.txt
curl https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/master/v02/md/md.txt   -o temp_md.txt
python make_change_circumflex.py temp_md.txt temp_slp1_iast.txt change_1.txt
#   → hand-review change_1_edit.txt → apply:
python updateByLine.py temp_md_00.txt change_1_edit_copy.txt temp_md_01.txt

cd ../step2b
python make_change_pc_2b.py temp_md_0.txt change_2b.txt      # pc (page-column) errors

# verbs01 — verb identification + MW correlation (path caveat: §3.2)
cd verbs01 && sh redo.sh

# any correction, all workflows:
python updateByLine.py <input> <change_file> <output>
```

**Delivery rule:** the canonical text is
[csl-orig/v02/md/md.txt](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/md/md.txt);
every fix is a `NNN old`/`NNN new` change file routed through the canonical
[correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md)
(org agents: queue for the batched PR, never a direct csl-orig push).

## 2. Data-flow diagram

```
csl-orig/v02/md/md.txt   (canonical; entries carry BOTH a Devanagari-derived
│                         SLP1 form {#…#} and the printed IAST form)
│
├── deva_iast_comp/  — DO THE TWO SCRIPTS AGREE?  (the error detector)
│     data.txt  = the paired deva/IAST lines from csl-orig issue #628
│     step0/    read/write warm-up            ┐ ALSO a deliberate Python
│     step1/    split → strip accents →       │ tutorial (issue #2): programs
│               lowercase → slp1→iast →       │ are numbered "1st…8th" with
│               keep only MISMATCHES          ┘ study suggestions
│     step2/    circumflex-class errors → make_change_circumflex.py
│               → change_1.txt → HAND REVIEW → updateByLine.py     (issue #6)
│     step2a/   page-column (pc) errors, round 1                   (issue #7)
│     step2b/   pc errors, round 2 → make_change_pc_2b.py
│     (readme's "step3" = what became step2a/2b — renumbered)
│
├── verbs01/  — WHICH ENTRIES ARE VERBS, MAPPED TO MW      (issue #1, open)
│     mwverb.py + mwverbs1.py  ← builds MW verb tables from ../../mw/mw.txt
│     md_verb_filter.py (+ md_verb_exclude.txt) → md_verb_filter.txt
│     md_verb_filter_map.py → MD↔MW spelling map
│     preverb0.py / preverb1.py (slp1, deva) + md_upasargas.txt
│       → md_preverb1{,_deva}.txt  (final correlation tables)
│
├── mdissues/issueNNN/  — per-issue correction workspaces
│     issue8 (IAST batch) · issue10 (homonym metalines) · issue11
│     (abbreviation tooltips) · issue12 (subheadwords) · issue13 (English errors)
│
└── prefaces/  — front-matter OCR (EN source) + RU translation, COMPLETE
      (10 pages: title, Max Müller dedication, 7-page preface, alphabet+abbrevs)
```

## 3. Step-by-step operator walkthrough

### 3.1 The deva↔IAST comparison (`deva_iast_comp/`)

**The idea:** every MD entry states the headword twice — as SLP1 (from the
Devanāgarī) and as printed IAST. Transliterating the SLP1 to IAST and
comparing it against the printed IAST (accents stripped, lowercased) makes
every disagreement a **digitization-error candidate**. The pipeline grew as
a numbered tutorial (its readme says so: "intended also as a tutorial on
Python programming" — the contributor onboarding of
[issue #2](https://github.com/sanskrit-lexicon/MD/issues/2)), so steps 0–1
are teaching programs over the frozen
[data.txt](https://github.com/sanskrit-lexicon/MD/blob/main/deva_iast_comp/data.txt)
(the paired lines from
[csl-orig issue #628](https://github.com/sanskrit-lexicon/csl-orig/issues/628)):

- **step0** — read/write warm-up (`readwrite.py`); committed outputs are
  teaching artifacts, not pipeline products.
- **step1** — the real comparison logic, built up program by program
  (`readwriteA2`–`A5_low`): split each line into
  `orig / slp1 / rest / iast`, strip IAST accents (`iastrev`), lowercase,
  transliterate slp1→iast, and emit **only the abnormal/mismatching lines**
  (`readwriteA5_low.py` is the culmination; `_countabnormal` tallies).
  Support scripts: `bytes.py` (byte-level inspection), `nonascii.py`
  (character census → `nonascii.txt`).
- **step2** ([issue #6](https://github.com/sanskrit-lexicon/MD/issues/6)) —
  the first *production* round: `slp1iast.py` parses the canonical mapping
  table (fetched from
  [COLOGNE/iast/slp1_iast.txt](https://github.com/sanskrit-lexicon/COLOGNE/blob/master/iast/slp1_iast.txt)),
  `digentry.py` parses md.txt into Entry objects,
  `make_change_circumflex.py` emits a change file for the
  circumflex-class errors. **The generated `change_1.txt` is never applied
  raw** — it is copied once to `change_1_edit.txt`, hand-reviewed, and the
  reviewed copy applied with `updateByLine.py`.
- **step2a / step2b** ([issue #7](https://github.com/sanskrit-lexicon/MD/issues/7))
  — same pattern for page-column (`pc`) reference errors
  (`make_change_pc.py`, then `make_change_pc_2b.py` for the residue).
  These are what the top-level readme still calls "step3" — the
  directories were renumbered, the readme wasn't.

**What a mismatch means:** either the Devanāgarī keyboarding or the IAST
keyboarding is wrong (occasionally both are right and the *rule* needs a
special case — e.g. the ḻ/ḻh/m̐ hiatus characters of
[issue #5](https://github.com/sanskrit-lexicon/MD/issues/5), still open).
The mismatch list is a review queue, never an auto-fix.

### 3.2 Verb identification (`verbs01/`)

Same family as the GRA/VCP verbs01 workflows; this copy is self-contained
(it builds its own MW tables rather than reading MWS's). `sh redo.sh` runs:
`mwverb.py` (harvest MW verb entries) → `mwverbs1.py` (merge per headword)
→ `md_verb_filter.py` (+ hand-kept `md_verb_exclude.txt`) →
`md_verb_filter_map.py` (MD↔MW spellings) → `preverb0.py`/`preverb1.py`
(upasarga parsing via `md_upasargas.txt`; run twice for SLP1 and
Devanāgarī) → **`md_preverb1.txt` / `md_preverb1_deva.txt`**.

**Path caveat:** the script was written to run from a `temp_verbs/`
subdirectory *inside* `csl-orig/v02/md/` — hence `../md.txt` and
`../../mw/mw.txt`. Run from this repo, those paths dangle: point them at
your csl-orig clone (or recreate the temp_verbs placement) before `sh
redo.sh`. Tracking issue:
[#1](https://github.com/sanskrit-lexicon/MD/issues/1) (open).

### 3.3 Per-issue corrections (`mdissues/issueNNN/`)

The standard Cologne pattern: pin a copy of `md.txt`, build a change file
(often with a small per-issue script), hand-audit, apply with
`updateByLine.py`, validate the rebuilt XML, deliver via the
[correction workflow](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md).
Existing workspaces: `issue8` (IAST corrections batch), `issue10` (homonym
identifiers in metalines), `issue11` (abbreviation tooltips — open,
medium), `issue12` (MW-style subheadwords — open, hard), `issue13`
(2020 English-errors batch).

### 3.4 Prefaces (`prefaces/`) — complete

Per-scan-page OCR of the front matter (English source → base `.md` is the
English edition) + Russian translations, consolidated editions built by
`build_combined.py`; all 10 pages done. See
[prefaces/README.md](https://github.com/sanskrit-lexicon/MD/blob/main/prefaces/README.md).
Operational note preserved in the root README: background OCR subagents
reproducibly hit a spurious content-filter error on this dictionary — run
preface OCR on the main thread.

## 4. Environment & prerequisites

- **Python 3** (the tutorial steps are deliberately stdlib-only); `curl`
  for fetching the pinned inputs; `sh` via Git Bash on Windows.
- **Sibling data:** `csl-orig` (canonical `md.txt`; also `mw/mw.txt` for
  verbs01) and the
  [COLOGNE](https://github.com/sanskrit-lexicon/COLOGNE) repo's
  `slp1_iast.txt` mapping table (step2 fetches it by URL).
- No secrets, no pip installs.

## 5. Symptom → cause → cure

| Symptom | Cause | Cure |
|---|---|---|
| Top-level readme says "step3" but there is no `step3/` | Renumbered to `step2a`/`step2b`; readme never updated | The pc-error work is §3.1's step2a/2b |
| `verbs01/redo.sh`: "can't open ../md.txt" | Paths assume the historic `csl-orig/v02/md/temp_verbs/` placement | Point `../md.txt` / `../../mw/mw.txt` at your csl-orig clone (§3.2) |
| step2a readme's commands look wrong (circumflex script named in the pc step, truncated sentences) | Copy-paste residue in the working log | Trust the scripts: the pc generators are `make_change_pc.py` / `make_change_pc_2b.py`; the readme is a log, not a spec |
| Tempted to apply a generated `change_1.txt` directly | The generated file is a *candidate* list | Copy once to `change_1_edit.txt`, hand-review, apply only the reviewed copy (§3.1 step2) |
| slp1→iast disagrees on ḻ / ḻh / m̐ / hiatus characters | Known mapping-edge cases, not data errors | [Issue #5](https://github.com/sanskrit-lexicon/MD/issues/5) — special-case the rule, don't "fix" the text |
| `updateByLine.py` line-count mismatch | Change file built against a different md.txt state | Re-pin the input to the state the change file names (the canonical workflow doc covers this class) |
| step0/step1 committed outputs look like junk | They are tutorial artifacts (numbered teaching programs) | Leave them; the production rounds are step2+ |
| Preface OCR subagent dies with a content-filter error | Known spurious failure on this dictionary in background agents | Run on the main thread (root README note) |

## 6. Glossary

| Term | Meaning |
|---|---|
| deva↔IAST comparison | Checking the SLP1 (Devanāgarī-derived) headword against the printed IAST rendering — disagreement = digitization-error candidate |
| `iastrev` | The pipeline's accent-stripped (later lowercased) form of the printed IAST, used for comparison |
| abnormal | step1's label for a line whose `iastrev` ≠ slp1→iast transliteration — the review queue |
| circumflex errors | The step2 error class: â/î/û where IAST wants ā/ī/ū (and kin) |
| `pc` | Page-column reference in the metaline, locating an entry in the 1893 print — step2a/2b's error class |
| `data.txt` | The frozen paired-lines dataset from csl-orig issue #628 that steps 0–1 teach on |
| `digentry.py` / `slp1iast.py` | The step2 parsing modules: md.txt → Entry objects; the canonical SLP1↔IAST table |
| upasarga | Verbal prefix; verbs01 parses prefixed verbs via `md_upasargas.txt` |
| metaline | `<L>…<pc>…<k1>…<k2>…` entry header (id, page-column, headword, sort key) |
| `updateByLine.py` | The shared line-keyed change-file applier used by every workflow here |

## 7. Maintainer appendix

- **Live vs finished:** open work = verbs01 (#1), the mapping edge cases
  (#5), abbreviation tooltips (#11), subheadwords (#12). Finished
  campaigns = the comparison rounds (#4/#6/#7), the correction batches
  (#8/#9/#10/#13/#14), prefaces. The tutorial layer (steps 0–1) is
  intentionally frozen.
- **Observed quirks** (11-07-2026, while writing this manual): (1) the
  "step3" naming drift in
  [deva_iast_comp/readme.txt](https://github.com/sanskrit-lexicon/MD/blob/main/deva_iast_comp/readme.txt);
  (2) verbs01's csl-orig-relative paths (§3.2); (3) copy-paste residue in
  the step2a readme; (4) step readmes carry mojibake for the characters
  they discuss (encoding damage in the logs, not in the data); (5) the
  generated-then-hand-edited change-file convention
  (`change_1.txt` → `_edit` → `_edit_copy`) is easy to misread as
  redundancy — it is the review gate.
- **Invariant:** generated change files are candidate lists; only
  hand-reviewed copies are ever applied. The comparison pipeline finds
  errors, humans adjudicate them, the correction workflow delivers them.
- **Cross-repo edges:** csl-orig (canonical text + issue #628 data),
  COLOGNE (`slp1_iast.txt` canonical mapping), MW (`mw.txt` for verbs01),
  the same verbs01 family in
  [GRA](https://github.com/sanskrit-lexicon/GRA/blob/main/docs/SUBWORKFLOW_MANUAL.md)
  and VCP (fix shared-family bugs across the set).
- **Issue taxonomy:** dictionary-repo taxonomy — see
  [CLAUDE.md](https://github.com/sanskrit-lexicon/MD/blob/main/CLAUDE.md)
  and the README's typology tables.

---

_Dr. Mārcis Gasūns_
