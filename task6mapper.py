#!/usr/bin/env python

import sys

sortedDictionary = dict()

for line in sys.stdin:
    word, count = line.split('\t')
    count = int(count)
    if len(sortedDictionary) == 20:
        minDictEntry = min(sortedDictionary.items(), key=lambda x: x[1])
        if int(minDictEntry[1]) < count:
            sortedDictionary.__delitem__(minDictEntry[0])
            sortedDictionary[word] = count
    else:
        sortedDictionary[word] = count



sortedDict = dict(sorted(sortedDictionary.items()))

for key in sortedDictionary.keys():
    print("{0}\t{1}".format(key,sortedDictionary[key]))


#elif int(minDictEntry[1]) == count:
#            sortedDictionary[word] = count
#what if two similar pharases come... need/shud handle that case too
