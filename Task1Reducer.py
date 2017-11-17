#!/usr/bin/env python

import sys

word = None

while 1:
    line = sys.stdin.readline()
    if not line:
        break
    else:
        keyValue, mapperLine = line.split("\t", 1)
        value = int(keyValue)
        print(mapperLine.lower())

