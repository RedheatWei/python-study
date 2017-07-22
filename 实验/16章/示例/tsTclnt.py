#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月14日

@author: Redheat
'''
from socket import *

HOST = '123.56.92.243'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST,PORT)



while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
    
tcpCliSock.close()