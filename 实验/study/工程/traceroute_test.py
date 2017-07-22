#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月12日

@author: Redheat
'''
import os
import time
import datetime
import subprocess
import urllib


input_ip = raw_input('IP list:')
ip_list = input_ip.split()#将ip地址处理成列表

def write_file(file_name,write_count): #写入内容到日志
    w = file(file_name,'a')
    w.write(write_count+'\n')
    w.close()

def read_file(file_name): #获取日志内容
    f = open(file_name)
    f_con = f.readlines()
    f.close()
    return f_con

def trace_print(ip):
    print '\033[0;32;40mWarning!\033[0m'
    print '\033[0;32;40mJust for output,may different from log.\033[0m'
    print '\033[0;32;40m%s\033[0m' % datetime.datetime.now()
#    for ip in ip_list:
    p = subprocess.Popen('traceroute '+ip,shell=True)
    p.wait()
            
def get_area_ip(line):
    for each_str in line.split():
        if '(' in each_str:
            area_ip = each_str.split('(')[-1].split(')')[0]
#            print area_ip
            return area_ip

def get_area(area_ip):
#    area_ip = get_area_ip()
    result = urllib.urlopen("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=%s" % area_ip)
    res = result.readlines()
    result.close()
#    print res
    area_final = ''
    if len(res[0].split()[3]) > 70:
        for i in range(3,6):
            area = res[0].split(',')[i].split(':')[1]
            area_str = area.decode("unicode_escape").encode("UTF-8")
            area_final += area_str
    else:
        area_final = '内网'
    return area_final
#    write_file(file_name, area_str)
#        area_str += area_str
#    return area_str,
    
def log_write(ip):
#    for ip in ip_list:
    res = subprocess.Popen('traceroute '+ip,shell=True,stdout=subprocess.PIPE)
    res.wait()
    res_list = res.stdout.read().split('\n')
    
#        file_name = 'res_traceroute_'+ip+'.log'
#    area = get_area(ip)
    now_time = str(datetime.datetime.now())
    write_file(file_name,now_time)
    for line in res_list:
        area_ip = get_area_ip(line)
#        print area_ip
        area = get_area(area_ip)
#        print area
        write_file(file_name, line)
        write_file(file_name, area)
        
for ip in ip_list:
    file_name = 'res_traceroute_'+ip+'.log'
    trace_print(ip)
    log_write(ip)
    print read_file(file_name)

