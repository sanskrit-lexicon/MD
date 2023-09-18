abbrev1/readme.txt

-----------------------------------------------------------------------
Abbreviations with spaces:
e. g.	= for example.
i. e.	= that is.
q. v.	= which see.
s. v.	= sub voce.
v. r.	= various reading.
------
temp_md_1a.txt
e.g  -> e. g.  (2)
i.e. -> i. e.  (9)
q.v. -> q. v.  (0)
s.v  -> s. v.  (2)
v.r. -> v. r.  (0)
../change_md_1a.txt
python ../updateByLine.py ../temp_md_0.txt change_md_1a.txt temp_md_1a.txt
15 change transactions from ../change_md_1a.txt
-----------------------------------------------------------------------
temp_md_1b.txt  Apply ab markup

python markup.py temp_md_1a.txt ../abbrev0/abbrev0.txt temp_md_1b.txt

python ab_count.py temp_md_1b.txt ../abbrev0/abbrev0.txt ab_count_1b.txt

------
abbrev1.txt  some revisions to ../abbrev0/abbrev0.txt
&amp;  md.xml  changes '&' to '&amp;'.
 The display program needs to have a tooltip for '&amp;'
&amp;c.  also needs tooltip (&c.)
python ../
------
‡ should this be marked as an abbreviation ?
{#anUtTita#}¦anu‡ut-thita, {%<ab>pp.</ab>%} <ab>√</ab> sthā.
tip = ? vowel-sandhi undone ?
This displays as: 'anu_ut-thita'.
The print shows this as a curve underneath.
make_xml.py changed to display this symbol.
0x203F Undertie (general punctuation, Basic Multilingual Plane
-----

python ab_count.py temp_md_1b.txt abbrev1.txt ab_count_1b.txt

python ../diff_to_changes_dict.py temp_md_1a.txt temp_md_1b.txt temp_change_1b.txt
62928 changes written to temp_change_1b.txt

-------------------------
09-14-2023
temp_md_1c.txt
Special abbreviations: + ± & &c. √
ab tags added to these when preceded by a 'space'.
However, there are instances remaining unmarked.
-----
9 matches for "[^>][+]"
 These are all changed.
 Questionable:  Such as
<L>11729<pc>164-3<k1>purauzRih<k2>purauzRih
{%a metre%} (¤12 <ab>+</ab> 8 <ab>+</ab> 8¤ {%syllables%})

-----
81 matches for "[^>][±]"
  70 matches for "([±]"
  11 matches for "^[±]"
  
-----
53 matches for "[^>]&"
  8 matches for "{%&c\.%}
 14 matches for "{%&%}"
  8 matches for "{%&c\."
 20 matches for "{%& "
  3 matches for "^&"
  (+ 8 14 8 20 3) = 53
  
-----
894 matches in 891 lines for "[^>][√]"
  100 matches for "^√"
  488 matches for "\[√"
  306 matches for "(√"
(+ 100 488 306) 894

-----
1 match for "[^>][&+±&√]"
  This is the comment at line 18.
-----
 python ../diff_to_changes_dict.py temp_md_1b.txt temp_md_1c.txt change_1c.txt

-----
python ab_count.py temp_md_1c.txt abbrev1.txt ab_count_1c.txt
178 abbreviations read from abbrev1.txt
178 cases written to ab_count_1c.txt

diff ab_count_1b.txt ab_count_1c.txt
171,173c171,173
< + :: 98 :: with; also.
< ± :: 137 :: with or without.
< & :: 188 :: and.
---
> + :: 107 :: with; also.
> ± :: 218 :: with or without.
> & :: 225 :: and.
175c175
< &c. :: 12 :: et cetera, and so forth.
---
> &c. :: 28 :: et cetera, and so forth.
178c178
< √ :: 909 :: root.
---
> √ :: 1804 :: root.

-----------------------------------------
Some Ā  (atmanepada)  don't have period
80 matches for "Ā\b[^.]"
  68 matches for "Ā,"   (The comma is typo)
    Change these to <ab>Ā.</ab>
   4 manual change
   8 do not require change (not atmanepada)
-----
cp temp_md_1c.txt ../temp_md_1.txt
cd ../
sh redo_dev.sh 1


------------------------------------------------
disambiguation of P.
cp temp_md_1c.txt temp_md_1d.txt
Modify temp_md_1d.txt manually
 Italic 'P.' is Purāṇa.
 Non-italic is Parasmaipada.
 64 matches for "{%<ab>P.</ab>%}"
 Treat as 'local abbreviation':
 {%<ab>P.</ab>%} -> {%<ab n="Purāṇa">P.</ab>%}
-----
1655 matches in 1577 lines for "<ab>P\.</ab>"
---
delete-matching lines: {%<ab>den.</ab>%} <ab>P.</ab>
  248
---
{%den,%} -> {%<ab>den.</ab>%}   (3)
---
I.<ab>P.</ab>
------------------------------
A. D. additional abbreviation 
------------------------------
 n="Purāṇa">P.</ab>%}
-----
1655 matches in 1577 lines for "<ab>P\.</ab>"
---
delete-matching lines: {%<ab>den.</ab>%} <ab>P.</ab>
  248
---
{%den,%} -> {%<ab>den.</ab>%}   (3)
---
I.<ab>P.</ab>
124 matches  for "<ab n="Purāṇa""
------------------------------
A. D. additional abbreviation
------------------------------
python ../diff_to_changes_dict.py temp_md_1c.txt temp_md_1d.txt change_1d.txt
232 changes written to change_1d.txt

------------------------------
cp temp_md_1d.txt ../temp_md_1.txt

------------------------------
TODO <hom>
<ab>√</ab> ¤1.¤ pat, <ab>P.</ab>
  <hom>1.</hom> pat
------------------------------

------------------------------------------------
------------------------------------------------
disambiguation of N.

acc. to tooltips:
N.	= name; when alone = name of a man or of a woman.
ɴ.	= noun.
This ɴ. is not present (it is Andhrabharati's choice).
How to distinguish ɴ. from N.
<ab n="noun">ɴ.</ab>

cp temp_md_1d.txt temp_md_1e.txt
4635 matches  "<ab>N\.</ab>"
See akftabudDi  .  abst. N.  (N. is italic and small)

Two cases found not in italics - corrected
<L>2102<pc>022-1<k1>aprAjYa
<L>19989<pc>366-3<k1>sTeman
Now, all '<ab>abst.</ab> <ab>N.</ab>' are in italic markup {%X%}.

Temporary? markup
OLD: <ab>abst.</ab> <ab>N.</ab>
NEW: <ab>abst. N.</ab>
Add to abbrev1:
abst. N.	= abstract noun.

global change in temp_md_1e.txt:
<ab>abst.</ab> <ab>N.</ab> → <ab>abst. N.</ab>

update to mdab_input.txt
cd ../
python make_mdab_input.py abbrev1.txt mdab_input_1.txt
#180 abbreviations read from abbrev1.txt
#180 lines written to mdab_input_1.txt

cp abbrev1/mdab_input_1.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt
cd abbrev1

cp temp_md_1e.txt ../temp_md_1.txt
cd ../
sh redo_dev.sh 1
cd abbrev1

python ab_count.py temp_md_1e.txt abbrev1.txt ab_count_1e.txt

-------
python ../diff_to_changes_dict.py temp_md_1d.txt temp_md_1e.txt change_1e.txt
-------
Are there any other N.  = noun. ?
Note <ab>N.</ab> as 'Name' can also be italic. But a normal 'N.' e.g. aMSa.
4333 matches in 3982 lines for "<ab>N\.</ab>
2510 matches in 2430 lines for "<ab>N.</ab> of

(1710 remain)
 236 matches for "<ab>f.</ab> <ab>N.</ab>
 892 matches for "<ab>m.</ab> <ab>N.</ab>
  22 matches for "<ab>n.</ab> <ab>N.</ab>"
 (+ 236 892 22) = 1150
(668 remain)

 58 matches for "<ab>N.</ab>%} {%of
   change to <ab>N.</ab> of
<ab>abst.</ab> %}

38 matches for "<ab>vbl.</ab> <ab>N.</ab>"
 change to "<ab>vbl. N.</ab>", and add to abbrev1.txt

print change:
<L>1775<pc>018-1<k1>antarbAzpa
old: <ab>abs.</ab> <ab>N.</ab>
new: <ab>abst. N.</ab>
;  -tva
<L>2814<pc>030-1<k1>avayava
{%<ab>N.</ab>%} whole -> {%<ab n="noun.">N.</ab>%} whole
;
<L>19971<pc>366-1<k1>sTita
old:
{%<ab>N.</ab> %}
{%in <ab>app.</ab>%}
new:
{%<ab n="noun.">N.</ab> %}
{%in <ab>app.</ab>%}
----
old: <ab>a.</ab> or <ab>N.</ab>
new: <ab>a.</ab> or <ab n="noun.">N.</ab>
4 cases
----

python prepare_lnums.py temp_md_1e.txt temp_N_work.txt temp_md_1e_lnums.txt prepare_lnums_1e.org

N_  -> N
<ab>N=.</ab> -> <ab n="noun.">N.</ab>

N.E.	= Northeast.
N.W.	= Northwest.
RV.²	= Rig-veda (² = ?)

^= -> <ab>=</ab>  75
'<ab>RV.</ab> ²' -> '<ab>RV.²</ab>'  22
'<ab>RV.</ab>¹'  -> '<ab>RV.¹</ab>' 402

39 matches for 'n="noun.'
1198 matches in 995 lines for "--"
--------------------------------------------------------------
09-18-2023  Finish this round of work on abbreviation markup
temp_md_1e_lnums.txt adjusted manually

python ../diff_to_changes_dict.py temp_md_1e.txt temp_md_1e_lnums.txt change_1e_lnums.txt

cp temp_md_1e_lnums.txt ../temp_md_1.txt


python ab_count.py ../temp_md_1.txt abbrev1.txt ab_count_1.txt

python ab_count_local.py ../temp_md_1.txt ab_count_local_1.txt

python ../make_mdab_input.py abbrev1.txt mdab_input_1.txt
185 abbreviations read from abbrev1.txt
185 lines written to mdab_input_1.txt


cp mdab_input_1.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt

cd ../
sh redo_dev.sh 1
