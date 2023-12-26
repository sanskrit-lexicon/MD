md/mdissues/issue11/abv1

Andhrabharati's version 1 of MD dictionary.

# github issue
https://github.com/sanskrit-lexicon/MD/issues/11

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue11/abv1

# 12-20-2023
# ../temp_md_ab_1.txt
from AB's md_AB_v1.zip.  (AB uploaded this on Sep 19, 2023).
From csl-orig/v02/md/md.txt  the latest revision is Sep 18, 2023.

# temp_md_ab_2.txt
There is also a md_AB_v2.zip  which AB says is not complete, but
has some preliminary 'althws'- type markup for k2.
May work on this later.

# temp_md_1.txt  l
https://github.com/sanskrit-lexicon/csl-orig/commit/258eefdfa059239b571715b3e502d42ac28823a4
  The commit of Sep 18, 2023
  
cd /c/xampp/htdocs/cologne/csl-orig/v02/md/
git show 258eefdfa:v02/md/md.txt > temp_md_258eefdfa.txt
mv temp_md_258eefdfa.txt /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue11/abv1/temp_md_1.txt
Note: temp_md_1.txt is same as ../temp_md_1.txt


wc -l temp_md_*.txt
  146636 temp_md_1.txt
   83040 temp_md_ab_1.txt
  109801 temp_md_ab_2.txt

---------------------------------------
generate displays in devab_1
Get xml error:
Opening and ending tag mismatch: pe line 176 and body, line 176, column 177

Special characters:
 🞄 01F784  The character 🞄 (Black Slightly Small Circle) is represented by the Unicode codepoint U+1F784. It is encoded in the Geometric Shapes Extended block, which belongs to the Supplementary Multilingual Plane. It was added to Unicode in version 7.0 (June, 2014).
 
AB's note: You may note that the '🞄' could be replaced by a line-break,
  to get closer (but not equal) to the cdsl version in terms of line count.

http://localhost/sanskrit-lexicon/md/mdissues/issue11/devab_1/web/webtc/indexcaller.php

# replace the circle-character with \n
# Also, correct 6 typos: <pe>X<pe> -> <pe>X</pe>
python circle_newline.py ../temp_md_ab_1.txt ../temp_md_ab_1a.txt
83040 lines read from ../temp_md_ab_1.txt
142864 lines written to ../temp_md_ab_1a.txt

Note: compare 146636 lines in temp_md_1.txt

# <pe> tag --  'person'  <pe>2</pe>  (or <pe>2.</pe>) means 2nd person
320 matches in 301 lines.

# <cl> tag -- class of verb.  <cl>X</cl>  X is a roman-numeral

Add pe to csl-pywork/v02/makotemplates/one.dtd
Add cl to one.dtd

Element zoo was declared #PCDATA but contains non text nodes
  This due to line-breaks.

# tag count
# xmltags.py: simplest approach
python xmltags.py ../temp_md_1.txt xmltags_md_1.txt
146636 lines read from ../temp_md_1.txt
48 lines written to xmltags_md_1.txt

python xmltags.py ../temp_md_ab_1a.txt xmltags_md_ab_1a.txt
142864 lines read from ../temp_md_ab_1a.txt
41 lines written to temp.txt

# xmltags1.py :
python xmltags1.py ../temp_md_1.txt xmltags1_md_1.txt
146636 lines read from ../temp_md_1.txt
6 lines written to xmltags1_md_1.txt

python xmltags1.py ../temp_md_ab_1a.txt xmltags1_md_ab_1a.txt
142864 lines read from ../temp_md_ab_1a.txt
14 lines written to xmltags1_md_ab_1a.txt

python xmltags1.py ../temp_md_ab_1.txt temp_xmltags1_md_ab_1.txt
 same as for md_ab_1a, EXCEPT for the 6 '</pe>' corrections.
