# coding=utf-8
""" make_md_0a.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

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

def adjust_linef(m):
 x = m.group(1)
 # {@-giri, -parvata,@}  -> {@-giri,@} {@-parvata,@}
 y = x.replace(', -', ',@} {@-')
 # restore {@ and @}
 z = '{@%s@}' % y
 return z

def adjust_line(line):
 if line.startswith(('<L>', '<LEND>')):
  return line
 newline = re.sub(r'{@(.*?)@}',adjust_linef,line)
 return newline

def test_adjust():
  line = '{@-giri, -parvata,@}'
  newline = adjust_line(line)
  print('test_adjust: %s  ->  %s' %(line,newline))
  exit(1)
  
def adjust_lines(lines):
 #test_adjust()  # debug

 newlines = []
 n = 0 # number of lines adjusted
 for iline,line in enumerate(lines):
  newline = adjust_line(line)
  if newline != line:
   n = n + 1
  newlines.append(newline)
 print(n,"lines changed")
 return newlines


if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt
 fileout = sys.argv[2] # xxx.txt adjusted

 lines = read_lines(filein)
 newlines = adjust_lines(lines)
 write_lines(fileout,newlines)
