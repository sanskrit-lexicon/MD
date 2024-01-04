# coding=utf-8
""" prep1a_check_status.py
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
  self.line_sfxes = []
  
def init_prep1a(filein):
 lines = read_lines(filein)
 recs = [Prep1a(line) for line in lines]
 return recs

def dict_by_L(recs):
 # recs = list of Prep1a objects
 d = {}
 for rec in recs:
  L = rec.L
  d[L] = rec
 return d

def line_to_sfxes(line):
 ans = [] # list of suffixes returned
 for m in re.finditer('{@-(.*?)@}',line):
  sfx = m.group(1)
  # often, there is a comma at the end of sfx. Remove that comma
  sfx = sfx.replace(',' , '')
  ans.append(sfx)
 return ans

def compare_lines_recs(lines,recs):
 recd = dict_by_L(recs)
 d = {}  # d[L] = sfxes, when L is a metaline with 1 or more sfxes
 ndiff2 = 0
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   # one data line assumed
   assert lines[iline+2].startswith('<LEND>')
   # skip this entry if it is not marked as <e>S (substantive)
   if not line.endswith('<e>S'):
    continue
   line1 = lines[iline+1] # the data line
   m = re.search(r'<L>(.*?)<',line)
   L = m.group(1) # L for the entry
   line_sfxes = line_to_sfxes(line1)
   if line_sfxes == []:
    continue
   if L not in recd:
    print('Diff 1: L=',L,'No Prep1 sfxes')
    print('line_sfxes=',line_sfxes)
    continue
   rec = recd[L]
   rec.line_sfxes = line_sfxes
   rec_sfxes = rec.sfxes
   # remove '*' from suffixes for comparison
   rec_sfxes1 = [sfx.replace('*','') for sfx in rec_sfxes]
   if rec_sfxes1 != line_sfxes:
    ndiff2 = ndiff2 + 1
    if True:
     print('Diff 2: L=',L,'difference in suffixes')
     print('  line: ',line_sfxes)
     print('   rec: ',rec_sfxes)
 print('ndiff2 = ',ndiff2)
  
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # prep1a_edit_status.txt

 lines = read_lines(filein)  # md.txt
 recs = init_prep1a(filein1)
 compare_lines_recs(lines,recs)
 # further check that all recs have been considered above
 recs_missed = [rec for rec in recs if rec.line_sfxes == []]
 print(len(recs_missed),'recs not accounted for')
 for rec in recs_missed:
  print('missed:', rec.line)

