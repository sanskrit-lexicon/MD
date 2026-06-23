# MD front matter (prefaces)

Faithful OCR + translation of the **front matter** of **Arthur A. Macdonell's *A Sanskrit-English Dictionary, Being a Practical Handbook with Transliteration, Accentuation, and Etymological Analysis Throughout*** (London: Longmans, Green, and Co., **1893**). Dedicated to Professor F. Max Müller.

Source scans (Cologne Digital Sanskrit Dictionaries):
<https://sanskrit-lexicon.uni-koeln.de/scans/csldev/csldoc/build/dictionaries/prefaces/mdpref.html>

**Source language: English** — the base per-page `.md` files are the English edition (no separate `.en.md`); a Russian translation `.ru.md` accompanies every page.

> **Status: in progress.** Pages 01–06 (Title, Dedication, and the four-page Preface, pp. v–viii) are complete. The remaining front-matter pages (07–10 — the abbreviations list and transliteration/grammar tables, scans `md_Page_012`–`015`) are **pending** and will be added in a follow-up pass.

## File conventions

| Suffix | What it is |
|---|---|
| `mdprefNN.md` | Faithful transcription (English source) |
| `mdprefNN.ru.md` | Russian translation |
| `scans/*.png` | Source scan images |
| `build_combined.py` | Rebuilds the consolidated editions (`DICT=md python build_combined.py`) |

## Consolidated editions

| Edition | File |
|---|---|
| English (so far) | [mdpref_all.en.md](mdpref_all.en.md) |
| Russian (so far) | [mdpref_all.ru.md](mdpref_all.ru.md) |

## Contents

| # | Section | Vol. | Source | RU | Status |
|---|---|---|---|---|---|
| 01 | Title | 1 | [mdpref01.md](mdpref01.md) | [ru](mdpref01.ru.md) | ✓ |
| 02 | Dedication | 1 | [mdpref02.md](mdpref02.md) | [ru](mdpref02.ru.md) | ✓ |
| 03 | Preface, 1 | 1 | [mdpref03.md](mdpref03.md) | [ru](mdpref03.ru.md) | ✓ |
| 04 | Preface, 2 | 1 | [mdpref04.md](mdpref04.md) | [ru](mdpref04.ru.md) | ✓ |
| 05 | Preface, 3 | 1 | [mdpref05.md](mdpref05.md) | [ru](mdpref05.ru.md) | ✓ |
| 06 | Preface, 4 | 1 | [mdpref06.md](mdpref06.md) | [ru](mdpref06.ru.md) | ✓ |
| 07–10 | Abbreviations & tables | 1 | — | — | pending |

## Notes

- The Preface (signed by Macdonell) sets out the scope (post-Vedic vocabulary plus accessible Vedic selections), the list of books referred to, the Rigveda hymn list, and the arrangement, type, abbreviation, and punctuation conventions.
- Macdonell's older transliteration is preserved verbatim (â = ā, î = ī, û = ū; *k*, *kh*, *n*, *ṛ* etc. in italics), as are the inline Devanāgarī examples.
