#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月19日
Email: weipeng@sinashow.com
@author: Redheat

'''
import socket,time,os,struct

class SocketClient(object):
    'for socket send or receve'
    def __init__(self):
        self.HOST = '123.56.92.243'
        self.PORT = 10751
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
        
        
    def InfoSend(self,data):
        self.tcpClisock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        while True:       
            try:
                self.tcpClisock.connect(self.ADDR)
            except Exception,e:
                print 'Error:%s' % e
                continue
            else:
                self.tcpClisock.send(data)
                rec = self.tcpClisock.recvfrom(self.BUFSIZE)
                self.tcpClisock.close()
                return rec
        
    
    def FileSend(self,filename):
        self.tcpClisock.timeout(1)
        try:
            self.tcpClisock.connect(self.ADDR)
        except Exception,e:
            print 'Error:%s' % e
        else:
#            FILEINFO_SIZE = struct.calcsize('128sI')
            data = struct.pack('128sI',filename,os.stat(filename).st_size)
            self.tcpClisock.send(data)
            fp = open(filename,'rb')
            while True:
                data = fp.read(self.BUFSIZE)
                if not data:
                    break
                self.tcpClisock.send(data)
            fp.close()
            
    def FileReceve(self,filename):
        self.tcpSerSock.bind('',10750)
        self.tcpSerSock.listen(5)
        while True:
            self.tcpCliSock,self.addr = self.tcpSerSock.accept()
            fp = open(filename,'ab')
            while True:
                rec = self.tcpClisock.recv(self.BUFSIZE)
                fp.write(rec)
            fp.close()
            
    def __del__(self):
        self.tcp
        self.tcpClisock.close()

#def PackageType(type_calss,data):
#    return (type_calss,data)


if __name__ == '__main__':
    try:
        while True:
            sendinfo = SocketClient()
            username = raw_input('Welcome to use this program,please input your username:')
            password = raw_input('Please Enter Your Password:')
            rec = sendinfo.InfoSend(username+' '+password+' '+'user')
            if rec[0] != 'True':
                print 'Bad user or password,please check!'
                continue
            else:
                print '''Welcome back %s\n!
    "ls" to display files list."get" to download files."put" to upload files.\n''' % username
                break
        while True:
            data = raw_input('-->')
            if data == 'ls':
                try:
                    print sendinfo.InfoSend(data)[:-1]
                    continue
                except Exception,e:
                    print e
                    break
    except Exception,e:
        SocketClient().InfoSend('close')
    