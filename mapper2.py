#!/usr/bin/env python

import sys

lineCount = 0
while 1:
    # remove leading and trailing whitespace
    line = sys.stdin.readline().strip()
    if not line:
        break
    else:
        sys.stdout(lineCount,line.lower())