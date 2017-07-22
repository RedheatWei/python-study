num = ['','','','']
for n in range(1,4):
    num[n] = ('num' + str(n))
#    print num[n]
    num[n] = raw_input("Enter your %d number:" % (n))
del num[0]
#print num
maxn = int(max(num))
minn = int(min(num))
midn = 0
if int(num[0]) != maxn and int(num[0]) != minn:
    midn = num[0]
elif int(num[1]) != maxn and int(num[1]) != minn:
    midn = num[1]
else:
    midn = num[2]
#print midn
#def mind():
#if num[0] < maxn and num[0] > minn:
#    midn = num[0]    
#print midn
print '%s > %s > %s' % (maxn,midn,minn)
    
