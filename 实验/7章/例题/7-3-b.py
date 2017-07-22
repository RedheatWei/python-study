#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年2月27日

@author: Redheat
'''
adict = {'a':1,'b':2,'c':3,'d':4}
bdict = sorted(adict)
for key in bdict:
    print key,adict[key]