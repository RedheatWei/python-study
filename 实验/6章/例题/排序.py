#��������һ����ֵ����������ֵֻ���Կո����
a = raw_input('Enter numbers and separated by spaces:\n')
b = a.split()
#��b��Ԫ������ת��Ϊ����
for i in range(len(b)):
    b[i] = int(b[i])
#��˳������
c = sorted(b)
c.reverse()
num = len(c)
#print c
#�������
for j in range(num-1):
    print '%d ' % c[j],
    print '>',
else:
    print '%d' % c[-1]
#print d