#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import time,sys,os,urllib,urllib2
from socket import *
ServerIp = '10.192.17.142'

#创建一个TCPClient类，给ServerIP发送数据，ServerIP为启动脚本时后面跟的IP数据，端口与服务端相同，缓冲区1024字节，发送字节大小为512
#如果连接失败，那么会判定本次连接超时，时间为服务端时间，ip_ip是服务端IP，delay是本次tcp请求用的时间
#time_out为1的时候表示本次连接超时，否则为None
class TcpStatusAgent(object):
    def __init__(self,ServerIp):
        self.HOST = ServerIp
        self.PORT = 9080
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
        self.data_sen = '1' * (2**9)
    def TcpAgent(self):
        while True:
            tcpCliSock = socket(AF_INET,SOCK_STREAM)#tcp套接字
            try:
                tcpCliSock.connect(self.ADDR)#尝试连接
            except Exception,e:
                print e
            else:
                tcpCliSock.send(str(time.time()))
                data_s = (tcpCliSock.recv(self.BUFSIZE),time.time())
                print data_s
                tcpCliSock.close()
                time.sleep(3)



class UdpStatusAgent(object):
    def __init__(self,ServerIp):
        self.HOST = ServerIp
        self.PORT = 21569
        self.BUFSIZE = 514
        self.ADDR = (self.HOST,self.PORT)
        self.data_sen = '1' * (2**9)#512字节的发送数据
            
    def UdpAgent(self):
        udpCliSock = socket(AF_INET,SOCK_DGRAM)
        udpCliSock.settimeout(5)#设置超时时间，发出去之后5秒还没收到回包，那么肯定就收不到包了，这也是作为udp包接收失败的依据
        while True:
            udpCliSock.sendto(self.data_sen,self.ADDR)
            time_time = time.time()#time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            number = 0
            while True:
                try:
                    data_rec,ADDR = udpCliSock.recvfrom(self.BUFSIZE)#接收到服务端发来的1个包，num就会自加1，最后统计收到的包是多少。
                    number += 1
                    continue
                except Exception,e:
                    print e
                    break
            time.sleep(1)
            ip_ip = self.HOST
            lengh = len(self.data_sen)
            success = number
            dropped = 40 - number
            rate = dropped / 40.0
            UdpSendPost(time_time, ip_ip, lengh, success, dropped, rate)
            print 'success'
            time.sleep(30)
            continue

TcpStatusAgent(ServerIp).TcpAgent()