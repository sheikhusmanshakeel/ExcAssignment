#!/usr/bin/env python

import sys
#file = open('/home/raven/task4document','r')
for line in sys.stdin:
    line = line.strip()
    if len(line) > 1:
        tokens = line.split()
        for i in range(0, len(tokens) - 1):
            word = tokens[i] + ' ' + tokens[i + 1]
            print("{0}\t{1}".format(word, 1))
#file.close()