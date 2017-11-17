#!/usr/bin/env python

import sys
#file = open('/home/raven/task4document','r')

phraseDictionary = dict()
bufferSize = 20000


def PrintWordsInDictionary(wordDictionary):
    for word in wordDictionary.keys():
        print("{0}\t{1}".format(word, wordDictionary[word]))

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    for i in range(0, len(tokens) - 1):
        word = tokens[i] + ' ' + tokens[i + 1]
        if word not in phraseDictionary:
            phraseDictionary[word] = 1
        else:
            phraseDictionary[word] += 1
        if len(phraseDictionary) > bufferSize:
            PrintWordsInDictionary(phraseDictionary)
            phraseDictionary.clear()

PrintWordsInDictionary(phraseDictionary)
#file.close()