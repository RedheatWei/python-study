#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��2��26��

@author: Redheat
'''
import sys
number = raw_input('Enter a number:')
if len(number) != 9:
    print 'Error!'
else:
    print '%s.%s.%s' % (number[:3],number[3:6],number[6:])