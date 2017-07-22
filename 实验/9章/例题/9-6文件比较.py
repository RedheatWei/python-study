#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月11日

@author: Redheat
'''
file1 = file('D:\python_test\UCC1.log')
AA = file1.readlines()
file1.close()
file2 = file('D:\python_test\UCC2.log')
BB = file2.readlines()
file2.close()
num_line = len(AA)
for i in range(num_line):
    if AA[i] != BB[i]:
        line = i
        num_str = len(AA[i])
        for x in range(num_str):
            if AA[line][x] != BB[line][x]:
                str_ing = x

print line,str_ing
        