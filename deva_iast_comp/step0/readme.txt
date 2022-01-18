step0/readme.txt

This readme.txt file is just a text file, written as a guide to what is in the
step0 directory.

# ------------------------------------
readwrite.py  First python program, designed to read the lines of data.txt
  and write the upper-cased lines to another file.
  Usage:
python readwrite.py ../data.txt readwrite.txt

Suggestions for study:
1.  Study the program - start at the bottom  (at 'if __name__=="__main__":').
  Pay particular attention to the indentation, as it is an important
  detail peculiar to Python.
  When you get to 'lines = read_lines(filein)', go back up to 'def read_lines'
  to see what the read_lines 'function' is doing.
  Similarly review the rest of the 'main' part.
2. Run the program, as indicated in the 'usage' comment above.
   Look at 'readwrite.txt' -  is it as you expected?
3. Make another program (you choose the name), which reads 'readwrite.txt'
   and changes all letters to lower case. Then run the program.
4. When you're done, push the directory.

#-------------------------------------------
'temp' files.
Look at the .gitignore file in the MD directory top level.
The 'temp*' line means that any file (or directory) whose name starts with
'temp' will NOT be tracked by git.  Such files will be available on your
machine, but will be ignored when you push.
This is a good way to make small experiments that are meaningful for you
but that might not be useful to other repository users.

Conversely, files which you
do want to share with others should have names that do not start with 'temp'.

You can always do a 'git status' after 'git add' but before 'git commit' to
see which files git is tracking.

#-------------------------------------------
readwriteA1.py  Second python program, designed to read the lines of data.txt
  and write the lower-cased lines to another file.
  Usage:
python readwriteA1.py ../data.txt readwriteA1.txt
