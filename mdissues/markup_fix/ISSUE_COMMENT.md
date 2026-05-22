### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 (PWG) and https://github.com/sanskrit-lexicon/PWK/issues/113 (PWK) for `md.txt`.

I ran the same two-job recipe over `csl-orig/v02/md/md.txt`: auto-fix the few things with a single safe resolution; audit everything else with line refs. Added `08_markup_fix.py` plus outputs to a new `mdissues/markup_fix/` folder on the branch `markup-fix-audit`.

@funderburkjim @Andhrabharati — please review the findings listed below.

## Markup fixer + audit for `md.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>X</ab> Y</ab>` | `<ab>X Y</ab>` |
| `<lex> word </lex>` | `<lex>word</lex>` |
| `<ab> word </ab>` | `<ab>word</ab>` |
| `<hom> word </hom>` | `<hom>word</hom>` |

Whitespace trimming applies to all 12 paired tag(s) in `md.txt`: `<lex>`, `<ab>`, `<hom>`, `<cl>`, `<per>`, `<bot>`, `<lang>`, `<ls>`, `<zoo>`, `<gk>`, `<lat>`, `<fr>`. The original file is never modified — output goes to `md_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format). **Output is byte-identical to source** (no auto-fixes triggered).

### Closing-tag inventory in current `md.txt`

| Tag | Count |
|---|---:|
| `</lex>` | 56 |
| `</123)>` | ? |
| `</ab>` | 46 |
| `</956)>` | ? |
| `</hom>` | 1 |
| `</363)>` | ? |
| `</cl>` | 993 |
| `</per>` | 314 |
| `</bot>` | 155 |
| `</lang>` | 102 |
| `</ls>` | 58 |
| `</zoo>` | 15 |
| `</gk>` | 10 |
| `</lat>` | 3 |
| `</fr>` | 1 |

### What it found in current `md.txt`

- 0 whitespace trims — byte-identical to source.
- 1 `<ab n="?">` placeholder: needs expansion lookup.
- 32 within-line `<ab n="…">` non-standard expansion matches — compass directions and Latin words ("North" ×4, "East" ×4, "centum" ×4, etc.).
- 2,078 within-line adjacent `</ab> <ab>` pairs for verification.
- 5 `{{old → new || …}}` correction records present.

### Usage

```
cd mdissues/markup_fix
python 08_markup_fix.py                        # uses csl-orig/v02/md/md.txt by default
python 08_markup_fix.py IN.txt OUT.txt         # custom paths
```

Outputs: `md_fixed.txt`, `markup_fix_changes.txt`, `markup_audit.txt`.

### Summary

12 paired tag types. <cl> and <per> are MD-specific.

### Severity

`minor`
