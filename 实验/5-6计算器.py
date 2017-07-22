#!/usr/bin/env python
A = str(raw_input('Enter your expression:\n'))
B = A.split('+')
C = A.split('-')
D = A.split('*')
E = A.split('/')
F = A.split('%')
G = A.split('**')
if len(B) == 2:
    print float(A[0]) + float(A[-1])
elif len(C) == 2:
    print float(A[0]) - float(A[-1])
elif len(D) == 2:
    print float(A[0]) * float(A[-1])
elif len(E) == 2:
    print float(A[0]) / float(A[-1])
elif len(F) == 2:
    print float(A[0]) % float(A[-1])
elif len(G) == 2:
    print float(A[0]) ** float(A[-1])
else:
    print 'Wrong!'