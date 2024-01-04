#-*- coding:utf-8 -*-
"""prep1a_slp1.py
"""
from __future__ import print_function
import sys, re,codecs
sys.path.insert(0,'../')
import transcoder

transcoder.transcoder_set_dir('../transcoder')

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

class Prep1a:
 def __init__(self,line):
  self.line = line
  # consistent with output of prep1a.py
  m = re.search(r'<L>(.*?)<k1>(.*?)<stat>(.*?)<pfx>(.*?)<sfxes>(.*?)$',line)
  self.L = m.group(1)
  self.k1 = m.group(2)
  self.status = m.group(3)
  self.pfx = m.group(4)
  self.sfxes_str = m.group(5)
  self.sfxes = self.sfxes_str.split(', ')
  self.sfxes_slp1 = None
  
def init_prep1a(filein):
 lines = read_lines(filein)
 recs = [Prep1a(line) for line in lines]
 return recs

def transcode_rec(rec,tranin,tranout):
 sfxes = rec.sfxes
 a = [transcoder.transcoder_processString(x,tranin,tranout) for x in sfxes]
 rec.sfxes_slp1 = a

def write_outrecs(fileout,outrecs):
 nlines = 0 # total number of lines writte
 with codecs.open(fileout,"w","utf-8") as f:
  for lines in outrecs:
   nlines = nlines + len(lines)
   for line in lines:
    f.write(line+'\n')  
 print("%s recs (%s lines) written to %s" %(len(recs),nlines,fileout))

def outarr_rec(rec):
 outarr = []
 pfx = rec.pfx  # sometimes wrong -- a major editing issue
 for isfx,sfx_iast in enumerate(rec.sfxes):
  sfx_slp1 = rec.sfxes_slp1[isfx]
  out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s' %(
         rec.L,rec.k1, sfx_iast,pfx,sfx_slp1)
  outarr.append(out)
 return outarr

def write_recs(fileout,recs):
 outrecs = []
 for rec in recs:
  outarr = outarr_rec(rec)
  outrecs.append(outarr)

 write_outrecs(fileout,outrecs)
 
if __name__=="__main__":
 tranin = 'roman' # sys.argv[1]
 tranout = 'slp1'
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] #
 recs = init_prep1a(filein)
 for rec in recs:
  transcode_rec(rec,tranin,tranout)

 write_recs(fileout,recs)
