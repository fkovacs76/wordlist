import random
import sys

fh = open("final.txt",'r')
ll = fh.readlines()
for i in range(1,100):
    s = ll[random.randrange(1,len(ll))]
    ss = s.strip('\n')
    sss = ss.strip('\r')
    sys.stdout.write(sss)
    sys.stdout.write(",")

