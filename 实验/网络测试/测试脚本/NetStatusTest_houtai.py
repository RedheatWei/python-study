#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月11日
Email: weipeng@sinashow.com
@author: Redheat
ver 2.0
'''
import time,sys,os
from socket import *

#创建一个TCPServer类，接收所有IP请求，端口21568，缓冲区1024字节
class TcpStatusServer(object):
    def __init__(self):
        self.HOST = ''
        self.PORT = 21568
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
    
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
                    while True:
                        data_rec = tcpCliSock.recv(self.BUFSIZE)
                        print data_rec
                        tcpCliSock.send(data_rec)
                        tcpCliSock.close()#关闭本次连接，重新等待连接
                        break
                tcpSerSock.close()

#创建一个TCPClient类，给ServerIP发送数据，ServerIP为启动脚本时后面跟的IP数据，端口与服务端相同，缓冲区1024字节，发送字节大小为512
#如果连接失败，那么会判定本次连接超时，时间为服务端时间，ip_ip是服务端IP，delay是本次tcp请求用的时间
#time_out为1的时候表示本次连接超时，否则为None
class TcpStatusAgent(object):
    def __init__(self,ServerIp):
        self.HOST = ServerIp
        self.PORT = 21568
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
                time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                ip_ip = self.HOST
                delay = None
                time_out = 1
                data = 't %s %s %s %s' % (time_time, ip_ip, delay, time_out)
                SendDataToMysql().TcpSendToMysql(data)
                time.sleep(30)
                continue#再次尝试连接，直到连接成功
            else:
                tcpCliSock.send(str(time.time()))
                data_s = (tcpCliSock.recv(self.BUFSIZE),time.time())
                tcpCliSock.close()
                ip_ip = self.HOST
                time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(data_s[-1]))
                delay = float(data_s[-1]) - float(data_s[0])
                time_out = None
                data = 't %s %s %s %s' % (time_time, ip_ip, delay, time_out)
                SendDataToMysql().TcpSendToMysql(data)#统计好数据后，通过socket发送到183.131.72.142
                time.sleep(30)


class  UdpStatusServer(object):
    def __init__(self):
        self.HOST = ''
        self.PORT = 21569
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)                       
                    
    def UdpServer(self):
        while True:
            udpSerSock = socket(AF_INET,SOCK_DGRAM)#udp套接字
            try:
                udpSerSock.bind(self.ADDR)
            except Exception,e:
                print e
                time.sleep(30)
                continue
            else:
                while True:
                    number = 0#初始化超时次数为0
                    data, addr = udpSerSock.recvfrom(self.BUFSIZE)
                    while number < 40:#接收到客户端发来的1个数据包，服务端就会返回40个包，所以这里是40
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
        self.data_sen = '1' * (2**9)#512字节的发送数据
            
    def UdpAgent(self):
        udpCliSock = socket(AF_INET,SOCK_DGRAM)
        udpCliSock.settimeout(5)#设置超时时间，发出去之后5秒还没收到回包，那么肯定就收不到包了，这也是作为udp包接收失败的依据
        while True:
            udpCliSock.sendto(self.data_sen,self.ADDR)
            time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
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
            data = 'u %s %s %s %s %s %s' % (time_time,ip_ip, lengh, success, dropped,rate)
            SendDataToMysql().TcpSendToMysql(data)#统计好数据后，通过socket发送到183.131.72.142
            print 'success'
            time.sleep(30)
            continue

#与mysql服务器通信的socket，将得到的数据发给183.131.72.142，用的tcp连接
class SendDataToMysql(object):
    'for send data to 183.131.72.142'
    def __init__(self):
        self.HOST = '183.131.72.142'
        self.PORT = 21567
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
    
    def TcpSendToMysql(self,data):
        while True:
            tcpCliSock = socket(AF_INET,SOCK_STREAM)
            try:
                tcpCliSock.connect(self.ADDR)
            except Exception,e:#连接183.131.72.142失败，会等待30秒重连，在这段时间内，tcp客户端是不会工作的。
                print e
                time.sleep(30)
                continue
            else:
                tcpCliSock.send(data)
                tcpCliSock.close()
                break
            
#通过脚本后面跟的参数判断运行模式
#首先长度大于1的肯定是服务端IP
#接下来判断是哪种模式
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
    #控制是否自动后台运行，1：后台运行、0：终端运行
    damoe = 1
    if damoe == 1 :
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror)
            sys.exit(1)
        os.setsid()
        os.umask(0)
    if mode == 's':
        if socket_mode == 't':
            TcpStatusServer().TcpServer()
        else:
            UdpStatusServer().UdpServer()
    else:
        if socket_mode == 't':
            TcpStatusAgent(ServerIp).TcpAgent()
        else:
            UdpStatusAgent(ServerIp).UdpAgent()
