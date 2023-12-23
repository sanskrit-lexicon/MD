# coding=utf-8
""" correct_pe.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)
 
def correct_pe(lines):
 newlines = []
 nchg = 0
 for line in lines:
  if line.startswith(('<L>','<LEND>')):
   newlines.append(line)
  else:
   # correct <pe>X<pe>
   newline = re.sub(r'<pe>([^<]*)<pe>', r'<pe>\1</pe>',line)
   # correct <cl>1.</cl>
   newline = newline.replace('<cl>1.</cl>', '<cl>I.</cl>')
   # another error
   newline = newline.replace('<ab>A.</ab>', '<lex>Ā.</lex>')
   # change <cl>V.</cl> (class 5 root) to avoid conflict
   # with '<ab>V.</ab>' (Vedic)
   newline = newline.replace('<cl>V.</cl>', '<cl>ᴠ.</cl>')
   newlines.append(newline)
   if newline != line:
    nchg = nchg + 1
 print(nchg,'lines changed')
 return newlines

def write(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt 
 fileout = sys.argv[2] # revised xxx.txt
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 newlines = correct_pe(lines)
 write(fileout,newlines)
 

