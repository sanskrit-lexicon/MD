# coding=utf-8
""" compare_metalines.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

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

def write_hwdiffs(fileout,diffs):
 outrecs = []
 for idiff,diff in enumerate(diffs):
  outarr = []
  cdsl,abv1 = diff
  idiff1 = idiff + 1
  outarr.append('; Case %s' % idiff1)
  outarr.append('cdsl: %s' % cdsl)
  outarr.append('abv1: %s' % abv1)
  outarr.append('; ------------------------------------')
  outrecs.append(outarr)
 write_outrecs(fileout,outrecs)
  
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
 regex = r'\b%s' % rec.abbrev
 regex = regex.replace('+','[+]')
 regex = regex.replace('.','[.]')
 replacement = '<ab>%s</ab>' % rec.abbrev
 #parts = re.split(r'(<ab>.*?</ab>)|(<lbinfo.*?>)',line)
 parts = re.split(r'(<ab.*>.*?</ab>)|(<lbinfo.*?>)|(<lang.*?>.*?</lang>)',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  if part.startswith(('<ab','<lbinfo','<lang')):
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

def make_newlines(lines):
 circle = '🞄'  # 01F784 'Black Slightly Small Circle'
 newlines = []
 for line in lines:
  if line.startswith(('<L>','<LEND>')):
   newlines.append(line)
  else:
   # correct <pe>X<pe>
   line = re.sub(r'<pe>([^<]*)<pe>', r'<pe>\1</pe>',line)
   parts = line.split(circle)
   for part in parts:
    newlines.append(part)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt
 filein1 = sys.argv[2] # another version of xxx.txt
 fileout = sys.argv[3] # metaline differences
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 lines1 = read_lines(filein1)
 print(len(lines1),"lines read from",filein1)
 diffs = hwdiffs(lines,lines1)
 write_hwdiffs(fileout,diffs)
 

