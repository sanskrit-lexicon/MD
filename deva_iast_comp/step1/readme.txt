step1/readme.txt

This readme.txt file is just a text file, written as a guide to what is in the
step1 directory.

# ------------------------------------

readwriteA2.py  Third python program, designed to read the lines of data.txt
  and write to another file the split lines.
  Usage:
python readwriteA2.py ../data.txt readwriteA2.txt

readwriteA3.py  4th python program, designed to read the lines of data.txt
  and write to another file the original and split lines with labels: orig, slp1, rest, iast. Four characters  ('-', '~', "*", "‘", "’", "[a]") in  the lines "iast" replaced by empty string ''.
  Usage:
python readwriteA3.py ../data.txt readwriteA3.txt

readwriteA4.py  5th python program, designed to read the lines of data.txt
  and write to another file the split lines and to transliterate the slp1 to iast (result of transliteration presents in the lines with label "slp-iast")
  Usage:
python readwriteA4.py ../data.txt readwriteA4.txt

readwriteA4_countabnormal.py  Minor variation calculates number of lines
  of form 'X:abnormal', and prints result to terminal.
 Usage:
 python readwriteA4_countabnormal.py readwriteA4_countabnormal.txt
   461 lines read from ../data.txt
    61 lines are marked as abnormal
  2766 lines written to readwriteA4_countabnormal.txt
 The output file is identical to readwriteA4.txt:
 diff readwriteA4.txt readwriteA4_countabnormal.txt
 (no output, which means the files are the same)

python nonascii.py ../data.txt nonascii.txt
 Find the non-ascii characters in the 'iast' portion of each line of data,
 and print each character along with its frequency.
 
python bytes.py inputfile outputfile
 reads the input file as a sequence of bytes.
    input file can be a text file, or even an image file or pdf.
 writes each byte on a separate line with additional information.
 
python unichars.py input.txt output.txt
 reads a text file as a sequence of unicode characters.
 Writes each character on a separate line with additional information.
 
