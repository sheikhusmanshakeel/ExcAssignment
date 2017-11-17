#!/usr/bin/env python

import sys

previousColumn = -1
matrixDictionary = {}
maxBufferSize = 500
numberOfOverFlows = 0
intermediateMatrixRow = ""




def PrintTemporaryMatrixStrings(rowIndex):
    print("{0}\t{1}".format(rowIndex, intermediateMatrixRow))


for line in sys.stdin:
    columnNumber, row, value = line.strip().split('\t')
    columnNumber = int(columnNumber)
    row = int(row)
    if columnNumber != previousColumn:
        if previousColumn != -1:
            for j in matrixDictionary.keys():
                intermediateMatrixRow += matrixDictionary[j] + '  '
            PrintTemporaryMatrixStrings(columnNumber -1)
            intermediateMatrixRow = ""
            numberOfOverFlows = 0
        previousColumn = columnNumber
        matrixDictionary.clear()
        matrixDictionary[int(row)-maxBufferSize*numberOfOverFlows] = value
    else:
        if row-maxBufferSize*numberOfOverFlows >= maxBufferSize:
            for j in matrixDictionary.keys():
                intermediateMatrixRow += matrixDictionary[j] + '  '
            #print(intermediateMatrixRow)
            matrixDictionary.clear()
            numberOfOverFlows += 1
            #print(numberOfOverFlows)
        matrixDictionary[int(row)-maxBufferSize*numberOfOverFlows] = value

if columnNumber == previousColumn:
    for j in matrixDictionary.keys():
        intermediateMatrixRow += matrixDictionary[j] + '  '
    PrintTemporaryMatrixStrings(columnNumber)
