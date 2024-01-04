# coding=utf-8
""" prep1a_subhw_inverse.py
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
  self.pfx = m.group(4)
  self.sfx2 = m.group(5) # slp1
  self.cpd = m.group(6)
  self.mw = m.group(7) # Y or N
  assert self.mw in ('Y','N')

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
   k2 = m.group(3)
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
   # iast versions of pfx and cpd
   if rec.pfx == rec.k1:
    pfx1 = k2
    cpd1 = k2 + '-' + rec.sfx1
   else:
    pfx1 = transcoder.transcoder_processString(rec.pfx,'slp1','roman')
    cpd1 = transcoder.transcoder_processString(rec.cpd,'slp1','roman')
    # pfx1 = pfx1 + '?'
    cpd1 = cpd1 + '?'
   newlines.append(';; subhw %s:%s:%s + %s -> %s' % (isubhw,rec.mw,pfx1,rec.sfx1,cpd1))
   #newlines.append(rec.line)
   subhwpart = subhwparts[irec]
   newlines.append('<H2> ' + subhwpart)
 return newlines

def edit_lines(lines):
 newlines = []
 for iline,line in enumerate(lines):
  if line.startswith(';;'):
   continue # skip
  newline = re.sub(r'^<H[234]> +','',line)
  newlines.append(newline)
 return newlines

def join_datalines(lines):
 newlines = []
 inentry = False
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   newlines.append(line)
   inentry = True
   datalines = []
   continue
  if not inentry:
   newlines.append(line)
   continue
  if line.startswith('<LEND>'):
   newline = ''.join(datalines)
   newlines.append(newline)
   newlines.append(line)
   inentry = False
   continue
  datalines.append(line)
 return newlines
if __name__=="__main__":
 filein = sys.argv[1] # intermediate version of xxx.txt
 fileout = sys.argv[2] # xxx.txt
 lines = read_lines(filein)  # md.txt
 # restore the 'one-line' form
 newlines = edit_lines(lines)
 newlines1 = join_datalines(newlines)
 write_lines(fileout,newlines1)
 exit(1)
