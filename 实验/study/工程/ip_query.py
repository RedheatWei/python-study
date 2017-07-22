#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import time
import datetime
import subprocess
import urllib
import re

def write_file(file_name,write_count): #写入内容到日志
    w = file(file_name,'a')
    w.write(write_count+'\n')
    w.close()

ip = '119.167.244.134'
result = urllib.urlopen("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=%s" % ip)
res = result.readlines()
result.close()
print res




area_final = ''
for i in range(3,6):
    #print res[0].split(',')[3].split(':')[1]
    area = res[0].split(',')[i].split(':')[1]
    area_str = area.decode("unicode_escape").encode("UTF-8")
    print area_str,
    area_final += area_str
write_file('test.txt', area_final,)
#    province = res[0].split(',')[4].split(':')[1]
#    province_str = province.decode("unicode_escape").encode("UTF-8")
#    print province_str
    #for i in res:
    #     print i+'\n'