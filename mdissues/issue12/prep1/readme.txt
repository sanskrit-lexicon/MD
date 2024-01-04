work on issue 12 for MD dictionary.
MD subheadwords

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue12/prep1
ls
--------------------------------------------------------------
temp_md_0.txt
 Original copy from csl-orig at 09-12-2023
cp /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt ../temp_md_0.txt
--------------------------------------------------------------
classify entries as verb, substantative, other?
The /verbs01/ directory (top-level of this MD repository)
  will be useful for prefixed verbs
Use md_verb_filter.txt to identify the verbal entries
cp ../../../verbs01/md_verb_filter.txt temp_verb_filter.txt

--------------------------------------------------------------
# 1. add classification line '<e>X' to metalines, where
 X = V  verb
 X = S  substantive
 X = X  other
# 2. prep1a.txt summarizes all 'substantive compounds'

python prep1a.py ../temp_md_0.txt verb_filter.txt temp_md_1a.txt prep1a.txt
83040 lines read from ../temp_md_0.txt
992 lines read from verb_filter.txt
992 read from verb_filter.txt
992 metalines marked as V
230 metalines marked as V1  Verbs ending kf, BU, etc.
18759 metalines marked as S
768 metalines marked as X
83040 lines written to temp_md_1a.txt
7639 lines written to prep1a.txt
32301 count of suffixes
--------------------------------------------------------------
--------------------------------------------------------------
temp_md_0a.txt  So {@-X@} has only one suffix.
Changes like:
 {@-prabhā, -bhās, -rocis, -‿aṃśu, -‿ābhā,@} ->
 {@-prabhā,@} {@-bhās,@} {@-rocis,@} {@-‿aṃśu,@} {@-‿ābhā,@}
 
python make_md_0a.py ../temp_md_0.txt ../temp_md_0a.txt
83040 lines read from ../temp_md_0.txt
339 lines changed
83040 lines written to ../temp_md_0a.txt

--------------------------------------------------------------
#rerun prep1a with md_0a

python prep1a.py ../temp_md_0a.txt verb_filter.txt temp_md_1a_1.txt prep1a_1.txt
32717 count of suffixes  (compare to 32301 above)
--------------------------------------------------------------
The compound suffixes are in IAST, with some additional characters
Transcode to SLP1.

python prep1a_slp1.py prep1a_1.txt prep1a_1_slp1.txt
7642 lines read from prep1a_1.txt
7642 recs (32717 lines) written to prep1a_1_slp1.txt

--------------------------------------------------------------
cp -r /c/xampp/htdocs/funderburkjim/ScharfSandhi/pythonv4/ ../sandhi
# remove unneeded parts

# sandhi join of pfx and sfx for each compound
# drop accents before joining
python prep1a_cpd.py prep1a_1_slp1.txt prep1a_cpd.txt
32717 recs (32717 lines) written to prep1a_cpd.txt
--------------------------------------------------------------
Many prefixes need to be modified.
Compare cpds to mw headwords as an aid to this.
Get mw headwords from mwhw.txt
cp /c/xampp/htdocs/cologne/mw/pywork/mwhw.txt temp_mwhw.txt

--------------------------------------------------------------
python prep1a_cpd_mw.py prep1a_cpd.txt temp_mwhw.txt prep1a_cpd_mw.txt 
mark_mw: 8300 cpds in mw, 24417 cpds not in mw
# with accents mark_mw: 8126 cpds in mw, 24591 cpds not in mw
--------------------------------------------------------------
# A status summary, like prep1a_1.txt
python prep1a_status.py prep1a_cpd_mw.txt prep1a_status.txt
7642 recs (7642 lines) written to prep1a_status.txt
1983 complete out of 7642

# 1983 matches for ">\([0-9]+\)/\1<" in buffer: prep1a_status.txt
**************************************************************
cp prep1a_1.txt prep1a_1_edit.txt  # changes to pfx

redo1a.sh

python prep1a_slp1.py prep1a_1_edit.txt prep1a_1_slp1.txt
python prep1a_cpd.py prep1a_1_slp1.txt prep1a_cpd.txt
python prep1a_cpd_mw.py prep1a_cpd.txt temp_mwhw.txt prep1a_cpd_mw.txt 
python prep1a_status.py prep1a_cpd_mw.txt prep1a_edit_status.txt

prep1a_edit_status.txt is like prep1a_1_edit.txt, but has <stat>

sh redo1a.sh
**************************************************************
re-arrange so prep1a_edit_status.txt takes the place of prep1a_1_edit.txt.
Then, we can iteratively do:
a. Make changes to prep1a_edit_status.txt (change to <pfx>)
b. sh redo1b.sh
  This also regenerates prep1a_edit_status.txt by
  updating the <stat> item of each record.
