#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月30日

@author: Redheat
'''
import urllib
area_ip = '123.56.92.243'
def get_area(area_ip):
    result = urllib.urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=%s" % area_ip)
    res = result.readlines()
    result.close()
    res_data = eval((res[0]))['data']#将含有ip信息的数据转为字典
    return res_data['country'].decode("unicode_escape").encode("UTF-8")+res_data['region'].decode("unicode_escape").encode("UTF-8")+\
                        res_data['city'].decode("unicode_escape").encode("UTF-8")+res_data['isp'].decode("unicode_escape").encode("UTF-8")
                        
print get_area(area_ip)