# coding=utf-8
""" prep1a.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

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

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
 
def print_outrecs(outrecs):
 for outarr in outrecs:
  for out in outarr:
   print(out)

class Verb:
 def __init__(self,line):
  self.line = line
  m = re.search("^;; Case ([0-9]+): L=(.*?), k1=(.*?), k2=(.*?), code=(.*?)$",
               line)
  if m == None:
   print('Verb parse error:',line)
  self.case = m.group(1)
  self.L = m.group(2)
  self.k1 = m.group(3)
  self.k2 = m.group(4)
  self.code = m.group(5)
  assert self.code == 'V'
  
def init_verb_filter(filein):
 lines = read_lines(filein)
 recs = []
 d = {}
 for line in lines:
  rec = Verb(line)
  recs.append(rec)
  L = rec.L
  if L in d:
   print('Duplicate L=',rec.line)
  d[L] = rec
 print(len(recs),"read from",filein)
 return recs,d

def mark_verbs(mdlines,dverb):
 newlines = []
 n = 0 # number of verbs marked
 n1 = 0 # number of IBU, IKf verbs
 for line in mdlines:
  if not line.startswith('<L>'):
   newline = line
  else:
   m = re.search(r'<L>(.*?)<',line)
   L = m.group(1)
   if L in dverb:
    newline = '%s<e>V' % line
    n = n + 1
   elif re.search(r'(IBU<k2>)|(Ikf<k2>)|(Atkf<k2>)',line):
    # Ikf, IBU, Atkf
    newline = '%s<e>V1' % line
    n1 = n1 + 1
   else:
    newline = line
  newlines.append(newline)
 print(n,"metalines marked as V")
 print(n1,"metalines marked as V1")
 return newlines

def mark_other(mdlines):
 newlines = []
 n = 0 # number of <lex> substantives
 n1 = 0 # non-V, non-lex
 for iline,line in enumerate(mdlines):
  if not line.startswith('<L>'):
   newline = line
  else:
   # metaline. 
   if line.endswith(('<e>V', '<e>V1')):
    # nothing else to do for Verb
    newline = line
   else:
    # does next line contain '<lex>' tag? If so, mark as '<e>S'
    line1 = mdlines[iline+1]
    if '<lex>' in line1:
     newline = '%s<e>S' % line
     n = n + 1
    elif '<ab>pp.</ab>' in line1:
     # mark as S
     newline = '%s<e>S' % line
     n = n + 1
    elif '<ab>fp.</ab>' in line1:
     # mark as S
     newline = '%s<e>S' % line
     n = n + 1
    elif '<ab>pr.</ab> <ab>pt.</ab>' in line1:
     # mark as S
     newline = '%s<e>S' % line
     n = n + 1
    else: # mark entry as X
     newline = '%s<e>X' % line
     n1 = n1 + 1
  newlines.append(newline)
 print(n,"metalines marked as S")
 print(n1,"metalines marked as X")
 return newlines

class Compound:
 def __init__(self,L,k1,sfxes):
  self.L = L
  self.k1 = k1
  self.sfxes = sfxes
  
def get_compounds(mdlines):
 cpds = []
 for iline,line in enumerate(mdlines):
  if not line.endswith('<e>S'): # metaline for compound
   continue
  iline1 = iline + 1
  line1 = mdlines[iline1]
  # we are in a substantive entry
  # assume that '{@-X@}' is used to mark compounds
  sfxes = []
  for m in re.finditer('{@-(.*?)@}',line1):
   sfx = m.group(1)
   # often, there is a comma at the end of sfx. Remove that comma
   sfx = sfx.replace(',' , '')
   sfxes.append(sfx)
  if len(sfxes) == 0:
   # no suffixes
   continue
  # L,k1,sfxes
  m = re.search(r'<L>([^<]*).*?<k1>([^<]*)<k2>',line)
  L = m.group(1)
  k1 = m.group(2)
  cpd = Compound(L,k1,sfxes)
  cpds.append(cpd)
 return cpds

def write_compounds_unused(fileout,cpds):
 outarr = []
 ntot = 0 # total number of suffixes
 for cpd in cpds:
  L = cpd.L
  k1 = cpd.k1
  sfxes = cpd.sfxes
  n = len(sfxes)
  ntot = ntot + n
  sfxes_str = ', '.join(sfxes)
  out = '<L>%s<k1>%s<n>%s<sfxes>%s' %(L,k1,n,sfxes_str)
  outarr.append(out)
 write_lines(fileout,outarr)
 print(ntot,"count of suffixes")

def write_compounds(fileout,cpds):
 outarr = []
 ntot = 0 # total number of suffixes
 for cpd in cpds:
  L = cpd.L
  k1 = cpd.k1
  pfx = k1  # this will be edited
  sfxes = cpd.sfxes
  n = len(sfxes)
  ntot = ntot + n
  sfxes_str = ', '.join(sfxes)
  out = '<L>%s<k1>%s<stat>0/%s<pfx>%s<sfxes>%s' %(L,k1,n,pfx,sfxes_str)
  outarr.append(out)
 write_lines(fileout,outarr)
 print(ntot,"count of suffixes")
 

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # temp_verb_filter.txt
 fileout = sys.argv[3] #
 fileout1 = sys.argv[4]
 """
 entries_cdsl = digentry.init(filein)
 """
 lines = read_lines(filein)  # md.txt
 verbrecs,dverb = init_verb_filter(filein1)

 newlines = mark_verbs(lines,dverb)

 newlines1 = mark_other(newlines)
 write_lines(fileout,newlines1)

 cpds = get_compounds(newlines1)
 write_compounds(fileout1,cpds)
 