#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年7月20日
Email: weipeng@sinashow.com
@author: Redheat

'''
from multiprocessing import Pool

def sayhai(name,n):
    print 'my name is ',name,n

pool = Pool(processes=5)

pool.map(sayhai,range(20))