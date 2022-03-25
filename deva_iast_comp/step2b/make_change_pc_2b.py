#-*- coding:utf-8 -*-
"""make_change_pc_2b.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

           
class Change(object):
 def __init__(self,entry):
  self.entry = entry

def generate_changes(entries):
 changes = [] # computed by this function
 for entry in entries:
  x = re.search(r"\{\%\[Page", entry)
  if x:
# z = x.string
# if z == entry:
   change = Change(entry)
   changes.append(change)
 print(len(changes),'lines that may need changes')
 return changes

def get_title(pcrecs):
 outarr = []
 outarr.append('; ===================================================')
 outarr.append('; Italicized page errors correction')
 outarr.append('; ===================================================')
 return outarr
               
def write_changes(fileout,changes,title):
 outrecs = [] # list of lines for each change
 outrecs.append(title)
 for change in changes:
  outarr = [] # lines for this change
  entry = change.entry
  outarr.append('; -------------------------------------')
  lnum = entry.linenum1
  dataline = entry.dataline
  newentry = re.sub(r"(\{\%)|(\%\})", '', dataline)
  outarr.append('; %s' %dataline)
  outarr.append('%s old %s' %(lnum,dataline))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newentry))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt
 fileout = sys.argv[2] # changes
 entries = digentry.init(filein)
 changes = generate_changes(entries)
 title = get_title(pcrecs)
 write_changes(fileout,changes,title)
