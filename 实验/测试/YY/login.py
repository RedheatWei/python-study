#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年4月11日
Email: weipeng@sinashow.com
@author: RedheatWei

'''
import httplib, urllib
 
httpClient = None
try:
#     params = urllib.urlencode({'':''})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    httpClient = httplib.HTTPConnection("http://www.yy.com", 80, timeout=30)
    httpClient.request("POST", "http://www.yy.com/index/wakeudblogin", headers)
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()