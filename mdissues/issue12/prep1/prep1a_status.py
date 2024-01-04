#-*- coding:utf-8 -*-
"""prep1a_status.py
"""
from __future__ import print_function
import sys, re,codecs

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

class Prep1a_cpd_mw:
 def __init__(self,line):
  # consistent with outarr_rec of prep1a_cpd_mw.py
  #  out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s<cpd>%s' %(
  #  rec.L, rec.k1, rec.sfx1, rec.pfx, rec.sfx2, rec.cpd)
  self.line = line
  m = re.search(r'^<L>(.*?)<k1>(.*?)<sfx1>(.*?)<pfx>(.*?)<sfx2>(.*?)<cpd>(.*?)<mw>(.*)$',
                line) 
  self.L = m.group(1)
  self.k1 = m.group(2)
  self.sfx1 = m.group(3) # iast
  self.pfx = m.group(4)
  self.sfx2 = m.group(5) # slp1
  self.cpd = m.group(6)
  self.mw = m.group(7) # Y or N
  assert self.mw in ('Y','N')

def init_prep1a_cpd_mw(filein):
 lines = read_lines(filein)
 recs = [Prep1a_cpd_mw(line) for line in lines]
 print(len(recs),"records at init_prep1a_cpd_mw")
 if False:
  r = recs[0]
  print('init_prep1a_cpd_mw: first pfx=',r.pfx)
 return recs
 
def write_outrecs(fileout,outrecs):
 nlines = 0 # total number of lines writte
 with codecs.open(fileout,"w","utf-8") as f:
  for lines in outrecs:
   nlines = nlines + len(lines)
   for line in lines:
    f.write(line+'\n')  
 print("%s recs (%s lines) written to %s" %(len(outrecs),nlines,fileout))

def outarr_rec(rec):
 outarr = []
 out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s<cpd>%s<mw>%s' %(
   rec.L, rec.k1, rec.sfx1, rec.pfx, rec.sfx2, rec.cpd, rec.mw)
 outarr.append(out)
 return outarr

def group_by_L(recs):
 for irec,rec in enumerate(recs):
  L = rec.L
  if irec == 0:
   group = [rec]
   Lprev = rec.L
  elif Lprev == L:
   group.append(rec)
  else:
   # new L
   # yield the group
   yield group
   # start a new group
   group = [rec]
   Lprev = rec.L
 # last group
 yield group

class Status:
 # like output of prep1a.py
 def __init__(self,L,k1,pfx,sfxes,status):
  self.L = L
  self.k1 = k1
  self.pfx = pfx
  self.sfxes = sfxes
  self.stat = status  # mw/total n1/n2
  self.ok,self.nsfxes = self.stat.split('/')
  self.ok = int(self.ok)
  self.nsfxes = int(self.nsfxes)

def group_to_status(group):
 r0 = group[0]  # a Prep1a_cpd_mw object
 # r.L, r.k1, r.pfx are assumed the same for all recs in group
 sfxes = [r.sfx1 for r in group]  # iast suffixes
 nsfxes = len(group)
 nmw = len([r for r in group if r.mw == 'Y'])  # cpds found in mw
 status = '%s/%s' %(nmw,nsfxes)
 statusrec = Status(r0.L,r0.k1,r0.pfx,sfxes,status)
 return statusrec

def make_status(recs):
 # recs is array of Prep1a_cpd_mw objects
 # assume in <L> order.
 # returns array of Status objects
 groups = list(group_by_L(recs))
 print('%s groups' % len(groups))
 ans = [group_to_status(group) for group in groups]
 if False:
  ans0 = ans[0] # status rec
  print('make_status: first status record pfx=',ans0.pfx)
 return ans

def make_status_outarr(r):
 # r is Status object
 outarr = []
 L = r.L
 k1 = r.k1
 pfx = r.pfx  # this will be edited
 stat = r.stat
 sfxes = r.sfxes
 n = len(sfxes)
 sfxes_str = ', '.join(sfxes)
 out = '<L>%s<k1>%s<stat>%s<pfx>%s<sfxes>%s' %(L,k1,stat,pfx,sfxes_str)
 if False and (L == '19'):
  print('make_status_outarr: pfx=',pfx)
 outarr.append(out)
 return outarr

 
if __name__=="__main__":
 tranin = 'roman' # sys.argv[1]
 tranout = 'slp1'
 filein = sys.argv[1] #  prep1a_cpd.txt
 fileout = sys.argv[2] #
 recsin = init_prep1a_cpd_mw(filein)
 statrecs = make_status(recsin)

 outrecs = [make_status_outarr(r) for r in statrecs]
 write_outrecs(fileout,outrecs)
 # write the number that are completely solved
 done = [r for r in statrecs if r.ok == r.nsfxes]
 ndone = len(done)
 print('%s complete out of %s' %(ndone,len(statrecs)))
 partials = [r for r in statrecs if (r.ok != 0) and (r.ok != r.nsfxes)]
 npartial = len(partials)
 print('%s partially done' % npartial)
 
