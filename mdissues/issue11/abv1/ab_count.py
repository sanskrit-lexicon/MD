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

def count_line_tag(tag,line,dabbrev,recs):
 #  since these latter also need tooltips
 # returns number of new tags in this line
 nnew = 0
 regex = r'<%s>(.*?)</%s>' %(tag,tag)
 for m in re.finditer(regex,line):
  abbrev = m.group(1)
  if abbrev not in dabbrev:
   #print('New abbreviation:',m.group(0))
   nnew = nnew + 1
   # add a new record to dabbrev
   tip = '??'
   tipline = '%s\t<id>%s</id> <disp>%s</disp>' %(abbrev,abbrev,tip)
   rec = Tip(tipline)
   rec.n = 1
   rec.tag = tag
   dabbrev[abbrev] = rec
   recs.append(rec)
  else:
   rec = dabbrev[abbrev]
   rec.n = rec.n + 1
   
 return nnew

def count(lines,dabbrev,recs):
 # modifys dabbrev and recs
 newlines = []
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
   tags = ('ab','cl','lang','lex','pe')
   for tag in tags:
    n = count_line_tag(tag,line,dabbrev,recs)
    nnew = nnew + n
 # nothing returned
 print(nnew,"new abbreviations")
 
def write_recs(fileout,recs0):
 # sort the array of Tip records by abbreviation (without case)
 recs = sorted(recs0,key = lambda rec: rec.abbrev.lower())
 outarr = []  # add a <count>N</count> field to output
 for rec in recs:
  #out = '%s :: %s :: %s' %(rec.abbrev,rec.n,rec.tip)
  if rec.tag == 'ab':
   tagnote = ''
  else:
   tagnote = ' <tag>%s</tag>' % rec.tag
  out = '%s\t<id>%s</id> <disp>%s</disp> <count>%s</count>%s' %(
   rec.abbrev, rec.abbrev, rec.tip, rec.n, tagnote)
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)
 exit(1)
 
if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 filein1 = sys.argv[2] # File with abbreviations
 fileout = sys.argv[3] # abbreviations with counts
 lines = read_lines(filein)
 print(len(lines),"lines from",filein)
 recs,d = init_abbrevs(filein1)
 count(lines,d,recs)  # modifies both d and recs
 write_recs(fileout,recs)
 

