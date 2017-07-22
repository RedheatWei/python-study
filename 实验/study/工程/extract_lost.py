#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月1日
Email: weipeng@sinashow.com
@author: Redheat

'''
iplist = '119.167.244.131  122.141.228.194  124.95.161.130  124.95.165.77  60.220.213.195'


for i in iplist.split():
    filename = '/data0/testsend/'+i+'/temp_sendd.log'
    f = open(filename)
    for line in f.readlines():
        if line.split()[-1].split('%')[0] > 0:
            print line
    
    f.close()