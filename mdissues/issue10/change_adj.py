""" change_adj.py
"""
#
from __future__ import print_function
import re,sys
import codecs
sys.stdout.reconfigure(encoding='utf-8') 

def init_changes(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\n\r') for line in f if line.startswith('Line ')]
  print(len(lines),"lines read from",filein)
 changes = []
 for iline,line in enumerate(lines):
  if (iline % 2) == 0:
   m = re.search(r'^Line ([0-9]+): (.*)$',line)
   if m == None:
    print('error 1: ', line)
    exit(1)
   lnumstr = m.group(1)
   old = m.group(2)
   line1 = lines[iline+1] # next line
   m1 = re.search(r'^Line new: (.*)$',line1)
   if m1 == None:
    print('error 2: ',line1)
    exit(1)
   new = m1.group(1)
   change = (lnumstr,old,new)
   changes.append(change)
 print(len(changes),"changes found")
 return changes

def write(changes,fileout):
 with codecs.open(fileout,'w','utf-8') as f:
  for change in changes:
   lnum,old,new = change
   outarr = []
   outarr.append('%s old %s' %(lnum,old))
   outarr.append('%s new %s' %(lnum,new))
   outarr.append('; ---------------------------------------------')
   for out in outarr:
    f.write(out+'\n')
if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 changes = init_changes(filein)
 write(changes,fileout)

