#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年10月14日
Email: weipeng@sinashow.com
@author: Redheat

'''

from socket import *
import time

######################配置参数区#######################
ServerIP='127.0.0.1'
SendStr='change.txt' 
data=[]
#####################################################

class TcpConnectClient(object):
    def __init__(self,ServerIp):
        self.HOST = ServerIp
        self.PORT = 21550
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
#         self.data_sen = '1' * (2**9)
    def TcpAgent(self,SendStr):
        tcpCliSock = socket(AF_INET,SOCK_STREAM)#tcp套接字
        while True:
            try:
                tcpCliSock.connect(self.ADDR)#尝试连接
            except Exception,e:
                print e
                time.sleep(5)
                continue#再次尝试连接，直到连接成功
            else:
                tcpCliSock.send(SendStr)
                while True:
                    data_s = tcpCliSock.recv(self.BUFSIZE)
                    data.append(data_s)
                    if not data_s:
                        break
                print ''.join(data)
                tcpCliSock.close()
                break
            
if __name__ == '__main__':
    TcpConnectClient(ServerIP).TcpAgent(SendStr)