c. Revert prep1a_edit_status.txt
d. Goto 'a.'

-- redo1b.sh
# save a unique copy, just in case
dt=`date +%F-%H-%M-%S`
file='prep1a_edit_status.txt'
filecpy="temp_edit_status/prep1a_edit_status_$dt.txt"
cmd="cp $file $filecpy"
echo $cmd
$cmd

python prep1a_slp1.py prep1a_edit_status.txt prep1a_1_slp1_b.txt
python prep1a_cpd.py prep1a_1_slp1_b.txt prep1a_cpd_b.txt
# last argument here is for Emacs org-mode review. Prepends '* ' for
# new entries.
python prep1a_cpd_mw.py prep1a_cpd_b.txt temp_mwhw.txt prep1a_cpd_mw_b.txt prep1a_cpd_mw_b.org
# write over prep1a_edit_status
python prep1a_status.py prep1a_cpd_mw_b.txt prep1a_edit_status.txt



--------------------------------------------------------------
prep1a_cpd.py  introduce cpd_exceptions, to
  override the sandhi construction of compounds.
  Start with one item:
    'asTan-vat' : 'asTanvat', # asTavat per sandhi

--------------------------------------------------------------
At 12% of prep1a_edit_status.txt manual review L=3914 is done,
  L=3920 is first not manually reviewed.
cp prep1a_edit_status.txt prep1a_edit_status_v0.txt
 # at this point:
  mark_mw: 9334 cpds in mw, 23384 cpds not in mw  
  7642 recs (7642 lines) written to prep1a_edit_status.txt
  2145 complete out of 7642
  1198 partially done
  
--------------------------------------------------------------
Try to 'speed' up the setting of pfx in remaining, by
 generating 'pfx' from md.txt

python prep1a_k2.py temp_md_1a.txt prep1a_k2.txt
 L,k1,k2a,k2b

