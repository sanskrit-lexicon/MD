#-*- coding:utf-8 -*-
"""make_change_pc_2b.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

           
class Change(object):
 def __init__(self,metaline,lnum,line,newline): # or def __init__(self,line,newline):
  self.metaline = metaline # maybe we don't need this line
  self.lnum = lnum # maybe we don't need this line
  self.line = line
  self.newline = re.sub(r"(\{\%)|(\%\})", '', self.line) # or self.newline = newline
  
def generate_changes(entries):
 changes = [] # computed by this function
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   #lnum = linenum1 + iline + 1 
   if line.startswith('{%[Page'):
    newline = re.sub(r"(\{\%)|(\%\})", '', line) # I am not sure
    lnum = linenum1 + iline + 1
   # we should mention metaline, but I don't know how
   change = Change(metaline,lnum,line,newline)
   changes.append(change)
 print(len(changes),'lines that may need changes')
 return changes

def get_title(entries):
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
  outarr.append('; -------------------------------------')
  metaline = entry.metaline
  metaline1 = re.sub(r'<k2>.*$','',metaline)  # just show L,pc,k1
  outarr.append('; %s' %metaline1)
  lnum = linenum1 + iline + 1
  line = entry.dataline
  newline = change.newline
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
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
 title = get_title(entries)
 write_changes(fileout,changes,title)
