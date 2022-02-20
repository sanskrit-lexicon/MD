#-*- coding:utf-8 -*-
"""slp1iast.py
   Module to read slp1_iast.txt from a file, and parse the lines
   into a list of SLP1IAST
"""
from __future__ import print_function
import sys, re,codecs

class SLP1IAST(object):
 Ldict = {}
 def __init__(self,line):
  # line has following structure:
  # 2 parts, separated by tab
  a,self.doc = line.split('\t')
  # part a has 3 parts according to this regex:
  #  slp1, iast and capitalized iast (in parentheses)
  m = re.search(r'^([^ ]+) ([^ ]+) \( (.*) \)$',a)
  self.slp1 = m.group(1)
  self.iast = m.group(2)
  self.iastcap = m.group(3)
 
def init(filein):
 recs=[]  # list of SLP1IAST objects, to be returned
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  for line in f:
   line = line.rstrip('\r\n') # remove line-ending character(s)
   rec = SLP1IAST(line) # parse line and get object
   recs.append(rec)  # add this record
 print(len(recs),"SLP1IAST records read from",filein)
 return recs

def count_various(recs):
 # list comprehension
 crecs = [rec for rec in recs if 'CIRCUMFLEX' in rec.doc]
 print(len(crecs),"Records have CIRCUMFLEX in the documentation string")
 # we can define a function WITHIN another function!
 def isvowel(rec):
  # rec.slp1 starts with one of the slp1 vowel letters
  #slp1vowels = 'aAiIuUfFxXeEoO'
  if re.search(r'^[aAiIuUfFxXeEoO]',rec.slp1):
   return True
  else:
   return False
 # filter on the vowel records
 vowelrecs = [rec for rec in recs if isvowel(rec)]
 print(len(vowelrecs),"vowel records")
 # vowel records whose iast has circumflex
 cvowels = [rec for rec in vowelrecs if rec in crecs]
 print(len(cvowels),"vowel records with iast circumflex")
 
if __name__=="__main__":
 # test program.
 # This code does not run when another program imports slp1iast module
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 recs = init(filein)
 count_various(recs) 
