#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年8月13日
Email: weipeng@sinashow.com
@author: qjyyn

'''
import urllib2,re


for i in range(1,16):
    urlstr = 'http://gh.woxiu.com/list.html?page=%s' % i
    response = urllib2.urlopen(urlstr)
    html = response.read()
    restr = '\d{6}'
    matchre = re.findall(restr, html)
    if matchre is not None:
        print matchre