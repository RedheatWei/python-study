#用于输入一组数值进行排序，数值只见以空格隔开
a = raw_input('Enter numbers and separated by spaces:\n')
b = a.split()
#将b的元素类型转换为整型
for i in range(len(b)):
    b[i] = int(b[i])
#按顺序排序
c = sorted(b)
c.reverse()
num = len(c)
#print c
#逐行输出
for j in range(num-1):
    print '%d ' % c[j],
    print '>',
else:
    print '%d' % c[-1]
#print d