#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年6月22日
Email: weipeng@sinashow.com
@author: Redheat

'''
oldfilename  = "/data0/logs/nginx/treasury.interface.sinashow.com.log"
newfilename = "/data0/logs/nginx/new.log"

try:
    fold = open(oldfilename,"r")
    fnew = open(newfilename,"a")
    for i in fold.readlines():
        oldlinelist = i.split()
        newlist = oldlinelist[4] + ' ' + oldlinelist[12]  + '\n'
        fnew.write(newlist)
except Exception,e:
    print "异常退出！",e
else:
    print "正常退出！"
finally:
    fold.close()
    fnew.close()
