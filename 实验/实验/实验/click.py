#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月28日
Email: weipeng@sinashow.com
@author: Redheat

'''

import urllib2,time
while True:
    url='http://www.vxvip.cn/news_info.asp?ArticleID=101' 
    response = urllib2.urlopen(url)
    time.sleep(1)
    continue