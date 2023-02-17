work on issue 10 for MD dictionary.

--------------------------------------------------------------
# get temporary copy of latest md.txt
cd /c/xampp/htdocs/sanskrit-lexicon/md/mdissues/issue10
#
cp /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt temp_md_0.txt
--------------------------------------------------------------

python make_change.py temp_md_0.txt change_1.txt

146636 lines read from temp_md_0.txt
20749 entries found
920 entries with hom
920 changes written to change_1.txt

--------------------------------------------------------------
# updateByLine.py usage
python updateByLine.py temp_md_0.txt change_1.txt temp_md_1.txt

146636 lines read from temp_md_0.txt
146636 records written to temp_md_1.txt
920 change transactions from change_1.txt
--------------------------------------------------------------
Ready to install temp_md_1.txt.
# first, install locally
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
# check xml
sh xmlchk_xampp.sh md
# ok.
## update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .  # v02/md/md.txt
git commit -m "md. Misc corrections.
 Ref: https://github.com/sanskrit-lexicon/MD/issues/10"
git push
----------------------------------------------------
update at Cologne
cd ... csl-orig
git pull
cd ../csl-pywork/v02
grep 'md ' redo_cologne_all.sh
sh generate_dict.sh md  ../../MDScan/2020/
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
----------------------------------------------------
update this md repository
-------------------------------------------------
Ready to install temp_md_1.txt.
# first, install locally
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
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
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
----------------------------------------------------
update this md repository
-------------------------------------------------
Ready to install temp_md_1.txt.
# first, install locally
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
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
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
----------------------------------------------------
update this md repository
-------------------------------------------------
Ready to install temp_md_1.txt.
# first, install locally
cp temp_md_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/md/md.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'md ' redo_xampp_all.sh
sh generate_dict.sh md  ../../md

cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
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
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
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
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
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
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
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
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
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
cd /c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue10
----------------------------------------------------
update this md repository
