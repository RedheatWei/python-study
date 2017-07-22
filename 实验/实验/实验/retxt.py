#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年7月30日
Email: weipeng@sinashow.com
@author: Redheat

'''

import re
f = open('haha.txt')
con = f.readlines()
f.close()

for i in con:
    m = re.match('\S', i)
    if m is not None:
        print m.group()