#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月26日

@author: Redheat
'''

import subprocess
import time
import sys
import threading

ip_list = sys.argv[1:]
mark_str = '64 bytes from'

def write_file(file_name,write_count): #写入内容到日志
    w = file(file_name,'a')
    w.write(write_count+'\n')
    w.close()

def ping_modle(ip):
    ping_cmd = 'ping -c 1 '+ip
    file_name = ip
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
        
def main():
    threads = []
    nloops = range(len(ip_list))
    
    for i in nloops:
        t = threading.Thread(target=ping_modle,args=(ip_list[i],))
        threads.append(t)

    for i in nloops:
        print threads[i]
        threads[i].start()
        
    for i in nloops:
        threads[i].join()
        
if __name__ == '__main__':
    main()