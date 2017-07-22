#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��2��26��

@author: Redheat
'''
minute = input('How many minute:')
number = divmod(minute, 60)
print '%d hours and %d minute!' % (number[0],number[-1])