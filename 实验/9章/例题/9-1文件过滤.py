#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月11日

@author: Redheat
'''
file_name = raw_input('Enter an absolute path: ')

f = open(file_name)
for line in f.readlines():
    if line[0] != '#':
        print line.strip('\n')
    else:
        continue
f.close()
