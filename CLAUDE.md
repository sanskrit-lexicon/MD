# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **MD (Macdonell's Sanskrit-English Dictionary) data processing** repository, part of the [sanskrit-lexicon](https://github.com/sanskrit-lexicon) project. It contains scripts and data for correcting and enriching the Macdonell dictionary.

The primary input is `md.txt` in the sibling repo `csl-orig/v02/md/md.txt`.

## Architecture

| Directory | Purpose |
|---|---|
| `verbs01/` | Verb identification and correspondence with MW dictionary |
| `deva_iast_comp/` | Devanagari-to-IAST comparison pipeline (steps 0–2b) |
| `mdissues/issueNNN/` | Per-issue correction workflows |

### Verb Pipeline (`verbs01/`)

Run from `verbs01/` with `sh redo.sh`. Sequential steps:

```sh
python mwverb.py mw ../../mw/mw.txt mwverbs.txt
python mwverbs1.py mwverbs.txt mwverbs1.txt
python md_verb_filter.py ../md.txt md_verb_exclude.txt md_verb_filter.txt
python md_verb_filter_map.py md_verb_filter.txt mwverbs1.txt md_verb_filter_map.txt
python preverb0.py md_verb_filter_map.txt mwverbs1.txt md_preverb0.txt
python preverb1.py md_preverb0.txt md_preverb1.txt
```

### Deva-IAST Comparison (`deva_iast_comp/`)

Sequential steps for comparing Devanagari and IAST renderings:
- `step0/` — read/write tests, encoding exploration
- `step1/` — byte-level analysis, SLP1-IAST transcoding, non-ASCII character census
- `step2/` — circumflex and correction change files, `updateByLine.py` application
- `step2a/` — page-column (pc) error corrections
- `step2b/` — further pc corrections

### `updateByLine.py` Pattern

Used across `mdissues/*/` and `deva_iast_comp/step2*/`:
```sh
python updateByLine.py <input_file> <changefile> <output_file>
```

## Dependencies

- **Python 3**
- **md.txt** — in sibling repo at `../csl-orig/v02/md/md.txt`
- **mw.txt** — in sibling repo for verb pipeline cross-reference

