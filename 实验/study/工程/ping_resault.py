#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月26日

@author: Redheat
'''
ip_list = '117.34.93.10  117.34.93.14  183.136.132.32  60.165.99.207  60.165.99.208  60.184.67.11  61.150.126.10  61.150.126.11'
import subprocess
p = subprocess.Popen('chmod +x deal_ping.py',shell=True)
p.wait()
for ip in ip_list.split():
    nohup_cmd = 'nohup ./deal_ping.py '+ip
    pro = subprocess.Popen(nohup_cmd,shell=True)
    continue