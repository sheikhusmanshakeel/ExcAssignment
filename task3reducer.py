#!/usr/bin/env python

import sys

runningTotalLine = 0
runningTotalWords = 0

for line in sys.stdin:
    lineLength, wordsLength = line.split('\t')
    runningTotalLine += int(lineLength)
    runningTotalWords += int(wordsLength)

print("{0}\t{1}".format(runningTotalWords, runningTotalLine))
