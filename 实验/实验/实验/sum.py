#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月25日
Email: weipeng@sinashow.com
@author: Redheat

'''

def check(num):
    need = divmod(num, 2)[0]
    num_list = []
    for i in range(need):
        if divmod(num,i)[-1] == 0:
            num_list.append(i)
    return sum(num_list)


large = 10**2
check_list = []

for num in range(large):
    print check(num)
#    check_list.append(check(num))
#print sum(check_list)