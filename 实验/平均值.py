numsum = float(0)
aList = [43,12,6543,634,643534,21312,232131]
for num in range(len(aList)):
    print num
    numbera = aList[num]
    numsum = numsum+numbera
ave = float(numsum / (len(aList)))
print ave
