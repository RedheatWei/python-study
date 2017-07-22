#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月27日
Email: weipeng@sinashow.com
@author: Redheat

'''
from socket import *
import time,sys

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)


while True:
    try:
        tcpSerSock.bind(ADDR)
        tcpSerSock.listen(5)
    except Exception,e:
        print e
        time.sleep(30)
        continue
    else:
        print 'waiting for connection...'
        while True:
            tcpCliSock, addr = tcpSerSock.accept()
            print '...connected from:',addr
            while True:
                data = tcpCliSock.recv(BUFSIZ)
                tcpCliSock.send(data)
                tcpCliSock.close()
                print data
                break
        tcpSerSock.close()