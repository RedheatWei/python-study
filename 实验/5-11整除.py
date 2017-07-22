#!/usr/bin/env python
A = int(raw_input('A='))
B = int(raw_input('B='))
C = divmod(A,B)
if C[-1] == 0:
    print 'True'
else:
    print 'Flase'