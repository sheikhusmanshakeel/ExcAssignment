#!/usr/bin/env python

import sys

lineCount = 0
while 1:
    # remove leading and trailing whitespace
    line = sys.stdin.readline().strip()
    if not line:
        break
    else:
        print("{0}\t{1}".format(lineCount, line))
        lineCount += 1
