# coding=utf-8
""" ab_count.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Tip(object):
 def __init__(self,line):
  # format of mdab_input.txt
  # A\t<id>A</id> <disp>T</disp> , where
  # A is the abbreviation
  # \t is the tab character
  # T is the tooltip
  
  self.abbrev,self.data = line.split('\t')
  m = re.search(r'^<id>(.*?)</id> <disp>(.*?)</disp>$',self.data)
  if m == None:
   print('Tip cannot parse 1',line)
   exit(1)
  if m.group(1) != self.abbrev:
   print('Tip cannot parse 2',line)
   exit(1)
   
  self.abbrev = m.group(1)
  self.tip = m.group(2)
  self.n = 0  # observed
  self.tag = 'ab'  # 

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

def write(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def count_line_tag(tag,line,d):
 #  since these latter also need tooltips
 # returns number of new tags in this line
 regex = r'<%s>.*?</%s>' %(tag,tag)
 for m in re.finditer(regex,line):
  instance = m.group(0)
  if instance not in d:
   d[instance] = 0
  d[instance] = d[instance] + 1

def count_tag_instances(lines,tags):
 d = {}  #instances of extra tags. returned
 inentry = False
 nnew = 0  # number of new abbreviations
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
   # for this purpose, also include tags ab and also cl, lang, lex, pe
   for tag in tags:
    count_line_tag(tag,line,d)
 return d

def write_recs(fileout,recs0):
 # sort the array of Tip records by abbreviation (without case)
 recs = sorted(recs0,key = lambda rec: rec.abbrev.lower())
 outarr = []  # add a <count>N</count> field to output
 for rec in recs:
  #out = '%s :: %s :: %s' %(rec.abbrev,rec.n,rec.tip)
  out = '%s\t<id>%s</id> <disp>%s</disp> <count>%s</count> <tag>%s</tag>' %(
   rec.abbrev, rec.abbrev, rec.tip, rec.n, rec.tag)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def write_extra(fileout,dextra,d,filein1):
 instances = dextra.keys()
 instances = sorted(instances,key = lambda x : x.lower())
 outarr = []  # add a <count>N</count> field to output
 for instance in instances:
  # <X>Y</X>
  m = re.search(r'^<(.*?)>(.*?)</(.*?)>$',instance)
  tag = m.group(1)
  abbrev = m.group(2)
  endtag = m.group(3)
  assert tag == endtag
  if (abbrev in d):
   flag = '(in %s = YES)' % filein1
  else:
   flag = '(in %s = NO )' % filein1
  count = dextra[instance]
  out = '%s %s %s' %(instance,count,flag)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def compare_instances(dab,dextra):
 found = 0
 for i in dextra:
  # <T>X</T>
  m = re.search(r'^<(.*?)>(.*?)</(.*?)>$',i)
  tag = m.group(1)
  abbrev = m.group(2)
  endtag = m.group(3)
  i_ab = '<ab>%s</ab>' % tag
  if i_ab in dab:
   nab = dab[i_ab]
   found = found + 1  # an overlap
  else:
   nab = 'NOTF'
  if nab != 'NOTF':
   out = '%s (%s) | %s (%s)' % (i, dextra[i],  i_ab, nab)
   print(out)
 print(found,"abbreviations with two tags")
 
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # File with abbreviations
 fileout = sys.argv[3] # abbreviations with counts
 lines = read_lines(filein)
 print(len(lines),"lines from",filein)
 recs,d = init_abbrevs(filein1)
 extra_tags = ('cl','lang','lex','pe')
 dextra = count_tag_instances(lines,extra_tags)
 write_extra(fileout,dextra,d,filein1)

 dab = count_tag_instances(lines,('ab'))
 # look for overlap
 compare_instances(dab,dextra)
