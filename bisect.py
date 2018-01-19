#!/usr/bin/python
import bisect
import random 

random.seed(1)

l = []
for i in range(1, 20): 
    r = random.randint(1, 1000)
    position = bisect.bisect(l, r)
    bisect.insort(l,r)
    print ("%2d %2d") % (r, position), l
