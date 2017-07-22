#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月26日

@author: Redheat
'''

import subprocess
import time
import sys

ip = sys.argv[1]
ping_cmd = 'ping -c 1 '+ip
mark_str = '64 bytes from'
file_name = ip

def write_file(file_name,write_count): #写入内容到日志
    w = file(file_name,'a')
    w.write(write_count+'\n')
    w.close()

while True:
    time.sleep(1)
    res = subprocess.Popen(ping_cmd,shell=True,stdout=subprocess.PIPE)
    now_time = time.asctime()
    res.wait()
    res_list = res.stdout.read().split('\n')
    res_str = res_list[1]
    if mark_str in res_str:
        ping_line = ' '+res_str
    else:
        ping_line = ' request time out'
    ping_str = now_time+ping_line
    write_file(file_name, ping_str)
