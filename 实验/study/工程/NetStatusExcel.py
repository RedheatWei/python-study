#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月29日
Email: weipeng@sinashow.com
@author: Redheat

'''

import time,re,subprocess,sys,xlwt
import socket,threading
from socket import *


class TcpStatusServer(object):
    def __init__(self):
        self.HOST = ''
        self.PORT = 21568
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
    
    def TcpServer(self):
        tcpSerSock = socket(AF_INET,SOCK_STREAM)
        while True:
            try:
                tcpSerSock.bind(self.ADDR)
                tcpSerSock.listen(5)
                print '1'
            except Exception,e:
                print e
                print '2'
                time.sleep(30)
                continue
            else:
                while True:
                    tcpCliSock, addr = tcpSerSock.accept()
                    while True:
                        data_rec = tcpCliSock.recv(self.BUFSIZE)
                        print data_rec
                        tcpCliSock.send(data_rec)
                        tcpCliSock.close()
                        break
                tcpSerSock.close()

class TcpStatusAgent(object):
    def __init__(self,ServerIp):
        self.HOST = ServerIp
        self.PORT = 21568
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
        self.data_sen = '1' * (2**9)
        
    def TcpAgent(self,tablename):
        while True:
            tcpCliSock = socket(AF_INET,SOCK_STREAM)
            try:
                tcpCliSock.connect(self.ADDR)
            except Exception,e:
                print e
                time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                ip_ip = self.HOST
                delay = None
                time_out = 1
                Account().TcpAdd(tablename,time_time, ip_ip, delay, time_out)
                time.sleep(10)
                continue
            else:
                tcpCliSock.send(str(time.time()))
                data_s = (tcpCliSock.recv(self.BUFSIZE),time.time())
                tcpCliSock.close()
                ip_ip = self.HOST
                time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(data_s[-1]))
                delay = float(data_s[-1]) - float(data_s[0])
                time_out = None
                Account().TcpAdd(tablename,time_time, ip_ip, delay, time_out)
                time.sleep(10)

class  UdpStatusServer(object):
    def __init__(self):
        self.HOST = ''
        self.PORT = 21569
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)                       
                    
    def UdpServer(self):
        while True:
            udpSerSock = socket(AF_INET,SOCK_DGRAM)
            try:
                udpSerSock.bind(self.ADDR)
            except Exception,e:
                print e
                time.sleep(30)
                continue
            else:
                while True:
                    number = 0
                    data, addr = udpSerSock.recvfrom(self.BUFSIZE)
                    while number < 40:
                        udpSerSock.sendto('[%s] %s' % (time.time(),data),addr)
                        number += 1
                        continue
                    else:
                        break

class UdpStatusAgent(object):
    def __init__(self,ServerIp):
        self.HOST = ServerIp
        self.PORT = 21569
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
        self.data_sen = '1' * (2**9)
            
    def UdpAgent(self,tablename):
        udpCliSock = socket(AF_INET,SOCK_DGRAM)
        udpCliSock.settimeout(5)
        while True:
            udpCliSock.sendto(self.data_sen,self.ADDR)
            time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            number = 0
            while True:
                try:
                    data_rec,ADDR = udpCliSock.recvfrom(self.BUFSIZE)
                    number += 1
                    print number
                    continue
                except Exception,e:
                    print e
                    break
            time.sleep(1)
#            udpCliSock.close()
            ip_ip = self.HOST
            lengh = len(data_rec)
            success = number
            dropped = 40 - number
            Account().UdpAdd(tablename, time_time, ip_ip, lengh, success, dropped)
            print 'success'
            time.sleep(3)
            continue

class WriteExcel():
    def __init__(self,genre):
        self.filename = time.strftime('%Y%m%d%H',time.localtime(time.time()))
        self.workbook = xlwt.Workbook()
        self.sheet = self.workbook.add_sheet(genre)
        
        

def IpTransform(ip):
    return ip.replace('.','_')

def GetIp():
    localip = socket.getfqdn(socket.gethostname())
    return socket.gethostbyname(localip)

def InstallXlwt():
    try:
        import xlwt
    except Exception:
        print 'xlwt is installing,please wait...'
        cmd = 'pip install xlwt'
        res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        res.wait()
        print 'xlwt has been installed!'

if __name__ == '__main__':
    
    parameter = sys.argv[1:]
    for i in parameter:
        if len(i) > 1:
            ServerIp = i
        else:
            if i == 's':
                mode = 's'
            if i == 't':
                socket_mode = 't'
            if i == 'c':
                mode = 'c'
            if i == 'u':
                socket_mode = 'u'
                
    if mode == 's':
        
        if socket_mode == 't':
            TcpStatusServer().TcpServer()
        else:
            UdpStatusServer().UdpServer()
    else:
        InstallMsqldb()
        local_ip = GetIp()
        tablename = IpTransform(local_ip)+''
        Account().CreatTables(tablename)
        if socket_mode == 't':
            TcpStatusAgent(ServerIp).TcpAgent(tablename)
        else:
            UdpStatusAgent(ServerIp).UdpAgent(tablename)    
