#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月29日
Email: weipeng@sinashow.com
@author: Redheat

'''
from random import randint,choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com','edu','net','org','gov')

f = open('redata.txt','a')
for i in range(randint(5,10)):
    dtint = randint(0,maxint-1)
    dtstr = ctime(dtint)
    shorter = randint(4,7)
    em = ''
    for j in range(shorter):
        em += choice(lowercase)
        
    longer = randint(shorter,12)
    dn = ''
    for j in range(longer):
        dn += choice(lowercase)
        
    f.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr,em,dn,choice(doms),dtint,shorter,longer))
f.close()
    