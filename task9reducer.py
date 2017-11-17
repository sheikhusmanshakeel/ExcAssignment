#!/usr/bin/env python
import sys

currentStudentName = ''
runningTotal = 0
runningCourses = 0
previousStudentId = -1
currentStudentId = -1


#file = open('/home/raven/uniSmallOutputSorted','r')
def PrintRecord(studentName, aggregateMarks, numberOfCourses):
    if int(numberOfCourses) > 4:
        average = float(aggregateMarks) / numberOfCourses
        #print("Name : {0}\nTotalMarks : {1}\nTotal Courses: {2}\nAverage : {3}".format(studentName,aggregateMarks,numberOfCourses,average))
        print("{0}\t{1}".format(studentName, float(average)))


for line in sys.stdin:  # For ever line in the input from stdin
    records = line.strip().split('\t')
    # Collection from mapper can be done here
    # Hadoop will sort on student id, so we are sure everything pertaining to a particular student will be received here
    currentStudentId = int(records[0])
    if previousStudentId != -1:
        if len(records) == 3:
            # Student marks record is received
            if previousStudentId == currentStudentId:
                runningTotal += int(records[2])
                runningCourses += 1
            else:  # New student is received
                # print the old record and start building the new one
                PrintRecord(currentStudentName, runningTotal, runningCourses)
                runningTotal = int(records[2])
                runningCourses = 1
            previousStudentId = currentStudentId
        else:
            # This means a student name record is received
            # If a new student is found, print the old one and start building the new one
            # Since task is to do inner join, programme will not print a student with no marks records
            # For example, if two student name records come in consecutively, the first one will be lost
            # otherwise this will become left outer join instead of inner join
            if previousStudentId != currentStudentId:
                # print the old record and start building the new one
                PrintRecord(currentStudentName, runningTotal, runningCourses)
                runningCourses = 0
                runningTotal = 0
            previousStudentId = currentStudentId
            currentStudentName = records[1]
    else:
        previousStudentId = currentStudentId
        if len(records) == 2:
            currentStudentName = records[1]
        else:
            runningTotal = int(records[2])
            runningCourses = 1

# print the last student record
if previousStudentId == currentStudentId:
    PrintRecord(currentStudentName, runningTotal, runningCourses)

#file.close()
