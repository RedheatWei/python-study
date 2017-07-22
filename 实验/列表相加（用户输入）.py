#!/usr/bin/env python
numsum = int(0)
num1 = int(raw_input('Enter your first number:'))
num2 = int(raw_input('Enter your second number:'))
num3 = int(raw_input('Enter your third number:'))
num4 = int(raw_input('Enter your forth number:'))
num5 = int(raw_input('Enter your fifth number:'))
aList = [num1,num2,num3,num4,num5]
for num in range(len(aList)):
    print num
    numbera = aList[num]
    numsum = numsum+numbera
print numsum
