# coding=utf-8
""" xmltags.py
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

def write_tags_helper(d):
 keys = d.keys()
 outarr = []
 keys = sorted(keys)
 for key in keys:
  count = d[key]
  outarr.append('%s %s' %(key,count))
 return outarr

def write_tags(fileout,d):
 outarr = write_tags_helper(d)
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

def count_tags(lines):
 d = {}
 newlines = []
 for line in lines:
  if line.startswith(('<L>','<LEND>')):
   continue # not interested in these
  tags = re.findall(r'<[^>]*>',line)
  for tag in tags:
   if tag.startswith('</'):
    # skip closing tags
    continue
   m = re.search(r'<([^ ]*)(.*)>',tag)
   name = m.group(1)
   attrib = m.group(2)
   if attrib != '':
    tag = '<%s-LOCAL>' % name
   if tag not in d:
    d[tag] = 0
   d[tag] = d[tag] + 1
 return d

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt 
 fileout = sys.argv[2] # xml tags with counts
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 tagdict = count_tags(lines)
 write_tags(fileout,tagdict)
 

