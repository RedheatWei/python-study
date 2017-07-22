#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月14日

@author: Redheat
'''

from socket import *
import time

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)


udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)


while True:

    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (time.time(),data),addr)
    print '...received form and returned to:', addr
    
udpSerSock.close()

