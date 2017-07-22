#!/usr/bin/env python
mon = int(raw_input('Enter your money: '))
A = divmod(mon,25)
Aa = A[0]
Ab = A[1]
B = divmod(Ab,10)
Ba = B[0]
Bb = B[1]
C = divmod(Bb,5)
Ca = C[0]
Cb = C[1]
print '25￠ %d 10￠ %d 5￠ %d 1￠ %d  ' % (Aa,Ba,Ca,Cb)