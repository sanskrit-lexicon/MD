

# get temporary copy of slp1_iast.txt
curl https://raw.githubusercontent.com/sanskrit-lexicon/COLOGNE/master/iast/slp1_iast.txt -o temp_slp1_iast.txt

# get temporary copy of csl-orig/v02/md/md.txt
curl https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/master/v02/md/md.txt -o temp_md.txt

# module slp1iast.py
read and parse temp_slp1_iast.txt
Result is an array of SLP1IAST objects.

# module digentry.py
read and parse xxx.txt into list of Entry objects
# make_change_circumflex.py
reads md.txt, filter on characters with circumflex (using slp1iast)

#
python make_change_circumflex.py temp_md.txt temp_slp1_iast.txt change_1.txt
# cp change_1.txt change_1_edit.txt
  Do this only once. change_1_edit.txt is to be edited manually.
  change_1.txt is created by program make_change_circumflex.py
