#!/usr/bin/env python
aList = raw_input('Enter a string:\n')
L = len(aList)
for i in [None] + range(L-1):
    if aList[i] == ' ':
        aList = aList[:i] + aList[i+1:]
#        L = len(aList)
        print aList