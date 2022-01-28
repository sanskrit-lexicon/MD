# coding=utf-8
"""readwriteA2.py
   
"""
from __future__ import print_function
import sys,re,codecs

# def f(x,y,z):  that's the way Python function definitions start
def read_lines(filein):
 # Notice the indentation
 # there's a lot packed into the next line.
 # We could say:
 #  open file named filein for reading. The file is encoded as utf-8.
 #  Use the variable 'f' for reading from the file. 'f' could be
 #  called the 'file handle'.
 with codecs.open(filein,"r","utf-8") as f:
  # Notice the further indentation
  # Read every line in the file, and strip from the end of each
  # line the line-ending characters '\r\n'
  # And, add each stripped line into the Python list named 'lines'
  lines = [line.rstrip('\r\n') for line in f]
 # Notice we have gone back to 1 character of indentation (same as 'with')
 # print to the 'console' a message indicating how many lines were read
 print(len(lines),"lines read from",filein)
 # the function returns the list of lines
 return lines

# this adjustlines function splits each line
def adjustlines(lines):
 newlines = []  # start with an empty list, in which the new lines will be put
 # adjust each line in a python 'for loop'
 
 for line in lines:
  # we know, from the way read_lines was constructed, that each element
  # in lines represents a line of the text file used as input ('filein')
  # As such, it is a python 'str' (for 'string'). There is a building way to
  # split strings into a list (separator is ":")
  x1 = line.split(":")
  newline1 = x1[0]
  x2 = line.split(":")
  newline2 = x1[1]
  # We want to add the new line to our list of new lines.
  # 'append' is the way to do that
  newlines.append(newline1)
  newlines.append(newline2)
 # we're done with the for loop, so we go back one level of indentation
 # We need to return the newlines object that this function computed
 return newlines
 
def write_lines(fileout,lines):
 # Note we call this function as 'write_lines(fileout,newlines)'.
 # In this function, the function parameter 'lines' will, when
 # called, have the value newlines.
 # open the file, but this time for 'writing'
 with codecs.open(fileout,"w","utf-8") as f:
  # write each line using a for loop
  for line in lines:
   # we will add the 'newline' line break character at the end of the line
   f.write(line+'\n')
 print(len(lines),"lines written to",fileout)
 # This function doesn't explicitly return anything.

if __name__=="__main__":
 # First input argument: path to input text file
 filein = sys.argv[1]
 # Second input argument: path to output text file
 fileout = sys.argv[2] # word frequency
 # Call function read_lines to get all the input lines into
 #  a python list 'lines'
 lines = read_lines(filein)
 # Call function adjustlines to do something to each line
 # Result is the list newlines
 newlines = adjustlines(lines)
 # write the list of new lines to fileout
 write_lines(fileout,newlines)
 # That's all this little program does

 
