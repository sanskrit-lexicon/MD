"""
 ScharfSandhiArg.py  May 25, 2015
 Jul 26, 2015. 
 Jul 27, 2015
 9 May 2020 PMS added parenthesis for python 3 compatibility
"""
from scharfsandhi import ScharfSandhi

if __name__ == '__main__':
 import sys
 ec = sys.argv[1]
 despace = sys.argv[2]
 s = sys.argv[3]
 sandhi = ScharfSandhi()
 sandhi.history=[] # init history.  It is modified by wrapper
 sandhi.dbg=True
 err = sandhi.sandhioptions(ec, "N", "S", despace)
 if err != 0:
  print("ERROR: options must be E or C, Y or N, not:", ec, despace)
  exit(1)
 ans = sandhi.sandhi(s)
 for h in sandhi.history:
  print(h)
 print('ScharfSandhiArg: ans="%s"' % ans)
