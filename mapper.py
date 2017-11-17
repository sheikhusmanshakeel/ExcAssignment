import sys

filePath = "/home/raven/hadooptestdocument"

file = open(filePath, 'r+')

fileString = file.read()

print(fileString)

for line in fileString.readline():  # input from standard input
    line = line.strip()  # remove whitespaces
    tokens = line.split()  # split the line into tokens

    for token in tokens:  # write the results to standard output
        print("{0}\t{1}".format(token, 1))

file.close()