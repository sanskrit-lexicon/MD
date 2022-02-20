#-*- coding:utf-8 -*-
"""make_change2_ls.py
"""
from __future__ import print_function
import sys, re,codecs
import slp1iast
import digentry
           
class Change(object):
 def __init__(self,entry,iline,a):
  self.entry = entry
  self.iline = iline
  self.wordcvs = a

def generate_changes(entries,cvrecs):
 changes = [] # computed by this function
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1+iline+1
   words = line.split() # Default split on white space
   a = [] # list of (word,iast) tuples found in line
   for word in words:
    for cvrec in cvrecs:
     if cvrec.iast in word:  
      a.append((word,cvrec.iast))
     if cvrec.iastcap in word:
      a.append((word,cvrec.iastcap))
   # words loop finished
   if a == []:
    continue  # no instances in this line
   # generate a change object 
   change = Change(entry,iline,a)
   changes.append(change)
 print(len(changes),'lines that may need changes')
 return changes

def get_title(sirecs):
 outarr = []
 outarr.append('; ===================================================')
 outarr.append('slp1 vowels with possible iast (lower and upper case)')
 slp1vowels = 'aAiIuUfFxXeEoO'
 for v in slp1vowels:
  a = []
  for sirec in sirecs:
   if sirec.slp1.startswith(v):
    a.append(sirec.iast)
    a.append(sirec.iastcap)
  astr = ' '.join(a)  # string space separated
  out = '; slp1 %s : %s' %(v,astr)
  outarr.append(out)
 outarr.append('; ===================================================')
 outarr.append('; LINES CONTAINING IAST CIRCUMFLEX VOWELS')
 outarr.append('; CHANGE new LINE IF NEEDED')
 outarr.append('; ===================================================')
 return outarr
               
def write_changes(fileout,changes,title):
 outrecs = [] # list of lines for each change
 outrecs.append(title)
 for change in changes:
  outarr = [] # lines for this change
  entry = change.entry
  iline = change.iline
  wordcvs = change.wordcvs
  line = entry.datalines[iline]
  linenum1 = entry.linenum1 
  lnum = linenum1 + iline + 1 # the line number in xxx.txt of this line
  #
  outarr.append('; -------------------------------------')
  metaline = entry.metaline
  metaline1 = re.sub(r'<k2>.*$','',metaline)  # just show L,pc,k1
  outarr.append('; ' + metaline1)
  if len(wordcvs) != 1:
   print('multiple at line',lnum)
  for word,iast in wordcvs:
   outarr.append('; %s  %s' %(iast,word))
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  newline = line # to be changed
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

def get_si_circumvowel(recs):
 def cv(rec):
  if 'CIRCUMFLEX' not in rec.doc:
   return False
  elif re.search(r'^[aAiIuUfFxXeEoO]',rec.slp1) == None:
   return False
  else:
   return True
 cvrecs = [rec for rec in recs if cv(rec)]
 print(len(cvrecs),"vowels with iast circumflex")
 return cvrecs

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt
 filesi = sys.argv[2]  # slp1_iast.txt
 fileout = sys.argv[3] # change_X
 entries = digentry.init(filein)
 sirecs = slp1iast.init(filesi)
 sirecscv = get_si_circumvowel(sirecs)
 changes = generate_changes(entries,sirecscv)
 title = get_title(sirecs)
 write_changes(fileout,changes,title)
