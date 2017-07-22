#!/usr/bin/env python
import sys
while True:
    aString = raw_input('Enter a string:\n')
    L = len(aString)
    i = 0
    if L > 0:
        for i in range(L):            
            print aString[i],aString[i-1]
            i += 1
        sys.exit()
    else:
        print 'Empty string!'