#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月26日

@author: Redheat
'''
ip_list = '183.131.72.3  183.131.72.4  183.131.72.53   183.131.72.6  183.131.72.7  183.131.72.8 183.131.72.5'
import subprocess
p = subprocess.Popen('chmod +x deal_ping.py',shell=True)
p.wait()
for ip in ip_list.split():
    nohup_cmd = 'python deal_ping.py '+ip
    pro = subprocess.Popen(nohup_cmd,shell=True)
    print '%s success!' % ip
    continue
