#-*- coding:utf-8 -*-
"""prep1a_cpd.py
"""
from __future__ import print_function
import sys, re,codecs
sys.path.insert(0,'../sandhi/')
from scharfsandhi import ScharfSandhi
sandhi = ScharfSandhi()
sandhi.sandhioptions('C','N','S',' ')
def test():
 sandhi.sandhioptions('E','N','S',' ')
 old = 'rAmaH gacCati'
 new = sandhi.sandhi(old)
 print('%s -> %s' %(old,new))
 #
 sandhi.sandhioptions('C','N','S',' ')
 old = 'deva-arjuna'
 new = sandhi.sandhi(old)
 print('%s -> %s' %(old,new))
 exit(1)

# test()

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

class Prep1aslp1:
 def __init__(self,line):
  # consistent with outarr_rec of prep1a_slp1.py
  self.line = line
  m = re.search(r'^<L>(.*?)<k1>(.*?)<sfx1>(.*?)<pfx>(.*?)<sfx2>(.*?)$',
                line) 
  self.L = m.group(1)
  self.k1 = m.group(2)
  self.sfx1 = m.group(3) # iast
  self.pfx = m.group(4)
  self.sfx2 = m.group(5) # slp1
  self.cpd = None
  
def init_prep1a_slp1(filein):
 lines = read_lines(filein)
 recs = [Prep1aslp1(line) for line in lines]
 print(len(recs),"records at init_prep1a")
 return recs

def drop_accent(x):
 x = x.replace('/','')
 x = x.replace('\\','')
 x = x.replace('^','')
 # also, karma‿anta -> karma-anta  
 x = x.replace('‿', '-')
 return x 

cpd_exceptions = {
  'asTan-vat' : 'asTanvat', # asTavat per sandhi
  'aviSvas-anIya' : 'aviSvasanIya',
  'aTarvANgiras-a' : 'aTarvANgirasa',
  'madan-Iya' : 'madanIya',
  'aDvan-Ina' : 'aDvanIna',
  'anAtman-Ina' : 'anAtmanIna',
  'an-AramB-a' : 'anAramBa',
  'anudD-fta' : 'anudDfta',
  'anul-laNG-anIya' : 'anullaNGanIya',
  'adrivat-vas' : 'adrivat<sfx2>vas',
  'aDas-pat' : 'aDaspat',
  'an-udD-fta' : 'anudDfta',
   'ayAs-ya' : 'ayAsya',
   'arakz-ya' : 'arakzya',
   'aram-kAmAya' : 'araMkAmAya',
   'aruc-ya' : 'arucya',
   'arTa-saMc-aya' : 'arTasaMcaya',
   'arDa-niz-panna' : 'arDanizpanna',
   'arD-in' : 'arDin',
   'arp-ita' : 'arpita',
   'alaMkar-tf' : 'alaMkartf',
   'alaNG-ayat' : 'alaNGayat',
   'alin-I' : 'alinI',
   'ava-BAs-a' : 'avaBAsa',
   'ava-BAs-a-ka' : 'avaBAsaka',
   'ava-BAs-ana' : 'avaBAsana',
   'ava-BAs-a' : 'avaBAsa',
   'avikatT-in' : 'avikatTin',
   'aSaraR-I-kf' : 'aSaraRIkf',
   'aSman-maya' : 'aSmanmaya',
   'asat-I' : 'asatI',
   'ahar-pati' : 'aharpati',
   'ahiMs-A' : 'ahiMsA',
   'Akamp-ra' : 'Akampra',
#  '' : '',
#  '' : '',
#  '' : '',
#  '' : '',
#  '' : '',
#  '' : '',
#  '' : '',
#  '' : '',
#  '' : '',
#  '' : '',
#  '' : '',
 
}

def join_concat(pfx,sfx):
 # Systematic cases were the compound is NOT formed by compound-sandhi
 if pfx.endswith('k') and sfx.startswith(('A','a','i')):
  return pfx + sfx
 # duS+c -> duSc
 if pfx.endswith('S') and sfx.startswith('c'):
  return pfx + sfx
 # duz+p -> duzp
 if pfx.endswith('z') and sfx.startswith('p'):
  return pfx + sfx
 # niH + S -> niHS
 if pfx.endswith('H') and sfx.startswith(('S','s')):
  return pfx + sfx
 # hiMs + a -> hiMsa
 if pfx.endswith('hiMs') and sfx.startswith(('a','r')):
  return pfx + sfx
 # poz + a -> poza
 if pfx.endswith('poz') and sfx.startswith('a'):
  return pfx + sfx
 # p + a -> pa
 if pfx.endswith('p') and sfx.startswith('a'):
  return pfx + sfx
 if pfx.endswith('S') and sfx.startswith(('a','i')):
  return pfx + sfx
 if pfx.endswith(('z','c')) and sfx.startswith(('a','i','k')):  # Ikz+a
  return pfx + sfx
 if pfx.endswith('D') and sfx.startswith('a'):
  return pfx + sfx
 if pfx.endswith('h'):
  return pfx + sfx
 # 
 if pfx.endswith('s') and sfx.startswith(('k','v')): # May generate some false positive 
  return pfx + sfx
 if (pfx =='SaMs') and sfx.startswith(('a','i')):
  return pfx + sfx
 if (pfx =='has') and sfx.startswith('a'):
  return pfx + sfx
 return None

def make_cpd(rec):
 sandhi.sandhioptions('C','N','S',' ') # compound sandhi
 pfx = drop_accent(rec.pfx)
 sfx = drop_accent(rec.sfx2)
 concat = join_concat(pfx,sfx)
 if concat != None:
  rec.cpd = concat.replace('-','')
  return
 # Use compound sandhi to join pfx and sfx
 old = '%s-%s' %(pfx,sfx)
 if old in cpd_exceptions:
  new = cpd_exceptions[old]
 else:
  new = sandhi.sandhi(old)
 rec.cpd = new.replace('-','')

def write_outrecs(fileout,outrecs):
 nlines = 0 # total number of lines writte
 with codecs.open(fileout,"w","utf-8") as f:
  for lines in outrecs:
   nlines = nlines + len(lines)
   for line in lines:
    f.write(line+'\n')  
 print("%s recs (%s lines) written to %s" %(len(recs),nlines,fileout))

def outarr_rec(rec):
 outarr = []
 out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s<cpd>%s' %(
   rec.L, rec.k1, rec.sfx1, rec.pfx, rec.sfx2, rec.cpd)
 outarr.append(out)
 return outarr

def write_recs(fileout,recs):
 outrecs = []
 for rec in recs:
  outarr = outarr_rec(rec)
  outrecs.append(outarr)

 write_outrecs(fileout,outrecs)


if __name__=="__main__":
 tranin = 'roman' # sys.argv[1]
 tranout = 'slp1'
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] #
 recs = init_prep1a_slp1(filein)
 
 for rec in recs:
  make_cpd(rec)  

 write_recs(fileout,recs)
