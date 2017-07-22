#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月15日
Email: weipeng@sinashow.com
@author: Redheat

'''
import time,random,os
from multiprocessing import Pool
def first():
    list1.append('a')
    return list1
def second(i):
    print 'Run task %s (%s)...' % (i, os.getpid())
    time.sleep(random.random() * 3)
    list2.append('b')
    print list2
    return list2



if __name__=='__main__':
    list1=[]
    list2=first()
    print list2
    print 'Parent process %s.' % os.getpid()
    pool = Pool(processes=2)
    for i in range(2):
        pool.apply_async(second,args=(i,))
    pool.close()
    pool.join()
    print 'Done'
    raw_input('Press <Enter>')