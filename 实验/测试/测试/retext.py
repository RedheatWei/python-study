#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年7月28日
Email: weipeng@sinashow.com
@author: Redheat

'''
import re
f = open('docker.txt')
cont = f.readlines()
f.close()

fi = open('dock.txt','a')


for i in cont:
    r = re.match('(\s{3}\d{2}\s{2})(.+)', i)
    if r is not None:
        fi.write(r.group(2)+'\n')
    else:
        fi.write(i)
fi.close()