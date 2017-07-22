#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��3��11��

@author: Redheat
'''
file_name = raw_input('Enter an absolute path:')
f = file(file_name)
aa = f.readlines()
f.close()
num = 0
while True:
    for line in aa[num:num+25]:
        print line,
    go = raw_input('Enter (c)  to continue,other to exit.')
    num += 25
    if go != 'c':
        break
    else:
        continue
    