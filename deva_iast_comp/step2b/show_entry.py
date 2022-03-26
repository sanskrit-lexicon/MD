#-*- coding:utf-8 -*-
"""show_entry.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def get_title(nentry,fileout):
 outarr = []
 outarr.append('; ===================================================')
 outarr.append('; entry number %s from %s' %(nentry,fileout))
 outarr.append('; ===================================================')
 return outarr
 
def write_entry(fileout,entry,title):
 outrecs = [] # list of lines for each change
 outrecs.append(title)
 outarr = [] # lines for this change
 linenum1 = entry.linenum1  # line number in md.txt for metaline
 outarr.append('(%s) entry.metaline     = %s' % (linenum1,entry.metaline))
 entrylines = entry.datalines  # lines between metaline and <LEND> line
 for iline,line in enumerate(entrylines):
  # line == entrylines[iline]
  # lnum is line number in md.txt of this line
  # iline starts at 0, so we add 1
  lnum = linenum1 + iline + 1
  outarr.append('(%s) entry.datalines[%s] = %s' %(lnum,iline,line))
 lend = entry.lend  # the <LEND> line. 
 linenum2 = entry.linenum2 # line number in md.txt for <LEND> 
 outarr.append('(%s) entry.lend         = %s' %(linenum2,lend))
 outrecs.append(outarr)
 # write the records
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

if __name__=="__main__":
 nentry = int(sys.argv[1])  # number of the entry to show
 filein = sys.argv[2] #  xxx.txt
 fileout = sys.argv[3] # changes
 entries = digentry.init(filein)
 title = get_title(nentry,fileout)
 entry = entries[0]
 write_entry(fileout,entry,title)
