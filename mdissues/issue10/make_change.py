# coding=utf-8
""" 
make_change.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def changes(entries):
 nfound = 0
 for entry in entries:
  entry.changedata = None
  meta = entry.metaline
  m = re.search(r'<h>([0-9]+)',meta)
  if m == None:
   continue
  # change first line, by inserting
  # '<hom>N.</hom> '
  hom = m.group(1)
  iline = 0
  old = entry.datalines[0]
  lnum = entry.linenum1 + iline + 1
  new = '<hom>%s.</hom> %s' %(hom,old)
  entry.changedata = (meta,lnum,old,new)
  nfound = nfound + 1
 print('%s entries with hom' % nfound)

def write(fileout,entries):
 outrecs = []
 for entry in entries:
  changedata = entry.changedata
  if changedata == None:
   continue
  (meta,lnum,old,new) = changedata
  outarr = []
  
  outarr.append('; ------------------------------------------------------')
  outarr.append('; %s' % meta)
  outarr.append('%s old %s' %(lnum,old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,new))
  outrecs.append(outarr)   
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"changes written to",fileout)
if __name__=="__main__":
 filein = sys.argv[1] # e.g., mw.txt
 fileout = sys.argv[2] # text output
 # read all the entries of the dictionary.
 entries = digentry.init(filein)
 
 changes(entries)
 write(fileout,entries)
