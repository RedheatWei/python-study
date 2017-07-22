#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月27日
Email: weipeng@sinashow.com
@author: Redheat

'''
from socket import *
import time
import os,sys

###################参数设置#########################
dir_name = '/data0/NetStatus'#日志目录
file_name = dir_name + '/tcp_status.log'#日志名字
time_out = []
max_number = 400#time_out列表里元素个数
max_size = 5000000#最大日志大小，这里设置的5M
HOST = sys.argv[1]#服务端ip
PORT = 21568#服务端口
BUFSIZ = 1024
ADDR = (HOST,PORT)

###################几个模块#########################
def log_write(file_name,log):#写入日志，没什么可注释的
    f = open(file_name,'a')
    f.write(log)
    f.close()

def log_hadle(file_name):#防止日志过大，处理日志的，执行一次删除前面的一半
    f = open(file_name)
    f_main = f.readlines()
    f.close()
    del f_main[:(len(f_main)/2)]
    f = open(file_name,'w')
    for line in f_main:
        f.write(line)
    f.close()     
    
def mk_dir(dir_name):#创建目录
    if  os.path.isdir(dir_name) == False:
        os.mkdir(dir_name)
        
        
####################主程序##########################        
mk_dir(dir_name)
while True:
    try:
        try:
            file_size = os.path.getsize(file_name)
        except Exception:
            file_size = 0
        while file_size < max_size:#判断日志大小，太大就会删除一部分
            if len(time_out) < max_number:#判断time_out列表元素个数，太多就会删除一部分
                tcpCliSock = socket(AF_INET,SOCK_STREAM)
                try:#尝试创建连接，失败就会写入日志
                    tcpCliSock.connect(ADDR)
                except Exception,e:
                    log = '%s %s \n' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),e)
                    log_write(file_name, log)
                    time.sleep(3)
                else:#成功就会计算时间差写入日志
                    tcpCliSock.send(str(time.time()))
                    data_s = (tcpCliSock.recv(BUFSIZ),time.time())
                    time.sleep(3)
                    tcpCliSock.close()
                    if not data_s[0]:
                        outtime = 3
                    else:
                        outtime = float(data_s[-1]) - float(data_s[0])
                        if outtime > 0:
                            pass
                        else:
                            outtime = 0
                        time_out.append(outtime)
                    now_delay = time_out[-1]
                    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(data_s[-1]))
                    avg_five = sum(time_out[-100:]) / len(time_out[-100:])
                    avg_fifteen = sum(time_out[-300:]) / len(time_out[-300:])
                    log = '%s  delay:%4f  five:%4f  fifteen:%4f \n' % (now_time,now_delay,avg_five,avg_fifteen)
                    log_write(file_name, log)
            else:
                del time_out[:(len(time_out)/2)]#防止这个倒霉列表太大占用内存，列表里个数超过400会删除一半内容
        else:
            log_hadle(file_name)
            continue
    except Exception,e:#记录所有异常并写入日志
        log = '%s %s \n' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),e)
        log_write(file_name, log)
        break
