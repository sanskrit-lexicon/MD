
Analysis of md verbs and upasargas, revised
This work was done in a temporary subdirectory (temp_verbs) of csl-orig/v02/md/.

The shell script redo.sh reruns python programs, from mwverb.py to preverb1.py.


* mwverbs
python mwverb.py mw ../../mw/mw.txt mwverbs.txt
#copy from v02/mw/temp_verbs
#cp ../../mw/temp_verbs/verb.txt mwverbs.txt
each line has 5 fields, colon delimited:
 k1
 L
 verb category: genuinroot, root, pre,gati,nom
 cps:  classes and/or padas. comma-separated string
 parse:  for pre and gati,  shows x+y+z  parsing prefixes and root

* mwverbs1.txt
python mwverbs1.py mwverbs.txt mwverbs1.txt
Merge records with same key (headword)
Also  use 'verb' for categories root, genuineroot, nom
and 'preverb' for categories pre, gati.
Format:
 5 fields, ':' separated
 1. mw headword
 2. MW Lnums, '&' separated
 3. category (verb or preverb)
 4. class-pada list, ',' separated
 5. parse. Empty for 'verb' category. For preverb category U1+U2+...+root

* prepare roman
python roman.py transcoder/slp1_roman.xml roman.txt
This gets a starting list of upper-case IAST letters used in transliteration
of verbs
* md_verb_filter.

python md_verb_filter.py ../md.txt   md_verb_exclude.txt md_verb_filter.txt

Verbs entries in MD are recognized by having an upper-case transliteration
following the Devanagari headword.
In terms of the Cologne digitization, this is found by the pattern:
u'¦[ABCDGHIJKPTUÑĀĪŚŪ̃ḌḤḶḸṂṄṆṚṜṢṬSNMRVLYEO‡-]+[, ]'
The ‡ character represents a sandhi-joining symbol, for just a few verbs,
such as slp1 'svad' (SU‡AD).

992  entries are thus identified as verbs, out of 20748 entries (4.8%).

The exclusion file is empty for MD (no false positives to exclude thus far).

Format of file md_verb_filter.txt:
;; Case 0001: L=159, k1=akz, k2=akz, code=V


* md_verb_filter_map
python md_verb_filter_map.py md_verb_filter.txt mwverbs1.txt md_verb_filter_map.txt

Get correspondences between md verb spellings and
 - md verb spellings
 - mw verb spellings

Format of md_verb_filter_map.txt:
 Adds a field mw=xxx to each line of md_verb_filter.txt,
indicating the MW root believed to correspond to the MD root.
For example, aMSay in MD is believed to correspond to aMS in MW.
;; Case 0001: L=21, k1=aMh, k2=aMh, code=V, mw=aMh
;; Case 0001: L=13, k1=aMSay, k2=aMSay, code=N, mw=aMS

In 6 cases, no correspondence could be found. These use 'mw=?'. 
;; Case 0011: L=1851, k1=ap, k2=ap, code=V, mw=?
;; Case 0125: L=6464, k1=kru, k2=[kru, code=V, mw=?
;; Case 0162: L=6691, k1=Kar, k2=[Kar, code=V, mw=?
;; Case 0573: L=14347, k1=mUr, k2=[mUr, code=V, mw=?
;; Case 0606: L=14762, k1=yah, k2=[yah, code=V, mw=?
;; Case 0964: L=20502, k1=hAs, k2=hAs, code=V, mw=?



* md_preverb0.txt
python preverb0.py ../md.txt md_verb_filter_map.txt md_upasargas.txt md_preverb0.txt > temp_upadump1.txt

Note: print statements in 'write' function provide debugging information,
and are thus present in temp_upadump1 file.

For each verb entry of md.txt, examine the text.
Search for all Devanagari text, and identify the text that represents
one (or more) upasargas.  Determine what is an upasarga by using
md_upasargas.txt, which lists all distinct upasargas identified for
verbs of cae dictionary, along with additional compound upasargas identified
by visual comparison using the temp_upadump1 file.

For each entry, list the upasargas found therein.
The result will be used to make mw correspondences by preverb1 program .

Sample of first few lines of md_preverb0.txt
;; Case 0001: L=159, k1=akz, #upasargas=1, upasargas=nis
;; Case 0002: L=360, k1=aNg, #upasargas=0, upasargas=
;; Case 0003: L=403, k1=ac, #upasargas=10, upasargas=anu,ava,A,ud,vyud,samud,ni,pari,vi,sam

* md_preverb1.txt
python preverb1.py slp1 md_preverb0.txt md_verb_filter_map.txt mwverbs1.txt md_preverb1.txt
python preverb1.py deva md_preverb0.txt md_verb_filter_map.txt mwverbs1.txt md_preverb1_deva.txt

This program first merges the information from md_preverb0 (the upasargas) with
the mw root mapping information from md_verb_filter_map.
Then, for each upasarga for a given root, it further joins the upasarga
with the MW root spelling to get a spelling for the implied prefixed root,
and identifies whether this prefixed root spelling occurs as an MW headword.

The number of upasargas found is reported on a line for the verb entry.
The first MD verb entry has no upasargas:
;; Case 0001: L=21, k1=aMh, k2=aMh, code=V, #upasargas=0, mw=aMh (same)

The tenth MD verb entry has 8 upasargas:
```
;; Case 0010: L=1153, k1=an, k2=an, code=V, #upasargas=8 (6/2), mw=an (same)
01        apa         an                 apAn                 apAn yes apa+an
02     aByapa         an              aByapAn              aByapAn yes aBi+apa+an
03        pra         an                 prAn                 prAn yes pra+an
04     anupra         an              anuprAn              anuprAR yes anu+pra+an
05        aBi         an                aByan                aByan no 
06         vi         an                 vyan                 vyan yes vi+an
07        sam         an                saman                saman yes sam+an
08     anusam         an             anusaman             anusaman no 
```
 
In this example, 6 prefixed forms were found as MW verbs (apAn, etc.);
while 2 prefixed forms (aByan and anusaman) were not found as MW verbs.

Altogether, there are currently 3050 prefixed forms matched to MW verbs ('yes' cases), 
and 380 'no' cases. 

Presumably, both Monier-Williams and Macdonell derive their upasarga forms from examination of
some corpus of Sanskrit Literature.   I suspect that the 380 'no' cases are mostly due to
differences between the MW corpus and the MD corpus. For instance, probably some instance
of the prefixed verb 'aByan' occurs in one of the texts examined by MD, but does not occur
in any of the texts examined by MW.



