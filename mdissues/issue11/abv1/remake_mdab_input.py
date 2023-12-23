# coding=utf-8
""" remake_mdab_input.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines
 
def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in lines:
    f.write(out+'\n')  
 print(len(lines),"cases written to",fileout)
 exit(1)

def make_newlines(lines):
 newlines = []
 for line in lines:
  newline = re.sub(r'</disp>.*$', '</disp>',line)
  newlines.append(newline)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1] # File with abbreviations and counts
 fileout = sys.argv[2] # abbreviations remove counts,etc
 lines = read_lines(filein)
 print(len(lines),"lines from",filein)
 newlines = make_newlines(lines)
 write_lines(fileout,newlines)
 

