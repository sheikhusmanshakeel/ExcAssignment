#!/usr/bin/env python

import sys
previousColumn = -1
matrixRow = []

def PrintMatrix(rowToPrint):
    row = ""
    for i in range(0,len(rowToPrint)):
        row += rowToPrint[i] + '\t'
    print(row)


for line in sys.stdin:
    columnNumber, row, value = line.strip().split('\t')
    if columnNumber != previousColumn:
        if previousColumn != -1:
            PrintMatrix(matrixRow)
        previousColumn = columnNumber
        matrixRow = []
        matrixRow.insert(int(row),value)
    else:
        matrixRow.insert(int(row),value)


if columnNumber == previousColumn:
    PrintMatrix(matrixRow)




