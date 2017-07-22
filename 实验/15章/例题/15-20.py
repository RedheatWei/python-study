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
    mail = re.search('\w+@\w+\.(com|edu|net|org|gov)', eachline)
    if mail is not None:
        print mail.group()