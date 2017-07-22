#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年2月28日

@author: Redheat
'''
n = [1,2,3,4]
s = ['a','b','c','d']
adict = {}
for i in range(len(n)):
    adict.setdefault(n[i],s[i])
print adict
    