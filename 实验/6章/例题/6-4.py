#!/usr/bin/env python
import sys
aList = []
bList = []
#fra = raw_input('Enter your fraction:\n')
#L = len(aList)
#def addnum():
#    aList.append()
def judge():
    if 90 <= fra <= 100:
        print 'A'
        bList.append('A')
    elif 80 <= fra <= 89:
        print 'B'
        bList.append('B')
    elif 70 <= fra <= 79:
        print 'C'
        bList.append('C')
    elif 60 <= fra <= 69:
        print 'D'
        bList.append('D')
    elif fra < 60:
        print 'F'
        bList.append('F')
#    else:
#        print 'Enter a true fraction!'
#        sys.exit()
        
def average():
    L = len(aList)
    i = 0
    sum = 0
    while i < L:
        i += 1
        sum += aList[i-1]
        ave = sum / L
    print 'average is %f' % (ave)
        
while True:
    fra = float(raw_input('Enter your fraction:\n'))
    if fra <= 100 and fra >= 0:
        aList.append(fra)
        judge()
        average()
        print aList
        print bList
    else:
        print 'Enter a true fraction!'
        sys.exit()