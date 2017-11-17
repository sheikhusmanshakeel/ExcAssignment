#!/usr/bin/env python

import sys
import operator

unsortedDictionary = dict()

for line in sys.stdin:
    word, count = line.split('\t')
    count = int(count)
    if len(unsortedDictionary) == 20:
        minDictEntry = min(unsortedDictionary.items(), key=lambda x: x[1])
        if int(minDictEntry[1]) < count:
            unsortedDictionary.__delitem__(minDictEntry[0])
            unsortedDictionary[word] = count
    else:
        unsortedDictionary[word] = count


sortedDictionary = sorted(unsortedDictionary.items(), key=operator.itemgetter(1))


for i in range(0,len(sortedDictionary)):
    print("{0}\t{1}".format(sortedDictionary[i][0],sortedDictionary[i][1]))

