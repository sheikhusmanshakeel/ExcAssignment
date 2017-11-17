#!/usr/bin/env python

import sys


previousColumn = -1
matrixDictionary = {}
maxBufferSize = 5
intermediateMatrixRow = ""

def PrintMatrix(unsortedRow, rowIndex):
    row = ""
    sortedDict = dict(sorted(unsortedRow.items()))
    for j in sortedDict.keys():
        row += sortedDict[j] + '  '
    print("{0}\t{1}".format(rowIndex,row))


for line in sys.stdin:
    columnNumber, row, value = line.strip().split('\t')
    columnNumber = int(columnNumber)
    #print(columnNumber)
    if columnNumber != previousColumn:
        if previousColumn != -1:
            PrintMatrix(matrixDictionary, columnNumber-1)
        previousColumn = columnNumber
        matrixDictionary.clear()
        matrixDictionary[int(row)] = value
    else:
        matrixDictionary[int(row)] = value


if columnNumber == previousColumn:
    PrintMatrix(matrixDictionary,columnNumber)
