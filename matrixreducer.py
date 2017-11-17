#!/usr/bin/env python

import sys

previousColumnNumber = -1
matrixRow = []
firstPass = 1
lastRowToPrint = 1
for line in sys.stdin:
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
            for printCount in range(0, len(matrixRow)):
                print(matrixRow[printCount])
            matrixRow = []
            matrixRow.insert(int(row), value)


    for printCount in range(0, len(matrixRow)):
        print(matrixRow[printCount])
