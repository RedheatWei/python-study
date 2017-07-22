#!/usr/bin/env python
A = int(raw_input('A=\n>'))
fou = divmod(A,4)
hun = divmod(A,100)
if fou[1] == 0 and hun[1] != 0:
    print 'yes'
elif fou[1] == 0 and hun[1] == 0:
    print 'yes'
else:
    print 'no'