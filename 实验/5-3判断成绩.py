#!/usr/bin/env python
import sys
A = int(raw_input('A=\n>'))
if 90 <= A <= 100:
    print 'A'
elif 80 <= A <= 89:
    print 'B'
elif 70 <= A <= 79:
    print 'C'
elif 60 <= A <= 69:
    print 'D'
elif A < 60:
    print 'F'
else:
    print 'Go away!'
    sys.exit()
#try:
#    0 < A < 100
#except Exception ,e:
#    sys.exit()
#else:
#    print A