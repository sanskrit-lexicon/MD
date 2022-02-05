# coding=utf-8
"""bytes.py
   python bytes.py input.txt output.txt
  Read input file as a sequence of bytes.
  Write each byte to a line of output.
"""
from __future__ import print_function
import sys,re,codecs
import unicodedata  # used in freq_write to give unicode character names

def read_bytes(filein):
 #  open file named filein for reading. 
 with codecs.open(filein,"rb") as f:
  bytes = f.read()  # list of all bytes in the file
 print(len(bytes),"bytes read from",filein)
 # the function returns the list of bytes
 return bytes

def bytes_write(fileout,bytes):
 with codecs.open(fileout,"w","utf-8") as f:
  # write each byte using a for loop
  for ibyte,code in enumerate(bytes):
   c1 = chr(code)
   if code == 10:
    c1 = ' '  # display as a space
    name = '[NEWLINE]'
   elif code == 13:
    c1 = ' '  # display as a space
    name = '[CARRIAGE RETURN]'
   elif code >= 128:
    name = '...'
    c1 = ' '
   else:
    try:
     name = unicodedata.name(c1)
    except:
     name = 'NAME NOT FOUND. code = %d' %code
     c1 = ' '  # display as a space
   out = "%05d %s  (\\u%02x)  := %s" %(ibyte+1,c1,code,name)
   f.write(out+'\n')
 print(len(bytes),"lines written to",fileout)
 # This function doesn't explicitly return anything.

if __name__=="__main__":
 # First input argument: path to input text file
 filein = sys.argv[1]
 # Second input argument: path to output text file
 fileout = sys.argv[2] # character frequency
 bytes = read_bytes(filein) # list of unicode characters in filein
 # write the sequence of characters
 bytes_write(fileout,bytes)

 
