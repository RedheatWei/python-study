#!/usr/bin/env python
import sys
x = int(raw_input('x='))
y = int(raw_input('y='))
n = min(x,y)
X = divmod(x,n)
Y = divmod(y,n)
while n <= x and n <= y and n > 1:
    if X[-1] == 0 and Y[-1] == 0:
        print n
        sys.exit()
    else:
        n -= 1
        X = divmod(x,n)
        Y = divmod(y,n)
print 'none'