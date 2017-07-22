#!/usr/bin/env python
for i in range(20):
    A = divmod(i,2)
    if A[-1] == 0:
        print i
    else:
        i = i + 1