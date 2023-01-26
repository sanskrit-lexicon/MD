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
