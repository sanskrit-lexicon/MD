# coding=utf-8
"""nonascii.py
   
"""
from __future__ import print_function
import sys,re,codecs
import unicodedata  # used in freq_write to give unicode character names

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

def update_nonascii(iast,d):
 # remove the alphabetic characters and digits of iast
 # note the special syntax 'a-z' means characters from 'a' to 'z'
 x = re.sub(r'[a-zA-Z]','',iast)
 # loop through the remaining characters:
 # x is a string, looping through x gives the characters, one at a time
 for c in x: # c is a string of length
  if c not in d: # c is not yet a key of the dictionary d
   d[c] = 0  # add 'c' to the keys of d, and set its frequency to 0
  d[c] = d[c] + 1  # we've found one more 'c'
 # nothing specific to return. Thus function just updates 'd'
 # There actually is a None value returned, but we don't use it.
 
def freq_find(lines):
 # Use a python dictionary for the frequency count
 # the keys of the dictionary will be non-alphabetic characters.
 # and the value of the dictionary at a given character will
 # be the number of times that character appears in newline3 (the iast variable)
 d = {}  # start with an empty dictionary.
 for line in lines:
  x1 = line.split(":")
  newline1 = x1[0] # slp1
  newline2 = x1[1] # rest
  x3 = newline2.split()
  newline3 = x3[0] # the first sub-string of rest
  newline3a = re.sub(r"([-~*‘’])|(\[a\])","",newline3) # iast
  update_nonascii(newline3a,d)  # update d based on the iast string
 return d
 
def freq_write(fileout,d):
 # get the 'keys' of d. This is a list of characters (strings of length 1)
 keys = d.keys()
 # sort the keys in alphabetical order. Use builtin function sorted
 keys1 = sorted(keys)
 
 with codecs.open(fileout,"w","utf-8") as f:
  # write each line using a for loop
  for c in keys1:
   # a rather complicated expression
   # ord(c) is an integer x which is the 'value' of the charcter
   # \\u%04x converts integer x into a hex-code
   # d[key] is the frequency of the character
   # unicodedata.name(c) gives the Unicode name of the unicode character 'c'
   out = "%s  (\\u%04x) %5d := %s" %(c,ord(c),d[c],unicodedata.name(c))
   f.write(out+'\n')
 print(len(keys),"lines written to",fileout)
 # This function doesn't explicitly return anything.

if __name__=="__main__":
 # First input argument: path to input text file
 filein = sys.argv[1]
 # Second input argument: path to output text file
 fileout = sys.argv[2] # character frequency
 lines = read_lines(filein)
 # Generate a dictionary which has frequency of non-ascii characters in lines
 d = freq_find(lines)
 # write the frequency table
 freq_write(fileout,d)

 