<L>3920<pc>043-1<k1>Avedaka<k2>Avedaka<e>S
{#Avedaka#}¦ ā-ved-aka, <lex>a.</lex>
<L>3920<k1>Avedaka><k2a>ā-ved-aka<k2b>A-ved-aka
 k2a is iast from md.txt
 k2b is slp1 form.
Only for <e>S metaline

-------------------------------------------------------
Generate pfx
python prep1a_pfx.py prep1a_edit_status_v0.txt prep1a_k2.txt prep1a_edit_status_v1.txt
7639 lines read from prep1a_k2.txt
7639 K2 records from prep1a_k2.txt
7642 lines read from prep1a_edit_status_v0.txt
update_pfx: L=4115,idam not in K2 records
update_pfx: L=8145,jYA not in K2 records
update_pfx: L=8313,tatas not in K2 records
7642 recs (7642 lines) written to prep1a_edit_status_v1.txt

cp prep1a_edit_status_v1.txt prep1a_edit_status.txt
sh redo1b.sh
mark_mw: 19847 cpds in mw, 12871 cpds not in mw
2714 complete out of 7642
1978 partially done

Comparison is good:
          before after   diff
    mw-Y:   9334 19931  10597 compounds 
    mw-N:  23384 12781  10597 fewer compounds
complete:   2145  2739    594  entries
 partial:   1198  1971    773  entries
 
--------------------------------------------------------------
# further iteration on prep1a_edit_status.txt

"stat>0/[0-9][0-9]"  manually adjust these (about 130)
mark_mw: 21766 cpds in mw, 10952 cpds not in mw
2808 complete out of 7642
2067 partially done

--------------------------------------------------------------
Observed errors in the joining of pfx and sfx in prep1a_cpd.

Some compounds are not in MW, but have been found in PW.
temp_cpd_notmw.txt  is a list of 7353 compounds not found in MW.
Are these PW headwords?
cp /c/xampp/htdocs/cologne/pw/pywork/pwhw.txt temp_pwhw.txt

python hw_check.py temp_cpd_notmw.txt temp_pwhw.txt temp_pwhw_check.txt
7353 lines read from temp_cpd_notmw.txt
135764 lines read from temp_pwhw.txt
131900 keys from temp_pwhw.txt
571 lines written to temp_pwhw_check.txt

# insert these words into the 'known_compounds' set in prep1a_cpd_mw.py

# counts from previous redo1b.sh
mark_mw: 25365 cpds in mw, 7353 cpds not in mw
4001 complete out of 7642
2422 partially done

# counts with these 500+ additional known words from pw
sh redo1b.sh
mark_mw: 25936 cpds in mw, 6782 cpds not in mw
4193 complete out of 7642
2309 partially done

--------------------------------------------------------------
continue analysis of the 6782 cpds not in mw (prep1a_cpd_mw_b.txt).
In prep1a_edit_status.txt,
  mark sfxes with '*' when they are Not compound indicators.
  e.g. in agraRI, '*s'  since this is telling the form of nom. sg.

--------------------------------------------------------------
NOTES:
---
<L>3167<pc>034-3<k1>asaScat
 {@-anti@} -> {@-antī@}
 NOTE: {@-antī@} and {@-át-ī@} are not cpds, but feminine forms
---
<L>338<pc>003-3<k1>aGnya<k2>aGnya<e>S
 {@-yá@}  is Alternate form (accent), not compound
---
<L>972<pc>009-3<k1>aDa
 {@-adha-adha,@} -> {@adha-adha,@}   NOT A compound. Change later
---
<L>983<pc>009-3<k1>aDarAt
{#aDarAt#}¦ adharā́t, <lex>ad.</lex> below; {@-āt,@}
 {@-āt,@} -> {@-tāt,@}  (PRINT-CHANGE cf. MW)
---
<L>1883<pc>019-2<k1>apatita
 {@-anyo'nya-tyāgin,@} -> {@-anyonya-tyāgin,@}  PRINT CHANGE
---
<L>997<k1>aDaHSaya
 {@-śayyā,@} {@-āsanin,@}  : H3 aDaHSayyAsanin (pw)
---
new entry from 1463:
<L>1463.1<pc>014-1<k1>anArudDa<k2>anArudDa<e>S
{#anArudDa#}¦ an-ā-ruddha, <ab>pp.</ab> unlimited.
<LEND>


--------------------------------------------------------------
--------------------------------------------------------------
prep1a_k2_edit.txt
prep1a_k2.txt has some errors, due to different format.
cp prep1a_k2.txt prep1a_k2_edit.txt
Manually change  prep1a_k2_edit.txt
 88 lines changed.
 Format:  k2a is iast, k2b is slp1.  Note 
 <L>277<k1>agniBu<k2a>agni-bhu<k2b>agni-Bu
 <L>297<k1>agra<k2a>ág-ra<k2b>a/g-ra
 Also, the 'vowel-sandhi markers' are present
 <L>398<k1>aNgulyagra<k2a>aṅguli‿agrá<k2b>aNguli‿agra/
 
--------------------------------------------------------------
prep1a_k2_edit.txt has 7639 lines.
prep1a_edit_status.txt has 7642 lines.
Resolve the differences.
Comparing just on <L>a<k1>b shows the differences:
1165d1164
< <L>4115<k1>idam
2543d2541
< <L>8145<k1>jYA
2589d2586
< <L>8313<k1>tatas

add 3 lines to prep1a_k2_edit.txt:
<L>4115<k1>idam<k2a>i-d-ám<k2b>i-d-a/m
<L>8145<k1>jYA<k2a>jñĀ<k2b>jYA
<L>8313<k1>tatas<k2a>tá-tas<k2b>ta/-tas

These additions resolve the difference.
--------------------------------------------------------------
MD additions and corrections.
First: <L>20700<pc>383-1<k1>aDyUQa
Last:  <L>20748<pc>384-3<k1>sadyaHprakzAlaka<k2>sadyaHprakzAlaka<e>S

49 <L>-entries
--------------------------------------------------------------
difference between ../temp_md_0a.txt and temp_md_1a_1.txt
temp_md_1a_1.txt is constructed by:
python prep1a.py ../temp_md_0a.txt verb_filter.txt temp_md_1a_1.txt prep1a_1.txt
which adds <e>X, <e>S, <e>V, or <e>V1 markup to each metaline.
By removing this markup, we restore ../temp_md_0a.txt.

--------------------------------------------------------------
cp ../temp_md_0a.txt ../temp_md_0b.txt
Manual corrections to ../temp_md_0b.txt
../change_notes_0b.txt  Contains note on these changes.

--------------------------------------------------------------
prep1b_1.txt  temp_md_1b_1.txt
 generate from ../temp_md_0b.txt
 Also, generate prep1b_1.txt.  However
   prep1b_1.txt is superceded by prep1a_edit_status.txt
   
python prep1a.py ../temp_md_0b.txt verb_filter.txt temp_md_1b_1.txt prep1b_1.txt
83044 lines read from ../temp_md_0b.txt
992 lines read from verb_filter.txt
992 read from verb_filter.txt
992 metalines marked as V
230 metalines marked as V1
18760 metalines marked as S
768 metalines marked as X
83044 lines written to temp_md_1b_1.txt
7642 lines written to prep1b_1.txt
32719 count of suffixes

--------------------------------------------------------------
# check consistency of temp_md_1b_1.txt and prep1a_edit_status.txt
python prep1a_check_status.py temp_md_1b_1.txt prep1a_edit_status.txt 
Revise temp_md_0b.txt and prep1a_edit_status.txt.
Revise prep1a_edit_status.txt.
Revise temp_md_0b.txt and change_notes_0b.txt
Remake temp_md_1b_1.txt
python prep1a.py ../temp_md_0b.txt verb_filter.txt temp_md_1b_1.txt prep1b_1.txt

Iterate. Final output shows as
83044 lines read from temp_md_1b_1.txt
7642 lines read from prep1a_edit_status.txt
ndiff2 =  0
0 recs not accounted for

--------------------------------------------------------------
# rerun
sh redo1b.sh

mark_mw: 26433 cpds in mw, 6288 cpds not in mw
32721 recs (32721 lines) written to prep1a_cpd_mw_b.txt
32721 recs (40363 lines) written to prep1a_cpd_mw_b.org
32721 lines read from prep1a_cpd_mw_b.txt
32721 records at init_prep1a_cpd_mw
7642 groups
7642 recs (7642 lines) written to prep1a_edit_status.txt
4501 complete out of 7642
2198 partially done


--------------------------------------------------------------
I think we will need the 'k2' for all headwords AND sub-headwords
Currently, temp_md_1b_1.txt has k2 == k1 always.
prep1a_k2_edit.txt has k2a (iast) and k2b (slp1), but
 just for those L which are compounds.

Let's do the similar operation for ALL entries.
Since some editing is required, let's include the editing
previously done (in prep1a_k2_edit.txt)

python prep1a_k2_all.py temp_md_1b_1.txt prep1a_k2_all.txt
20750 meta k2s found
60 of these have no k2
20750 lines written to prep1a_k2_all.txt

Provide an alternate method (not requiring a comma):
0 of these have no k2


--------------------------------------------------------------
prep1a_k2_all does SOME editing of k2.
Check consistency with prep1a_k2_edit.txt

---
python prep1a_k2_all_check.py prep1a_k2_all.txt prep1a_k2_edit.txt

20750 lines read from prep1a_k2_all.txt
7642 lines read from prep1a_k2_edit.txt
1. error in _edit - missing iast
prep1a_k2_edit: <L>1844<k1>anvavekzA<k2a><k2b>anu‿avekz-A
prep1a_k2_all : <L>1844<k1>anvavekzA<k2a>anu‿avekṣ-ā<k2b>anu‿avekz-A
2. error in _edit: space in k2a
prep1a_k2_edit: <L>3418<k1>Agama<k2a>ā́-gama <k2b>A/-gama
prep1a_k2_all : <L>3418<k1>Agama<k2a>ā́-gama<k2b>A/-gama
3. error in _edit. '<' at end of k2b
prep1a_k2_edit: <L>7350<k1>caYcu<k2a>cañc-u<k2b>caYc-u<
prep1a_k2_all : <L>7350<k1>caYcu<k2a>cañc-u<k2b>caYc-u

3 consistency problems

Correct prep1a_k2_edit.txt, and rerun
python prep1a_k2_all_check.py prep1a_k2_all.txt prep1a_k2_edit.txt
0 consistency problems

Note: We will have no further need for prep1a_k2_edit.txt.

--------------------------------------------------------------
New version of md.txt: temp_md_1b_2.txt from temp_md_1b_1.txt,
 replacing <k2>X< with <k2>Y for a given L,
 where Y is from prep1a_k2_all.txt for that L

python prep1a_k2_revise.py temp_md_1b_1.txt prep1a_k2_all.txt temp_md_1b_2.txt

--------------------------------------------------------------
# Split md.txt entries into sub-headwords (for the compounds)
python prep1a_subhw.py temp_md_1b_2.txt prep1a_cpd_mw_b.txt temp_md_1b_subhw.txt

# Do the inverse,
python prep1a_subhw_inverse.py temp_md_1b_subhw.txt temp.txt
diff temp_md_1b_2.txt temp.txt | wc -l
# 0 differences expected

--------------------------------------------------------------

--------------------------------------------------------------
--------------------------------------------------------------

--------------------------------------------------------------
--------------------------------------------------------------

--------------------------------------------------------------
--------------------------------------------------------------

--------------------------------------------------------------
--------------------------------------------------------------

--------------------------------------------------------------
--------------------------------------------------------------

--------------------------------------------------------------
--------------------------------------------------------------
