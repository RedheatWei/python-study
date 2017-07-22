#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年7月23日
Email: weipeng@sinashow.com
@author: Redheat

'''
import re

def WriteText(text):
    f = open('zongheng.txt','a')
    f.write(text)
    f.close()



f = open('sihai.txt')
con = f.readlines()
f.close()
for i in con:
    m = re.search(u'<(\s|\S)*>',i)
    if m is not None:
        print m.group()
    else:
        WriteText(i)