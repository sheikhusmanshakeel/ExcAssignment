#!/usr/bin/env python

import sys
# logic is to push out all student records and marks records by student id
# so that all the records for one particular student are collected by the same reducer.
# The reducer can then generate the output by collecting the results
# Since different mappers might start reading the file at different locations, this collection can't be done in the mapper
while 1:
    # remove leading and trailing whitespace
    line = sys.stdin.readline().strip()
    if not line:
        break
    else:
        tokens = line.split()
        if len(tokens) == 3:
            # push out the student record, student id first.
            print("{0}\t{1}".format(tokens[1], tokens[2]))
        else:
            # push out the marks record, student id first.
            print("{0}\t{1}\t{2}".format(tokens[2], tokens[1], tokens[3]))
