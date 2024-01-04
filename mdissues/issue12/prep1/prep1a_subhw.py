# coding=utf-8
""" prep1a_subhw.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  
sys.path.insert(0,'../')
import transcoder
#    k2b = transcoder.transcoder_processString(k2alow,tranin,tranout)
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

class Prep1acpd_unused:
 def __init__(self,line):
  # consistent with outarr_rec of prep1a_cpd.py
  #  out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s<cpd>%s' %(
  #  rec.L, rec.k1, rec.sfx1, rec.pfx, rec.sfx2, rec.cpd)
  self.line = line
  m = re.search(r'^<L>(.*?)<k1>(.*?)<sfx1>(.*?)<pfx>(.*?)<sfx2>(.*?)<cpd>(.*)$',
                line) 
  self.L = m.group(1)
  self.k1 = m.group(2)
  self.sfx1 = m.group(3) # iast
  self.pfx = m.group(4)
  self.sfx2 = m.group(5) # slp1
  self.cpd = m.group(6)
  self.mw = None
def init_prep1a_cpd_unused(filein):
 lines = read_lines(filein)
 recs = [Prep1acpd(line) for line in lines]
 print(len(recs),"records at init_prep1a")
 return recs

class Prep1a_cpd_mw:
 def __init__(self,line):
  # consistent with outarr_rec of prep1a_cpd_mw.py
  #  out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s<cpd>%s' %(
  
  self.line = line
  m = re.search(r'^<L>(.*?)<k1>(.*?)<sfx1>(.*?)<pfx>(.*?)<sfx2>(.*?)<cpd>(.*?)<mw>(.*)$',
                line) 
  self.L = m.group(1)
  self.k1 = m.group(2)
  self.sfx1 = m.group(3) # iast
  self.pfx = m.group(4)  # slp1
  self.sfx2 = m.group(5) # slp1
  self.cpd = m.group(6)
  self.mw = m.group(7) # Y or N
  assert self.mw in ('Y','N')

 def get_pfx1_cpd1(self,k2a):
  # k2a is k2 (iast) of the parent headword
  pfx1 = transcoder.transcoder_processString(self.pfx,'slp1','roman')
  self.pfx1 = pfx1
  cpdiast = transcoder.transcoder_processString(self.cpd,'slp1','roman')
  # recognize various sandhis
  if self.pfx1.endswith(('a','ā')) and self.sfx1.startswith(('a','‿a','ā','‿ā','u')):
   self.cpd1 = cpdiast
   return
  if self.pfx1.endswith('i') and self.sfx1.startswith(('i','‿i','ī')):
   self.cpd1 = cpdiast
   return
  if self.pfx1.endswith('u') and self.sfx1.startswith(('u','‿u','ū')):
   self.cpd1 = cpdiast
   return
  if self.pfx1.endswith('i') and self.sfx1.startswith(('a','ā','u','ū')):
   self.pfx1 = re.sub(r'i$','y',self.pfx1)
   self.cpd1 = self.pfx1 + '-' + self.sfx1
   return
  if self.pfx1.endswith('u') and self.sfx1.startswith(('a','ā','u','ū','i','ī')):
   self.pfx1 = re.sub(r'u$','v',self.pfx1)
   self.cpd1 = self.pfx1 + '-' + self.sfx1
   return
  
  if self.pfx == self.k1:  # slp1 comparison
   # the compound has k1 as prefix
   self.cpd1 = self.pfx1 + '-' + self.sfx1 # iast
   return
  if (self.pfx1 + self.sfx1) == cpdiast:
   self.cpd1 = self.pfx1 + '-' + self.sfx1
   return                          
  # take into account accents
  self.sfx1a = drop_accent1_iast(self.sfx1).replace('-','')
  self.pfx1a = drop_accent1_iast(self.pfx1)
  if (self.pfx1a + self.sfx1a) == cpdiast:
   self.cpd1 = self.pfx1 + '-' + self.sfx1
   return
    
  # fail
  self.cpd1 = self.pfx1 + '-' + self.sfx1
  self.cpd1 = self.cpd1.replace('ā-ṛ','ār')
  self.cpd1 = self.cpd1.replace('a-i','e')
  self.cpd1 = self.cpd1.replace('ā-ī','e')
  self.cpd1 = self.cpd1.replace('ā-i','e')
  self.cpd1 = self.cpd1.replace('a-ī','e')
  self.cpd1 = self.cpd1.replace('a‿a','ā')
  self.cpd1 = self.cpd1.replace('a‿u','o')
  self.cpd1 = self.cpd1.replace('ā‿ā','ā')
  self.cpd1 = self.cpd1.replace('a‿e','ai')
  self.cpd1 = self.cpd1.replace('ā‿e','ai')
  self.cpd1 = self.cpd1.replace('a‿o','au')
  self.cpd1 = self.cpd1.replace('ā‿o','au')
  if self.mw == 'N':
   self.cpd1 = self.cpd1 + '?'
  return
  
  parts = k2a.split('-')
  if len(parts) == 2:
   if parts[0:1] == pfx1:    
    cpd1 = self.pfx1 + '-' + rec.sfx1 # iast
    cpdtst = cpd1.replace('-','')
    if cpdtst == cpdiast:
     self.cpd1 = cpd1
     return
    else:
     if (self.L == '19') and True:print('cpdtst=',cpdtst)
  if (self.L == '19') and True: # dbg
   print('check rec:',self.line)
   print('k2a=',k2a,'cpdiast=',cpdiast)
   print(parts)
   #exit(1)
  self.cpd1 = cpdiast + '?'
  return
  # code not yet right.
  for ipart,part in enumerate(parts[0:-1]):
   pfxtst = '-'.join(parts[0:ipart+1])
   cpdtst = pfxtst + '-' + self.sfx1
   cpdcmp = cpdtst.replace('-','')
   if cpdcmp == cpdiast:
    pass

def drop_accent1_slp1(x):
 # x is slp1
 x = x.replace('/','')
 x = x.replace('\\','')
 x = x.replace('^','')
 # also, karma‿anta -> karma-anta  
 #x = x.replace('‿', '-')
 return x 

def drop_accent1_iast(x):
 # x is iast
 y = transcoder.transcoder_processString(x,'roman','slp1')
 z = drop_accent1_slp1(y)
 w = transcoder.transcoder_processString(z,'slp1','roman')
 return w

def init_prep1a_cpd_mw(filein):
 lines = read_lines(filein)
 recs = [Prep1a_cpd_mw(line) for line in lines]
 print(len(recs),"records at init_prep1a_cpd_mw")
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

def make_rec_groups(recs):
 groups = list(group_by_L(recs))
 d = {} # access by L
 for group in groups:
  rec = group[0]
  L = rec.L
  d[L] = group
 print('%s groups' % len(groups))
 return groups,d

def line_parse(line,L):
 parts = re.split(r'({@-.*?,?@})',line)
 if (L == '730') and False:  # debugging
  for ipart,part in enumerate(parts):
   ipart1 = ipart # + 1
   print('line_parse %02d: %s' %(ipart1,part))
 hwpart = parts[0]
 subhwparts = []
 partsa = parts[1:]
 for ipart,parta in enumerate(partsa):
  if (ipart % 2) == 0:
   subhwpart = partsa[ipart] + partsa[ipart+1]
   subhwparts.append(subhwpart)
 return hwpart,subhwparts

def get_newlines(lines,gdict):
 nprob = 0  # cannot find k2
 newlines = []
 entryflag = False
 subflag = False  # substantive?
 for iline,line in enumerate(lines):
  if line.startswith('<L>'): # metaline
   m = re.search(r'<L>([^<]*).*?<k1>([^<]*)<k2>(.*?)<',line)
   L = m.group(1)
   k1 = m.group(2)
   k2 = m.group(3) # slp1
   newlines.append(line)
   entryflag = True
   subflag = line.endswith('<e>S')
   continue
  if line.startswith('<LEND>'):
   newlines.append(line)
   entryflag = False
   continue
  if not entryflag:
   newlines.append(line)
   continue
  # line is now the 'data line' of an entry
  # Check that this is a substantive with subheadwords
  if not subflag:
   newlines.append(line)
   continue
  hwpart,subhwparts = line_parse(line,L)
  if subhwparts == []:
   # no compounds
   newlines.append(line)
   continue
  # generate new entry lines
  if L not in gdict:
   print('ERROR: %s has no subheadwords' % L)
   exit(1)
  group = gdict[L]
  if len(subhwparts) != len(group):
   print('ERROR: subhwparts incompatible with group. L=',L)
   print(' subhwparts count = %s, group count = %s' %(len(subhwparts) , len(group)))
   for i,subhwpart in enumerate(subhwparts):
    print('%02d: %s' %(i+1,subhwpart))
   exit(1)
  newlines.append(hwpart)
  for irec,rec in enumerate(group):
   isubhw = irec + 1
   k2a = transcoder.transcoder_processString(k2,'slp1','roman')
   rec.get_pfx1_cpd1(k2a)
   newlines.append(';; subhw %s:%s:%s + %s -> %s' % (isubhw,rec.mw,rec.pfx1,rec.sfx1,rec.cpd1))
   subhwpart = subhwparts[irec]
   newlines.append('<H2> ' + subhwpart)
 return newlines
 
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # prep1a_edit_status.txt
 fileout = sys.argv[3] # intermediate version of xxx.txt
 lines = read_lines(filein)  # md.txt
 recs = init_prep1a_cpd_mw(filein1)
 groupa,groupsdict = make_rec_groups(recs)
 #
 newlines = get_newlines(lines,groupsdict)
 write_lines(fileout,newlines)
 exit(1)
