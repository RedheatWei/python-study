#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年10月14日
Email: weipeng@sinashow.com
@author: Redheat

'''
from socket import *
import time

#############参数配置区###############
HOST=''
#IP白名单应该写成192.168.1.0,192.168.2.1等格式，中间以,隔开 
AllowIp='192.168.1.0,192.168.2.1'
####################################

class TcpConnectServer(object):
    def __init__(self,HOST):
        self.HOST = HOST
        self.PORT = 21550
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
        self.AllowIpList = GetTxtStr().AllowIpList(AllowIp)
    
    def TcpServer(self):
        tcpSerSock = socket(AF_INET,SOCK_STREAM)#tcp套接字
        while True:
            try:
                tcpSerSock.bind(self.ADDR)
                tcpSerSock.listen(5)
            except Exception,e:#如果绑定套接字失败，打印失败提示，并且等待30秒后再次绑定
                print e
                time.sleep(30)
                continue
            else:#绑定套接字成功之后，就开始等待tcp接入
                while True:
                    tcpCliSock, addr = tcpSerSock.accept()
                    if addr in self.AllowIpList:
                        while True:
                            data_rec = tcpCliSock.recv(self.BUFSIZE)
        #                         print data_rec
                            filename = GetTxtStr().HandleRec(data_rec)
                            allstr = GetTxtStr().GetStr(filename)
        #                         print type(allstr)        
                            tcpCliSock.send(allstr)
                            tcpCliSock.close()#关闭本次连接，重新等待连接
                            break
                    else:
                        pass
                tcpSerSock.close()

class GetTxtStr(object):
    
    #接收数据处理函数，在这里修改接收到的数据如何处理
    def HandleRec(self,data_rec):
        return data_rec
    #文件处理函数，在这里修改对txt文件如何处理
    def GetStr(self,filename):
        f=open(filename)
        alllist=f.readlines()
        f.close()
        allstr = ''.join(alllist)
        return allstr
    #IP参数处理函数，在这里修改白名单参数如何处理
    def AllowIpList(self,AllowIp):
        iplist=[]
        for ip in AllowIp.split(','):
            iphead='.'.join(ip.split('.')[:4])
            ipend=ip.split('.')[-1]
            if ipend == '0':
                for i in range(1,256):
                    newip=iphead+'.'+i
                    iplist.append(newip)
            else:
                iplist.append(ip)
        return iplist


if __name__ == '__main__':
    TcpConnectServer(HOST).TcpServer()