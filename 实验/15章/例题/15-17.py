#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月29日
Email: weipeng@sinashow.com
@author: Redheat

'''
import re
f = open('redata.txt')
conn = f.readlines()
for eachline in conn:
    week = re.match(r'^(Mon|The|Wen|Thu|Fri|Sat|Sun)',eachline)
    if week is not None:
        print len(week.group())