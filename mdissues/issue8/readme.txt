work on issue 8 for MD dictionary.

# startup instructions (for Anna)
make a 'sanskrit-lexicon' directory (such as in ~/Documents/)
cd ~/Documents/sanskrit-lexicon
# clone the MD directory from Github.
git clone https://github.com/sanskrit-lexicon/MD.git
--------------------------------------------------------------
# get temporary copy of latest md.txt
cd ~/Documents/sanskrit-lexicon/md/mdissues/issue8
#
cp ~/Documents/cologne/csl-orig/v02/md/md.txt temp_mw_0.txt
# make a second copy in issue8
cp temp_mw_0.txt temp_mw_1.txt
# manually examine few.more.corrections.in.MD.txt (file from issue8)
# and make corresponding changes in temp_mw_1.txt.
#   keep separate file of notes (maybe in readme_fewmore.txt)
--------------------------------------------------------------
diff_to_changes_dict.py usage
# Generate 'change transactions' from two versions of a dictionary file
# When you make changes to temp_mw_1.txt, then you can generate a
# 'change file'; let's name the change file 'change_fewmore.txt'
python diff_to_changes_dict.py temp_md_0.txt temp_md_1.txt change_fewmore.txt


--------------------------------------------------------------
updateByLine.py usage
# Anna may not need this. But Jim can use it to his local copy of
# revised md.txt
# Jim also gets temp_md_0.txt from his local csl-orig repository.
# change_fewmore.txt is created by Anna, and pulled by Jim.
python updateByLine.py temp_md_0.txt change_fewmore.txt temp_md_1.txt
--------------------------------------------------------------
02-06-2023
 Anna submitted change_few.more.txt
 This is similar to the desired form, but not quite the same.
 Next program transforms change_few.more.txt to temp_change_fewmore.txt,
  
python change_adj.py change_few.more.txt change_fewmore_a.txt
 This required a couple of edits to change_few.more.txt.

# Now apply this change file, getting temp_md_0a.txt.
python updateByLine.py temp_md_0.txt change_fewmore_a.txt temp_md_0a.txt
# Next,
python diff_to_changes_dict.py temp_md_0.txt temp_md_0a.txt change_fewmore.txt
#  change_fewmore.txt is functionally the same as change_fewmore_a.txt,
#  but has extra 'metaline' information helpful for debugging.
#
# Next manually reviewed change_fewmore.txt, and
# changed several.  Search ';x' for these items.
-------------------------------------------------
# now get temp_md_1.txt by applying the modified change_fewmore.txt.
python updateByLine.py temp_md_0.txt change_fewmore.txt temp_md_1.txt
-------------------------------------------------
Ready to install temp_md_1.txt.
# first, install locally
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
# check xml
sh xmlchk_xampp.sh md
# ok.
## update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .  # v02/md/md.txt
git commit -m "md. Misc corrections.
 Ref: https://github.com/sanskrit-lexicon/MD/issues/8"
git push
----------------------------------------------------
update at Cologne
cd ... csl-orig
git pull
cd ../csl-pywork/v02
grep 'md ' redo_cologne_all.sh
sh generate_dict.sh md  ../../MDScan/2020/
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
----------------------------------------------------
update this md repository
-------------------------------------------------
Ready to install temp_md_1.txt.
# first, install locally
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
# check xml
sh xmlchk_xampp.sh md
# ok.
## update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .  # v02/md/md.txt
git commit -m "md. Misc corrections.
 Ref: https://github.com/sanskrit-lexicon/MD/issues/8"
git push
----------------------------------------------------
update at Cologne
cd ... csl-orig
git pull
cd ../csl-pywork/v02
grep 'md ' redo_cologne_all.sh
sh generate_dict.sh md  ../../MDScan/2020/
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
----------------------------------------------------
update this md repository
-------------------------------------------------
Ready to install temp_md_1.txt.
# first, install locally
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
# check xml
sh xmlchk_xampp.sh md
# ok.
## update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .  # v02/md/md.txt
git commit -m "md. Misc corrections.
 Ref: https://github.com/sanskrit-lexicon/MD/issues/8"
git push
----------------------------------------------------
update at Cologne
cd ... csl-orig
git pull
cd ../csl-pywork/v02
grep 'md ' redo_cologne_all.sh
sh generate_dict.sh md  ../../MDScan/2020/
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
----------------------------------------------------
update this md repository
-------------------------------------------------
Ready to install temp_md_1.txt.
# first, install locally
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
# check xml
sh xmlchk_xampp.sh md
# ok.
## update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .  # v02/md/md.txt
git commit -m "md. Misc corrections.
 Ref: https://github.com/sanskrit-lexicon/MD/issues/8"
git push
----------------------------------------------------
update at Cologne
cd ... csl-orig
git pull
cd ../csl-pywork/v02
grep 'md ' redo_cologne_all.sh
sh generate_dict.sh md  ../../MDScan/2020/
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
----------------------------------------------------
update this md repository
-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
change_2.txt applied, to get temp_md_2.txt
python updateByLine.py temp_md_1.txt change_2.txt temp_md_2.txt
-------------------------------------------------
Ready to install temp_md_2.txt.
# first, install locally
cp temp_md_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md
# check xml
sh xmlchk_xampp.sh md
# ok.
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
## update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .  # v02/md/md.txt
git commit -m "md. Misc corrections.
 Ref: https://github.com/sanskrit-lexicon/MD/issues/8"
git push
----------------------------------------------------
update at Cologne
cd ... csl-orig
git pull
cd ../csl-pywork/v02
grep 'md ' redo_cologne_all.sh
sh generate_dict.sh md  ../../MDScan/2020/
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
----------------------------------------------------
update this md repository
***********************************************************
Corrections involving ¤
Use file md.lines.having.numbers.without.the.symbol.marking.txt
# make corrections to temp_md_3.txt
cp temp_md_2.txt temp_md_3.txt
# generate change transactions for comparison purposes.
python diff_to_changes_dict.py temp_md_2.txt temp_md_3.txt change_3.txt

# NOTE: two cases (30413, 32185) The md.lines file has `¤(1/4)¤`.
  but change_2 uses `¤1/4¤`  Reason: print has no parens.

NOW, go through the installation.

cp temp_md_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md
# check xml
sh xmlchk_xampp.sh md
# ok.
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
## update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .  # v02/md/md.txt
git commit -m "md. Misc corrections. change_3
 Ref: https://github.com/sanskrit-lexicon/MD/issues/8"
git push
----------------------------------------------------
update at Cologne
cd ... csl-orig
git pull
cd ../csl-pywork/v02
grep 'md ' redo_cologne_all.sh
sh generate_dict.sh md  ../../MDScan/2020/
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue8
----------------------------------------------------
update this md repository
