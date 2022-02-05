# coding=utf-8
"""unichars.py
   python unichars.py input.txt output.txt
  Read input file as a sequence of unicode characters.
  Write each character (with unicode information) to a line of output.
"""
from __future__ import print_function
import sys,re,codecs
import unicodedata  # used in freq_write to give unicode character names

def read_chars(filein):
 #  open file named filein for reading. The file is encoded as utf-8.
 with codecs.open(filein,"r","utf-8") as f:
  chars = f.read()  # list of all characters in the file
 print(len(chars),"unicode characters read from",filein)
 # the function returns the list of characters
 return chars

def chars_write(fileout,chars):
 with codecs.open(fileout,"w","utf-8") as f:
  # write each chars using a for loop
  for ic,c in enumerate(chars):
   # a rather complicated expression
   # ord(c) is an integer x which is the 'value' of the charcter
   # \\u%04x converts integer x into a hex-code
   # unicodedata.name(c) gives the Unicode name of the unicode character 'c'
   # There is no unicode name for line feed and carriage return
   #  REF: https://stackoverflow.com/questions/24552786/why-doesnt-unicodedata-recognise-certain-characters
   code = ord(c)
   c1 = c
   if code == 10:
    name = '[NEWLINE]'
    c1 = ' '  # display as a space
   elif code == 13:
    name = '[CARRIAGE RETURN]'
    c1 = ' '  # display as a space
   else:
    try:
     name = unicodedata.name(c)
    except:
     name = 'NAME NOT FOUND. code = %d' %code
     c1 = ' '  # display as a space
   out = "%05d %s  (\\u%04x)  := %s" %(ic+1,c1,code,name)
   f.write(out+'\n')
 print(len(chars),"lines written to",fileout)
 # This function doesn't explicitly return anything.

if __name__=="__main__":
 # First input argument: path to input text file
 filein = sys.argv[1]
 # Second input argument: path to output text file
 fileout = sys.argv[2] # character frequency
 chars = read_chars(filein) # list of unicode characters in filein
 # write the sequence of characters
 chars_write(fileout,chars)

 
