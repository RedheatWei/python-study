#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年7月20日
Email: weipeng@sinashow.com
@author: Redheat
Ver1.0 
'''
from socket import *
import threading,re

#端口列表请按照如下方式自行添加，支持-表示一段端口。注意：ip地址暂不支持整段
#多线程脚本，没有做线程池处理，虽然在测试中发现直接写1-65535没有问题，但是仍然不建议测试过多端口。
Port = '21,22,80,81,161,3306'
ip_list = ['127.0.0.1']


#将端口转换为端口列表
def PortList(Port):
    portlist = Port.split(',')
    alllist = []
    for i in portlist:
        if re.search('\d*-\d*', i):
            list1 = list(xrange(int(i.split('-')[0]),int(i.split('-')[-1])+1))
        else:
            alllist.append(int(i))
    return alllist + list1

port_list = PortList(Port)
port_num = len(port_list)

#建立一个socket连接
class PortLinkTcp(object):
    def __init__(self,ServerIp,Port):
        self.HOST = ServerIp
        self.PORT = Port
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
        
    def TcpConnect(self):
        while True:
            tcpCliSock = socket(AF_INET,SOCK_STREAM)
            tcpCliSock.settimeout(1)
            try:
                tcpCliSock.connect(self.ADDR)
            except Exception,e:
                return 0
            else:
                return 1
#端口连接测试，成功则返回端口号
def PortTest(ip,port):
    state = PortLinkTcp(ip,port).TcpConnect()
    if  state == 0:
        pass
    else:
        print '%s %s \n' % (ip,port)
#端口多线程处理      
def PortThread(ip):
    threads = []
    for port in port_list:
        t = threading.Thread(target=PortTest,args=(ip,port))
        threads.append(t)
        
    for i in range(port_num):
        threads[i].start()
    
    for i in range(port_num):
        threads[i].join()

#IP多线程处理
if __name__ == '__main__':
    IPthreads = []
    for ip in ip_list:
        th = threading.Thread(target=PortThread,args=(ip,))
        IPthreads.append(th)
    
    for i in range(len(ip_list)):
        IPthreads[i].start()
        
    for i in range(len(ip_list)):
        IPthreads[i].join()
