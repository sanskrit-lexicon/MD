
# get temporary copy of csl-orig/v02/md/md.txt
curl https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/master/v02/md/md.txt -o temp_md_0.txt

# create pcerror.txt  
# module digentry.py
read and parse xxx.txt into list of Entry objects
Used by make_change_pc.py

# make_change_pc.py
reads md.txt and 

#
python make_change_circumflex.py temp_md.txt pcdata.txt change_1.txt
  change_1.txt is created by program make_change_circumflex.py

#
python updateByLine.py temp_md_00.txt change_1_edit_copy.txt temp_md_01.txt
The program modify the copy of md.txt (temp_md_00.txt) according the changes included in the change_1_edit_copy.txt
change_1_edit_copy.txt is the edited manually change_1_edit.txt
