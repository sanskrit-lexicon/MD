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

## GitHub Issue Conventions

### Milestones and projects

Every issue belongs to exactly one milestone, which mirrors an org-level kanban project:

| Milestone | Project | Scope |
|---|---|---|
| Dictionary to Book (1) | Project 1 | Link targets and link splitting |
| Digitization Quality (2) | Project 2 | Scan quality, encoding, bug fixes, text corrections |
| Structured Data (3) | Project 3 | Markup normalisation, structured data, editorial questions |
| Major Enhancements (4) | Project 4 | Large new content, display upgrades, new versions |

### Type labels

Every issue has exactly one type label:

| Label | When to use |
|---|---|
| `link-target` | Building a click-through from a `<ls>` abbreviation to scanned PDF pages |
| `link-splitting` | Splitting combined `SOURCE N,N` refs into individual per-page links |
| `markup` | Normalising XML tag content or structure (`<ls>`, `<ab>`, etc.) |
| `text-correction` | Corrections to dictionary text (definitions, headwords) |
| `content-enhancement` | New material, display upgrades, or structural additions beyond correction |
| `encoding` | SLP1/IAST transcoding, character rendering, hyphen/dash normalisation |
| `scan-quality` | Replacing blurry, skewed, or missing scan pages |
| `bug` | Broken links, XML structure errors, broken download files |
| `question` | Scholarly or editorial questions requiring research before any code change |

### Severity labels

Every issue also has exactly one severity label:

| Label | When to use |
|---|---|
| `minor` | Targeted, self-contained fix — a handful of lines or a single file |
| `medium` | Standard unit of work — one verb pipeline run, a batch of corrections |
| `hard` | Large effort spanning many sources, files, or dictionaries |
