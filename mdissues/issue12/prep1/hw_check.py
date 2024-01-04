#-*- coding:utf-8 -*-
"""hw_check.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"lines read from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"lines written to",fileout)

def init_hws(filein):
 # <L>1<pc>1,1<k1>a<k2>a<h>1<e>1<ln1>5<ln2>7
 lines = read_lines(filein)
 d = {} # unique
 for iline,line in enumerate(lines):
  m = re.search('^<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',line)
  k1 = m.group(3)
  d[k1] = True
 #  
 keys = d.keys()
 print("%s keys from %s" %(len(keys),filein))
 return d

if __name__=="__main__":
 filein = sys.argv[1] #  list of words (slp1 Sanskrit), one per line
 filein1 = sys.argv[2] #  headwords in xxxhw.txt format 
 fileout = sys.argv[3] # list of words found

 words = read_lines(filein) 
 hwd = init_hws(filein1) # dictionary of k1s from xxxhw.txt
 
 found = [x for x in words if x in hwd]

 write_lines(fileout,found)
