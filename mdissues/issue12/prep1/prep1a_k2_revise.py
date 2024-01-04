# coding=utf-8
""" prep1a_k2_revise.py
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

def init_k2dict(filein):
 lines = read_lines(filein)
 d = {}
 # <L>L<k1>k1<k2a>k2a<k2b>k2b
 for line in lines:
  m = re.search('^<L>(.*?)<k1>(.*?)<k2a>(.*?)<k2b>(.*$)',line)
  L = m.group(1)
  k2b = m.group(4)  #k2 for slp
  d[L] = k2b
 return d

def update_lines(lines,k2dict):
 newlines = []
 for line in lines:
  if not line.startswith('<L>'):
   newlines.append(line)
   continue
  # meta line
  m = re.search(r'<L>(.*?)<',line)
  L = m.group(1)
  k2new = k2dict[L]
  m1 = re.search(r'<k2>(.*?)<',line)
  k2old = m1.group(1)
  newline = line.replace('<k2>'+k2old+'<',  '<k2>'+k2new+'<')
  newlines.append(newline)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt 
 filein1 = sys.argv[2] # prep1a_k2_all.txt
 fileout = sys.argv[3] #  revise k2 metalines
 lines = read_lines(filein)  # md.txt
 k2dict = init_k2dict(filein1)
 newlines = update_lines(lines,k2dict)
 write_lines(fileout,newlines)
 
