Note - I am aware that this is incomplete in various ways.
From this form (when corrected), I think a revised 'mdnew.txt' can be made.
The task as I see it, is to 'correct' this file.

## major conventions
For this discussion, let
* mdold = previous cdsl version of md.txt.
* mdwork = mw_1b_subhw.txt.
* mdnew = a new version to be created from mdwork; it will replace mdold at cdsl

## formal differences between mdold and mdwork
* metaline has new k2: This is slp1 derived from the iast of mdold's dataline.
* metaline has new field. : `<e>value`, where value is
  * V : normal verb
  * V1 : verbs with kf, etc.
  * S : substantive (from a 'lex' tag)
  * X : none of the above.
* the dataline of mdold is split based on `{@-` in 'S' entries.
  * 7642 metalines with sub-headwords in mdwork.
  ^ No representation in mdwork for verbs. subheadwords for verbs will be handled in future.
* Each `{@-X,@}` (or `{@-X@}`) of mdold is represented by 2 lines of mdwork:
  * `;; subhw ....` will be used in mdnew to generate the metaline of the subhw, and the `{#slp1#}¦ iast` start of the dataline for the subhw entry
  * `<H2> rest of the dataline for the subhw entry in mdnew

## the `;; subhw` line conventions
  `;; subhw N:X:pfx + sfx -> cpd`

* N: sequential numbering of the subhw in this entry
* X: value Y meaning cpd 'validated' or value N not validated. value Y means
  * cpd is an MW headword, or
  * cpd is a PWK headword (or a comment in a PW headword)
  * Value 'N' will contain 'new' md headwords in mdnew.
* cpd is created by 'combining' pfx and sfx.  All these are in iast.
  * in mdnew, a new subhw metaline k2 will be the slp1 version of cpd
  * the new subhw metaline k1 will be converted from the new metaline k2
* the cpd should have only '-' along with iast characters.
  * some 'known-unknowns' are represented in cpd with '*' or '?'
  * the current 'unknown-unknowns' are not formally recognized in mdwork!
  
## the subhw dataline in mdwork
 All of these currently start as `<H2>`.  After revision of mdwork, some of
 these will be marked as `<H3>`. The form of this H2, H3 markup is the
 same as for MW dictionary. But the meaning in MD is different, but
 currently fuzzy.
 In current mdwork, H2 means that the pfx comes from k2 (of parent).
 and H3 means the pfx comes from the previous H2 subhw.
 H3's are currently unmarked, but a small number have an '*'
 Some suffixes have a 'space' (`;; subhw 9:N:antar + *ṃ gam -> antar-*ṃ gam?`)
 
