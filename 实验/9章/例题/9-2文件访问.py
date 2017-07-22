#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��3��11��

@author: Redheat
'''
file_name = raw_input('Enter an absolute path:')
count = input('Enter a number for read:')
f = file(file_name)
for line in f.readlines():
    if count > 0:
        count -= 1
        print line.strip('\n')
    else:
        break
f.close()