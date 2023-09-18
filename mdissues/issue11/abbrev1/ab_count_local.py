# coding=utf-8
""" ab_count_local.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def count_local(lines):
 newlines = []
 inentry = False
 dabbrev = {}
 
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   newline = line
   inentry = True
  elif line.startswith('<LEND>'):
   newline = line
   inentry = False
  elif not inentry:
   newline = line
  elif line.strip() == '':
   newline = line
  elif line.startswith('[Page'):
   newline = line
  else:
   for m in re.finditer(r'<ab n="(.*?)">(.*?)</ab>',line):
    abbrev = m.group(0)
    if abbrev not in dabbrev:
     dabbrev[abbrev] = 0
    dabbrev[abbrev] = dabbrev[abbrev] + 1
 return dabbrev

def write_recs(fileout,d):
 keys = sorted(d.keys())
 outarr = []
 for key in keys:
  out = '%s :: %s' %(key,d[key])
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)
 exit(1)
 
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 fileout = sys.argv[2] # abbreviations with counts
 lines = read_lines(filein)
 print(len(lines),"lines from",filein)
 dabbrev = count_local(lines)
 write_recs(fileout,dabbrev)
 

