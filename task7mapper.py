#!/usr/bin/env python

import sys
#file = open('/home/raven/matrixSmall.txt','r')
while 1:
    line = sys.stdin.readline().strip()
    if not line:
        break
    else:
        rowIndex, columns = line.strip().split('\t')
        tokens = columns.strip().split('  ')
        for columnIndex in range(0,len(tokens)):  # write the results to standard output
            print("{0}\t{1}\t{2}".format(columnIndex, rowIndex, tokens[int(columnIndex)]))
#file.close()
