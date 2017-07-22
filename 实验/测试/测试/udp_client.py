#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月30日
Email: weipeng@sinashow.com
@author: Redheat

'''
import os,sys
import time,threading
from socket import *

dir_name = '/data0/NetStatus' #日志目录
file_name = dir_name + '/udp_status.log'#日志名字
HOST = sys.argv[1]
PORT = 21567
BUFSIZ = 1024
max_size = 5000000#最大日志大小，这里设置的5M
ADDR = (HOST,PORT)
data_sen = '1' * (2**9)
max_number = 200
#lost = 'lost'
error = 'error'
rec = 'rec'
count = []


def log_write(file_name,log):#写入日志，没什么可注释的
    f = open(file_name,'a')
    f.write(log)
    f.close()

def mk_dir(dir_name):#创建目录
    if os.path.isdir(dir_name) == False:
        os.mkdir(dir_name)
        

def log_hadle(file_name):#防止日志过大，处理日志的，执行一次删除前面的一半
    f = open(file_name)
    f_main = f.readlines()
    f.close()
    del f_main[:(len(f_main)/2)]
    f = open(file_name,'w')
    for line in f_main:
        f.write(line)
    f.close()


mk_dir(dir_name)
while True:
    try:
        try:
            file_size = os.path.getsize(file_name)
        except Exception:
            file_size = 0
        while file_size < max_size:
            while len(count) < max_number:
                udpCliSock = socket(AF_INET,SOCK_DGRAM)
                udpCliSock.settimeout(0.3)
                udpCliSock.sendto(data_sen,ADDR)
                try:
                    data_rec,ADDR = udpCliSock.recvfrom(BUFSIZ)
                    count.append(rec)
                except Exception,e:
                    count.append(error)
                udpCliSock.close()
                count_five = count[-100:]
#                count_fifteen = count[-300:0]
                log = '%s packet_size:%s send:%s recv:%s error:%s five:packet loss rate:%s%% \n' %\
                 (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),len(data_sen),len(count_five),\
                  count_five.count(rec),count_five.count(error),float(count_five.count(error))/len(count_five)*100)
                log_write(file_name, log)
                time.sleep(3)
            else:
                del count[:(len(count)/2)]
                continue
        else:
            log_hadle(file_name)
            continue
    except KeyboardInterrupt,e:
        print e
        log = str(e) + '\n'
        log_write(file_name, log)
        udpCliSock.close()
        break
