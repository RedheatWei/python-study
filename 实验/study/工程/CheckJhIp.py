#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年8月6日
Email: weipeng@sinashow.com
@author: Redheat

'''

def GetTxt(filename):
    f = open(filename)
    cont = f.readlines()
    f.close()
    return cont

def WriteTxt(file,line):
    f = open(file,'a')
    f.write(line)
    f.close()



agojh = GetTxt('agojh.txt')
cmdb = GetTxt('cmdb.txt')




file = 'change.txt'

for i in agojh:
    if i in cmdb:
        pass
    else:
        WriteTxt(file, i)
