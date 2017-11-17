#!/usr/bin/env python

import sys

previousStudentId = -1
studentName = ""
studentCourseRecord = ""

for line in sys.stdin:
    records = line.strip().split('\t')
    studentId = int(records[0])
    if len(records) == 3:
        course = records[1]
        marks = records[2]
        if studentId != previousStudentId:
            if previousStudentId != -1:
                print("{0}---> {1}".format(studentName, studentCourseRecord))
            studentName = ""
            studentCourseRecord = "({0},{1})".format(course, marks)
        else:
            studentCourseRecord += "({0},{1})".format(course, marks)
        previousStudentId = studentId
    else:
        if studentId != previousStudentId:
            if previousStudentId != -1:
                print("{0}---> {1}".format(studentName, studentCourseRecord))
            studentCourseRecord = ""
        studentName = records[1]
        previousStudentId = studentId

if studentId == previousStudentId:
    print("{0}---> {1}".format(studentName, studentCourseRecord))
