#!/usr/bin/env python

import sys

currentLine = ""
previousLine = ""

for line in sys.stdin:
    currentLine = line
    #currentLine = line
    if currentLine != previousLine:
        if previousLine:
            print(previousLine.strip('\n'))
        previousLine = currentLine

if currentLine == previousLine:
    print(currentLine.strip('\n'))
