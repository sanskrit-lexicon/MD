#-*- coding:utf-8 -*-
"""prep1a_pfx.py
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

class K2:
 def __init__(self,line):
  # '<L>%s<k1>%s<k2a>%s<k2b>%s' %(L,k1,k2a,k2b)
  m = re.search(r'^<L>(.*)<k1>(.*)<k2a>(.*)<k2b>(.*)$',line)
  self.L = m.group(1)
  self.k1 = m.group(2)
  self.k2a = m.group(3)  # roman/iast
  self.k2b = m.group(4)  # slp1 # has accents, etc.

def init_k2(filein):
 lines = read_lines(filein)
 recs = [K2(line) for line in lines]
 print(len(recs),"K2 records from",filein)
 # dictionary on L
 d = {}
 for rec in recs:
  d[rec.L] = rec
 return recs,d

class Prep1a: # statusrecs
 def __init__(self,line):
  self.line = line
  # consistent with output of prep1a.py
  m = re.search(r'<L>(.*?)<k1>(.*?)<stat>(.*?)<pfx>(.*?)<sfxes>(.*?)$',line)
  self.L = m.group(1)
  self.k1 = m.group(2)
  self.stat = m.group(3)
  self.pfx = m.group(4)
  self.sfxes_str = m.group(5)
  self.sfxes = self.sfxes_str.split(', ')
  self.sfxes_slp1 = None # not used
  self.newpfx = None
def init_prep1a(filein):
 lines = read_lines(filein)
 recs = [Prep1a(line) for line in lines]
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
 # pfx = r.pfx  # this will be edited
 pfx = r.newpfx
 stat = r.stat
 sfxes = r.sfxes
 n = len(sfxes)
 sfxes_str = ', '.join(sfxes)
 out = '<L>%s<k1>%s<stat>%s<pfx>%s<sfxes>%s' %(L,k1,stat,pfx,sfxes_str)
 if False and (L == '19'):
  print('make_status_outarr: pfx=',pfx)
 outarr.append(out)
 return outarr

def drop_accent(x):
 x = x.replace('/','')
 x = x.replace('\\','')
 x = x.replace('^','')
 # also, karma‿anta -> karma-anta  
 x = x.replace('‿', '-')
 return x 

def get_newpfx(k2rec):
 k2b = k2rec.k2b  # slp1 form of k2rec.k2a
 k2 = drop_accent(k2b)  # as in prep1a_cpd.py
 parts = k2.split('-')
 if len(parts) == 1:
  # no '-'.  Use k1
  pfx = k2rec.k1
 else:
  # if k2 = X-Y, set pfx to X
  # drop last part
  pfx = ''.join(parts[0:-1])
 # but 250+ are 'a'.
 if len(pfx) == 1:  # one character
  # use k1
  pfx = k2rec.k1
 return pfx

def update_pfx(statrecs,k2d):
 for statrec in statrecs:
  if not statrec.stat.startswith('0/'):
   # modify statrec.newpfx.  But only when stat = 0
   pass
  L = statrec.L
  if L not in k2d:
   print('update_pfx: L=%s,%s not in K2 records' % (L,statrec.k1))
   statrec.newpfx = statrec.pfx
   continue
  k2rec = k2d[L]
  statrec.newpfx = get_newpfx(k2rec)
  
if __name__=="__main__":
 filein = sys.argv[1] # prep1_status
 filein1 = sys.argv[2] # prep1a_k2
 fileout = sys.argv[3] #
 k2,k2d = init_k2(filein1)
 #
 statrecs = init_prep1a(filein)
 # replace pfx in statrecs
 update_pfx(statrecs,k2d)
 
 outrecs = [make_status_outarr(r) for r in statrecs]
 write_outrecs(fileout,outrecs)
