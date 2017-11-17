#!/usr/bin/env python

import sys
lineTotal = 0
mapTotal = 0
for line in sys.stdin:
    line = line.strip('\n')
    tokens = line.split()
    mapTotal += len(tokens)
    lineTotal += 1


print("{0}\t{1}".format(lineTotal,mapTotal))
