#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年2月26日

@author: Redheat
'''
import sys
EN = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
number = raw_input('Enter a number:')
number_lenth = len(number)
if number_lenth == 1:
    number = int(number)
    print EN[number]
elif number_lenth == 2:
    number_first = int(number[0])
    number_second = int(number[-1])
    print '%s-%s' % (EN[number_first],EN[number_second])
else:
    print 'Error!'
    sys.exit()