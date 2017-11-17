#!/usr/bin/env python

import sys

previousColumnNumber = -1
matrixRow = []
firstPass = 1
lastRowToPrint = 1
while 1:
    line = sys.stdin.readline()
    if not line:
        break
    else:
        columnNumber, row, value = line.strip().split('\t')
        if int(columnNumber) == previousColumnNumber:
            matrixRow.insert(int(row), value)
            lastRowToPrint = 1
        else:
            previousColumnNumber = int(columnNumber)
            if firstPass == 1:
                firstPass = 0
                matrixRow.insert(int(row), value)
            else:
                str = ''
                for printCount in range(0,len(matrixRow)):
                    str += matrixRow[printCount] + '\t'
                print(str)
                lastRowToPrint = 0
                matrixRow = []
                matrixRow.insert(int(row), value)

if lastRowToPrint == 1:
    for printCount in range(0,len(matrixRow)):
        str += matrixRow[printCount] + '\t'
    print (str)