-------------------------------------------
temp_md_ab_1pe.txt
 This corrects the 6 <pe>X<pe>, but retains the circle-markup.
 Note: other changes
 <cl>1.</cl> -> <cl>I.</cl>  (1)
 <ab>A.</ab>', '<lex>Ā.</lex> (1) 
 <cl>V.</cl> -> <cl>ᴠ.</cl>  class 5 (33 - to avoid conflict with <ab>V.</ab> Vedict 2470 instances
 <cl>V.</ab> is class 5 root
  Change to use Unicode U+1d20  Latin Letter Small Capital V
  <cl>ᴠ.</ab>
  
python correct_pe.py ../temp_md_ab_1.txt ../temp_md_ab_1pe.txt
40 lines changed

change made to make_xml.py for construction of displays using 1pe version.
------------------------------------------
compare metalines of ../temp_md_1.txt and ../temp_md_ab_1a.txt
python compare_metalines.py ../temp_md_1.txt ../temp_md_ab_1a.txt compare_metalines.txt

146636 lines read from ../temp_md_1.txt
142864 lines read from ../temp_md_ab_1a.txt
cdsl has 20749 entries
ab   has 20749 entries
81 differences in metalines
81 cases written to compare_metalines.txt


------------------------------------------
python alldiff.py ../temp_md_1.txt ../temp_md_ab_1a.txt alldiff.txt

Unicode Character "’" (U+2019) Right Single Quotation Mark  112 instances

instances instances
Unicode Character "ʼ" (U+02BC) Modifier Letter Apostrophe  1743 instances
------------------------------------------
Tooltips -- for ab and ??

   # for this purpose, also include tags ab and also cl, lang, lex, pe
python ab_count_extra.py ../temp_md_ab_1pe.txt mdab_input.txt ab_count_extra.txt

# latest copy of mdab_input.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt mdab_input.txt
83040 lines from ../temp_md_ab_1pe.txt
185 abbreviations read from mdab_input.txt
41 cases written to ab_count_extra.txt


python ab_count.py ../temp_md_ab_1pe.txt mdab_input.txt ab_count.txt
83040 lines from ../temp_md_ab_1pe.txt
185 abbreviations read from mdab_input.txt
122 new abbreviations
307 cases written to ab_count.txt


# copy ab_count.txt to ab_count_edit.txt,  and
# manually write tooltips at '<disp>??</disp>'

# remake new version of mdab_input.txt
python remake_mdab_input.py ab_count_edit.txt temp_mdab_input_1.txt
# and copy new version to csl-pywork
cp temp_mdab_input_1.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt

Revise basicadjust.php (csl-websanlexicon)
  Display treats cl, lang, and pe tags like <ab>.
  This is in addition to similar treatment for <lex> tags which is for all
  dictionaries.

Revise make_xml.py so bot and zoo are italicized for 'md'. 

----------------------------------------------------------
commit repositories csl-orig, csl-pywork, csl-websanlexicon

cp ../temp_md_ab_1pe.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-orig/
git pull #
git add .  # md.txt
git commit -m "MD: major revision. 
Ref: https://github.com/sanskrit-lexicon/MD/issues/11"
git push


cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue11/abv1

-----------
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh md  ../../md
sh xmlchk_xampp.sh md
# ok

# modifications to mdab_input.txt, make_xml.py and one.dtd
git pull
git add .
git commit -m "MD: major revision. 
Ref: https://github.com/sanskrit-lexicon/MD/issues/11"
git push

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
# changes to basicadjust.php and basicdisplay.php
git pull
git add .
git commit -m "MD: major revision. 
Ref: https://github.com/sanskrit-lexicon/MD/issues/11"
git push

----
Cologne install of csl-orig, csl-pywork, csl-websanlexicon
In cologne installation,  an error with one.dtd caught by xmllint:
  'pe' element appears twice.  These are removed (in two commits of csl-pywork)


----------------------------------------------------------
commit repository csl-apidev.

# first, copy latest basicadjust.php and basicdisplay.php
cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh apidev_copy.sh
cd /c/xampp/htdocs/cologne/csl-apidev
git add .
git commit -m "MD:  revised basicdisplay.php and basicadjust.php
> Ref: https://github.com/sanskrit-lexicon/MD/issues/11"
git push

-----
at Cologne, cd csl-apidev, then git pull.

----------------------------------------------------------
**********************************************************
change to roman numerals in <cl>X</cl>
Ref: https://github.com/sanskrit-lexicon/MD/issues/11#issuecomment-1868537765
Start with temp_md_ab_v1_roman.txt from this link.

temp_md_ab_v1_romana.txt  one additional change.
One change: in <L>19659<pc>358-2<k1>sfj
<ab>A.</ab> -> <lex>Ā.</lex>

Revise mdab_input.txt in csl-pywork
Ⅰ.	<id>Ⅰ.</id> <disp>First conjugation.</disp>
Ⅱ.	<id>Ⅱ.</id> <disp>Second conjugation.</disp>
Ⅲ.	<id>Ⅲ.</id> <disp>Third conjugation.</disp>
Ⅳ.	<id>Ⅳ.</id> <disp>Fourth conjugation.</disp>
Ⅴ.	<id>Ⅴ.</id> <disp>Fifth conjugation</disp>
Ⅵ.	<id>Ⅵ.</id> <disp>Sixth conjugation.</disp>
Ⅶ.	<id>Ⅶ.</id> <disp>Seventh conjugation.</disp>
Ⅷ.	<id>Ⅷ.</id> <disp>Eighth conjugation</disp>
Ⅸ.	<id>Ⅸ.</id> <disp>Ninth conjugation.</disp>
Ⅹ.	<id>Ⅹ.</id> <disp>Tenth conjugation</disp>

Install this version.
commit to repository csl-orig

cp ../temp_md_ab_v1_romana.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt

-----------
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh md  ../../md
sh xmlchk_xampp.sh md
# ok

-- csl-orig push to github
cd /c/xampp/htdocs/cologne/csl-orig/
git pull #
git add .  # md.txt
git commit -m "MD: Use Unicode Roman numerals for 'cl' tag
Ref: https://github.com/sanskrit-lexicon/MD/issues/11#issuecomment-1868537765"

git push
#  1 file changed, 750 insertions(+), 750 deletions(-)

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue11/abv1

----
Cologne install of csl-orig for new md, and regen displays.
----
---------------------------------------------------------
Regenerate list of extended ascii
python ea.py ../temp_md_ab_v1_romana.txt ea_romana.txt
# 107 extended ascii counts written to ea_romana.txt

revise csl-orig/v02/md/md-meta2.txt
 - Put in the new extended ascii, and some other minor editing.

push this change to github.
pull csl-orig at cologne, and regenerate md in csl-pywork.

---------------------------------------------------------
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue11/abv1
# push this repo to github
---------------------------------------------------------
csl-pywork  - 
Revise /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input

# regenerate local
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh md  ../../md
sh xmlchk_xampp.sh md
# ok

# push csl-pywork to github
git add .
git commit -m "MD:  revise mdab_input.txt.
> Ref: https://github.com/sanskrit-lexicon/MD/issues/11"
--------------------------------------------------------
12-26-2023  
AB rev to mdab_input.txt
[mdab_input_AB.txt](https://github.com/sanskrit-lexicon/MD/files/13768806/mdab_input_AB.txt)
mdab_input_AB.txt  corrects some mistakes by Jim, and fills in ??? items.
diff /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt mdab_input_AB.txt > tempdiff.txt

mdab_input_AB_rev.txt   Jim's revisions to mdab_input_AB.txt

diff mdab_input_AB.txt mdab_input_AB_rev.txt
21c21
< abs.  <id>abs.</id> <disp>absolutive.</disp>
---
> abs.  <id>abs.</id> <disp>absolute, absolutive</disp>
48c48
< cj+-. <id>cj.</id> <disp>conjunction.</disp>
---
> cj.   <id>cj.</id> <disp>conjunction.</disp>
166c166
< nl.   <id>nl.</id> <disp>nominal.</disp>      ;;for nouns (nominals), similar to vbl. for verbals
---
> nl.   <id>nl.</id> <disp>nominal.</disp>
255,256c255,256
< sts.  <id>sts.</id> <disp>stems. ?</disp>
< Sts.  <id>Sts.</id> <disp>Stems. ?</disp>
---
> sts.  <id>sts.</id> <disp>sometimes.</disp>
> Sts.  <id>Sts.</id> <disp>Sometimes.</disp>

## install mdab_input_AB_rev.txt
cp mdab_input_AB_rev.txt  /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt

--------------------------------------------------------
12-26-2023  
AB file uploaded Dec 26, 2023
[md_AB_v1.zip](https://github.com/sanskrit-lexicon/MD/files/13768757/md_AB_v1.zip)
rename to ../temp_md_ab_1rev2.txt

compare to previous version: ../temp_md_ab_v1_romana.txt

diff ../temp_md_ab_v1_romana.txt ../temp_md_ab_1rev2.txt
Only 1 line different, under 'upa'
   <ab>vb.</ab> -> <ab>vbl.</ab>  (print change)
--------------------------------------------------------
Push to Github.
cp mdab_input_AB_rev.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt

cp ../temp_md_ab_1rev2.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt

# local install of displays
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh md  ../../md
sh xmlchk_xampp.sh md
# ok

# commit csl-pywork
git add .
git commit -m "md: revise mdab_input.txt.
Ref: https://github.com/sanskrit-lexicon/MD/issues/11"

git push

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git pull
git add .
git commit -m "md:upa correction.
Ref: https://github.com/sanskrit-lexicon/MD/issues/11"

# revise csl-orig and csl-pywork at Cologne.
cd "scans/csl-orig"
git pull
cd ../csl-pywork/v02
git pull
# Regenerate displays for md
sh generate_dict.sh md  ../../MDScan/2020/

----------------------------------------------
push this repository to github
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue11/abv1
