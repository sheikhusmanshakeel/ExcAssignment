#!/usr/bin/env python
import sys

studentName = ''
studentCourseRecord = ''
previousStudentId = -1
currentStudentId = -1
#file = open('/home/raven/uniSmallOutputSorted','r')
for line in sys.stdin:  # For ever line in the input from stdin
    records = line.strip().split('\t')
    # Collection from mapper can be done here
    # Hadoop will sort on student id, so we are sure everything pertaining to a particular student will be received here
    currentStudentId = int(records[0])
    if previousStudentId != -1:
        if len(records) == 3:
            # Student marks record is received
            if previousStudentId == currentStudentId:
                studentCourseRecord += " ({0},{1})".format(records[1], records[2])
            else:  # New student is received
                # print the old record and start building the new one
                print("{0}-->{1}".format(studentName, studentCourseRecord))
                studentCourseRecord = " ({0},{1})".format(records[1], records[2])
            previousStudentId = currentStudentId
        else:
            # This means a student name record is received
            # If a new student is found, print the old one and start building the new one
            # Since task is to do inner join, programme will not print a student with no marks records
            # For example, if two student name records come in consecutively, the first one will be lost
            # otherwise this will become left outer join instead of inner join
            if previousStudentId != currentStudentId:
                # print the old record and start building the new one
                print("{0}-->{1}".format(studentName, studentCourseRecord))
            previousStudentId = currentStudentId
            studentName = records[1]
    else:
        previousStudentId = currentStudentId
        if len(records) == 2:
            studentName = records[1]
        else:
            studentCourseRecord = " ({0},{1})".format(records[1], records[2])

# print the last student record
if previousStudentId == currentStudentId:
    print("{0}-->{1}".format(studentName, studentCourseRecord))

#file.close()