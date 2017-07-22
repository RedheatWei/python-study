#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��3��11��

@author: Redheat
'''
file_name = raw_input('Enter an absolute path:')
f = file(file_name)
print len([line for line in f])