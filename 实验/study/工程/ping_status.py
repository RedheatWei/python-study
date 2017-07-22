#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月11日

@author: Redheat
'''
import time  
import string  
import thread  
import os  
  
ping_ip = []  
times = -1  
delay = 0  
ping_cmd = 'ping [ip]'  
result_file = 'result.txt'  
thread_count = 0  
  
  
def log(f, s):  
    fp = open(f, 'a')  
    fp.write(s)  
    fp.close()  
    return  
  
def  doping(ip):  
    ping = ping_cmd  
    ping = ping.replace('[ip]', ip)  
    ping = ping.replace('[result_file]', result_file)  
    log_str = '\n' + ping + '\n' + time.asctime() + '\n'  
    line = os.popen(ping).read()
    log_str = log_str + line + '\n'  
    print log_str  
    log(result_file, log_str)  
          
    time.sleep(delay)  
    return  
  
def ping_thread(ip, times):  
    global thread_count  
    if times == -1:  
        while True:  
            doping(ip)  
        return  
    for t in range(0, times):  
        doping(ip)  
    thread_count = thread_count - 1  
    return  
  
fp = open('exping.cfg')  
for line in fp:  
    line = line.strip()  
    if line[0:1] == '#':  
        continue  
    t = line.split('=')  
    if len(t) <= 1:  
        continue  
    if 'ip' == t[0]:  
        ping_ip.append(t[1])  
    elif 'times' == t[0]:  
        times = string.atoi(t[1])  
    elif 'delay' == t[0]:  
        delay = string.atoi(t[1])  
    elif 'cmd' == t[0]:  
        ping_cmd = t[1]     
    elif 'result_file' == t[0]:  
        result_file = t[1]  
fp.close()  
  
for ip in ping_ip:  
    thread_count = thread_count + 1  
    thread.start_new_thread(ping_thread, (ip, times))  
  
while True:  
    if thread_count == 0:  
        break  
    time.sleep(5)
