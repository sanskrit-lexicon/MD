# coding=utf-8
""" prep1a_k2_all_check.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  
sys.path.insert(0,'../')
import transcoder

transcoder.transcoder_set_dir('../transcoder')
tranin = 'roman'
tranout = 'slp1'

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


class Meta:
 def __init__(self,L,k1,k2a,k2b):
  self.L = L
  self.k1 = k1
  self.k2a = k2a  # roman/iast
  self.k2b = k2b  # slp1

def get_k2(line):
 # {#aMsakUwa#}¦ aṃsa-kūṭa,  return aṃsa-kūṭa
 # if the parse fails, return None
 # remove <hom>X</hom> if present
 line = re.sub(r'¦ <hom>[0-9]+.</hom>', '¦',line)
 m = re.search(r'^{#.*?#}¦ (.*?),',line)
 if m == None:
  # probably no comma found. 
  # e.g.L=3444: {#AN#}¦ ā-ṅ = {#A#} <hom>1.</hom> ā (<ab>gr.</ab>).
  # try an alternate method
  m1 = re.search(r'¦ (.*?)[ ,]',line)
  if m1 != None:
   k2 = m1.group(1)
  else:
   k2 = None
 else:
  k2 = m.group(1)
 # Sometimes the 'comma' in search above is at the wrong place
 # remove a space and subsequent data
 if k2 != None:
  k2adj = re.sub(r' .*$','',k2)
  return k2adj
 else:
  return None

def get_metas(mdlines):
 metas = []
 nprob = 0  # cannot find k2
 for iline,line in enumerate(mdlines):
  if not line.startswith('<L>'): # metaline
   continue
  iline1 = iline + 1
  line1 = mdlines[iline1] # The data-line
  k2a = get_k2(line1)
  if k2a == None:
   nprob = nprob + 1
   k2b = None
  else:
   # require lower-case IAST
   k2alow = k2a.lower()
   k2b = transcoder.transcoder_processString(k2alow,tranin,tranout)
  # L,k1
  m = re.search(r'<L>([^<]*).*?<k1>([^<]*)<k2>',line)
  L = m.group(1)
  k1 = m.group(2)
  meta = Meta(L,k1,k2a,k2b)
  metas.append(meta)
 print(len(metas),'meta k2s found')
 print(nprob,"of these have no k2")
 return metas

def write_metas(fileout,metas):
 outarr = []
 ntot = 0 # total number of metas
 for meta in metas:
  L = meta.L
  k1 = meta.k1
  pfx = k1  # this will be edited
  k2a = meta.k2a
  k2b = meta.k2b
  out = '<L>%s<k1>%s<k2a>%s<k2b>%s' %(L,k1,k2a,k2b)
  outarr.append(out)
 write_lines(fileout,outarr)

def get_dict(lines):
 d = {}
 for line in lines:
  m = re.search(r'<L>(.*?)<',line)
  L = m.group(1)
  d[L] = line
 return d

if __name__=="__main__":
 filein = sys.argv[1] # prep1a_k2_all
 filein1 = sys.argv[2] # prep1a_k2_edit
 lines = read_lines(filein)  
 lines1 = read_lines(filein1)  
 dlines = get_dict(lines)
 nprob = 0
 for line1 in lines1:
  m = re.search(r'<L>(.*?)<',line1)
  L = m.group(1)  
  line = dlines[L]
  if line != line1:
   nprob = nprob + 1
   print('prep1a_k2_edit:',line1)
   print('prep1a_k2_all :',line)
   print()
 print(nprob,'consistency problems')
 
