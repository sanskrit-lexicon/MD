# coding=utf-8
""" markup.py
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Tip(object):
 def __init__(self,line):
  # 'abst.	= abstract.'
  regex0 = '\t= '
  self.abbrev,self.tip = re.split(regex0,line)
  ## regex used for marking abbreviation
  if self.abbrev in ('+','±','&','&c.','√'):
   # the general method below does not work for these.
   # due to the peculiarities of '\b' in regex.
   regexraw = r' %s' % self.abbrev
   replacement = ' <ab>%s</ab>' % self.abbrev
  else:
   regexraw = r'\b%s' % self.abbrev
   replacement = '<ab>%s</ab>' % self.abbrev
  regexraw = regexraw.replace('+','[+]')
  regexraw = regexraw.replace('.','[.]')
  regex = re.compile(regexraw)
  self.regexraw = regexraw
  self.regex = regex
  self.replacement = replacement
 
def init_abbrevs(filein):
 lines = read_lines(filein)
 recs = [Tip(line) for line in lines]
 print(len(recs),"abbreviations read from",filein)
 d = {}
 for rec in recs:
  abbrev = rec.abbrev
  if abbrev in d:
   print('init_abbrev: unexpected duplicate',abbrev)
  d[abbrev] = rec
 return recs,d

def get_metafield(f,meta):
 if f == 'k2':
  if '<h>' in meta:
   regex = r'<%s>(.*?)<' % f
  else:
   regex = r'<%s>(.*?)$' % f
 else:
  regex = r'<%s>(.*?)<' % f
 m = re.search(regex,meta)
 value = m.group(1)
 return value


def hwdiffs(cdsl_lines,ab_lines):
 cdsl_metas = [line for line in cdsl_lines if line.startswith('<L>')]
 ab_metas = [line for line in ab_lines if line.startswith('<L>')]
 print('cdsl has %s entries' % len(cdsl_metas))
 print('ab   has %s entries' % len(ab_metas))
 assert len(cdsl_metas) == len(ab_metas)
 diffs = []
 for iline,line in enumerate(cdsl_metas):
  line1 = ab_metas[iline]
  if line != line1:
   diff = (line,line1)
   diffs.append(diff)
 print(len(diffs),"differences in metalines")
 return diffs


def write_difftext(fileout,e1s,e2s):
 outrecs = []
 n = 0
 no = 0
 for i,e1 in enumerate(e1s):
  e2 = e2s[i]
  if e1.text == e2.text:
   n = n + 1
  else:
   no = no + 1
   if no < 5:
    print(e1.metaline)
    print('cdsl text\n',e1.text)
    print()
    print('ab text\n',e2.text)
   
 print(n,'entries have same text')


def compare_tags(text1,text2,metaline):
 a1 = re.findall('<ab>.*?<?ab>',text1)
 a2 = re.findall('<ab>.*?<?ab>',text2)
 ans = []
 if a1 == a2:
  return ans 
 # diff
 n1 = len(a1)
 n2 = len(a2)
 n = max(n1,n2)
 tok = ''
 for i in range(0,n):
  if i < n1:
   x1 = a1[i]
  else:
   x1 = 'None'
   a1.append(x1)
  if i < n2:
   x2 = a2[i]
  else:
   x2 = 'None'
   a2.append(x2)
  if (x1 != x2) and (x2 == '<ab>v. l.</ab>'):
   meta = re.sub(r'<k2>.*$','',metaline)
   outarr = []
   outarr.append('--------')
   outarr.append(meta)
   i1 = max(i - 5,0)
   for j in range(i1,i):
    outarr.append('%s %s' %(j+1,a1[j]))
   outarr.append('%s: %s  !=  %s' %(i+1,x1,x2))
   ans = outarr
   return ans
 # ever executed?
 return ans

def compare(entries1,entries2,maxdiff):
 nd = 0
 ntag = 0
 tagtype = None
 tag = 'ls'
 #tagtype='n'
 outrecs = []
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  text1 = ' '.join(e1.datalines)
  text2 = ' '.join(e2.datalines)
  # next exits on diff
  ans = compare_tags(text1,text2,e1.metaline)
  if ans != []:
   outrecs.append(ans)
   if maxdiff != None:
    if len(outrecs) > maxdiff:
     break
 return outrecs

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

def compare_hws(entries1,entries2):
 nd = 0
 ntag = 0
 tagtype = None
 tag = 'ls'
 #tagtype='n'
 for ientry,e1 in enumerate(entries1):
  e2 = entries2[ientry]
  if e1.metaline == e2.metaline:
   continue
  print('metaline diff:')
  print('#1: %s' %(e1.metaline))
  print('#2: %s' %(e2.metaline))
  exit(1)
def init_premark(filein):
 lines = read_lines(filein)
 d = {}
 for line in lines:
  m = re.search(r'<L>(.*?)<pc>',line)
  if m != None:
   L = m.group(1)
   d[L] = True
 return d

def marklines(lines,d):
 newlines = []
 for line in lines:
  m = re.search(r'<L>(.*?)<pc>',line)
  if m == None:
   newline = line
  else:
   L = m.group(1)
   if L in d:
    newline = '* ' + line
   else:
    newline = line
  newlines.append(newline)
 return newlines

def write(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def sort_recs(recs):
 recs1 = sorted(recs,key = lambda rec: len(rec.abbrev),reverse=True)
 if True: # dbg
  for i,r in enumerate(recs1):
   print(r.abbrev)
   if i == 5:
    break
 return recs1

def markline_rec(line,rec):
 regex = rec.regex
 replacement = rec.replacement
 parts = re.split(r'(<ab.*?>.*?</ab>)|(<lbinfo.*?>)|(<lang.*?>.*?</lang>)|(<LB>)',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  if part.startswith(('<ab','<lbinfo','<lang','<LB>')):
   newpart = part
  else:
   try:
    newpart = re.sub(regex,replacement,part)
   except:
    print('markline_rec. regex="%s", replacement="%s"' %(regex,replacement))
    print(line)
    exit(1)
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline

def markline_recs(line,recs):
 newline = line
 for irec,rec in enumerate(recs):
  newline = markline_rec(newline,rec)
 return newline

def merge_lines(lines):
 mergelines = []
 inentry = False
 bodylines = None
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   mergelines.append(line)
   inentry = True
   bodylines = []
  elif line.startswith('<LEND>'):
   mergeline = '<LB>'.join(bodylines)
   mergelines.append(mergeline)
   mergelines.append(line)
   bodylines = None # ? needed
   inentry = False
  elif not inentry:
   mergelines.append(line)
  #elif line.startswith('[Page'):
  # newline = line
  else:
   bodylines.append(line)
 return mergelines

def unmerge_lines(lines):
 newlines = []
 for line in lines:
  a = line.split('<LB>')
  for x in a:
   newlines.append(x)
 return newlines

def marklines(lines,recs):
 newlines = []
 inentry = False
 for iline,line in enumerate(lines):
  if line.startswith('<L>'):
   newline = line
   inentry = True
  elif line.startswith('<LEND>'):
   newline = line
   inentry = False
  elif not inentry:
   newline = line
  elif line.strip() == '':
   newline = line
  elif line.startswith('[Page'):
   newline = line
  else:
   newline = markline_recs(line,recs)
  newlines.append(newline)
 return newlines

def test(fileout,recs):
 outarr = []
 for rec in recs:
  out = '%s :: %s :: %s' %(rec.abbrev,rec.regexraw,rec.replacement)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)
 # exit(1)
 
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # File with abbreviations
 fileout = sys.argv[3] # revised xxx.txt
 lines = read_lines(filein)
 print(len(lines),"lines from",filein)
 recs,d = init_abbrevs(filein1)
 # sort recs by decreasing length of abbreviation
 recs1 = sort_recs(recs)
 test('temp_markup_abbrev.txt',recs)
 lines1= merge_lines(lines)
 lines2 = marklines(lines1,recs1)
 newlines = unmerge_lines(lines2)
 write(fileout,newlines)
 

