work on issue 11 for MD dictionary.
MD abbreviations 
--------------------------------------------------------------
abbrev0 folder:
prepare text form of printed abbreviations.
Final form abbrev0.txt
177 lines
format:
abbrev<TAB>= tooltip

--------------------------------------------------------------
temp_md_0.txt
 Original copy from csl-orig at 09-12-2023
cp /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt temp_md_0.txt

--------------------------------------------------------------
Prepare csl-pywork for MD abbreviations
-----
1. inventory.txt
/c/xampp/htdocs/cologne/csl-pywork/v02/inventory.txt
edit to add 'md' to the dictionaries with abbreviations
OLD:
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs:pywork/${dictlo}ab/${dictlo}ab.sql:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs:pywork/${dictlo}ab/${dictlo}ab_input.txt:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs:pywork/${dictlo}ab/readme.txt:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs:pywork/${dictlo}ab/redo.sh:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs:pywork/${dictlo}ab/redo_${dictlo}ab.sh:CD
NEW:
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/${dictlo}ab.sql:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/${dictlo}ab_input.txt:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/readme.txt:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/redo.sh:CD
ben stc bur cae mw pw pwkvn pwg lan gra ap90 bhs md:pywork/${dictlo}ab/redo_${dictlo}ab.sh:CD

-----
2. redo_postxml.sh
/c/xampp/htdocs/cologne/csl-pywork/v02/makotemplates/pywork/redo_postxml.sh
OLD:
%if dictlo in ['ben','stc','bur','cae','mw','pw','pwg','lan','gra','ap90','pwkvn','bhs']:
NEW:
%if dictlo in ['ben','stc','bur','cae','mw','pw','pwg','lan','gra','ap90','pwkvn','bhs','md']:
-----
3. mdab directory
---
3a. start with bhsab
cp -r /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/bhs/pywork/bhsab /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab
---
3b. change filenames
cd 
mv bhsab.sql mdab.sql
mv bhsab_input.txt mdab_input.txt
mv redo_bhsab.sh redo_mdab.sh
# return to me
cd /c/xampp/htdocs/sanskrit-lexicon/md/mdissues/issue11
---
3c. edit files and change 'bhs' to 'md'
 mdab.sql
 redo.sh
 redo_mdab.sh
-----
4. recreate mdab_input.txt
# copy abbrev0/abbrev0.txt to mdab/mdab_input.txt with format change
cd /c/xampp/htdocs/sanskrit-lexicon/md/mdissues/issue11
python make_mdab_input.py abbrev0/abbrev0.txt abbrev0/mdab_input_0.txt
cp abbrev0/mdab_input_0.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt


--------------------------------------------------------------
dev version
sh redo_dev.sh 1
creates issue11/dev1  displays
localhost/sanskrit-lexicon/MD/mdissues/issue11/dev1/web/
.gitignore

--------------------------------------------------------------
Cologne install based on temp_md_1.txt and abbrev1/abbrev1.txt
1. mdab_input_1.txt
  See abbrev1 directory for details
cp abbrev1/mdab_input_1.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/md/pywork/mdab/mdab_input.txt

2. md.txt
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt

3. generate local displays for md, check xml validity
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
sh generate_dict.sh md  ../../md

sh xmlchk_xampp.sh md
python3 ../../xmlvalidate.py ../../md/pywork/md.xml ../../md/pywork/md.dtd
ok

4. sync csl-pywork to github

5. update csl-orig repository and sync to github
cd /c/xampp/htdocs/cologne/csl-orig/v02/
   commit: 258eefdfa059239b571715b3e502d42ac28823a4
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue11

6. Login to Cologne ssh
6a. cd to scans/csl-orig
  git pull
6b. cd to scans/csl-pywork/v02
  git pull
6c. regen Cologne displays for md
 sh generate_dict.sh md  ../../MDScan/2020/

--------------------------------------------------------------
page 199 smudged -- need new image
237, 384
--------------------------------------------------------------

--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------
