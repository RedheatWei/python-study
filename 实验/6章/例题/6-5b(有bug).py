#/usr/bin/env python
aList = []
for i in (1,2):
    stri = raw_input('Enter your %s number' % i)
    aList.append(stri)
x = len(aList[0])
z = len(aList[-1])
if x == z:
    for xa in range(x):
        if aList[0][xa] == aList[-1][xa]:
            print 'same!',
        else:
            print 'NO'
else:
    print 'NO!'