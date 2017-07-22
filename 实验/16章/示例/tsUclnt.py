#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月14日

@author: Redheat
'''
import sys
import time
from socket import *


if len(sys.argv) == 1:
    HOST = 'localhost'
    PORT = 21567
elif len(sys.argv) == 2:
    if len(sys.argv[1]) > 7:
        HOST = sys.argv[1]
        PORT = 21567
    else:
        PORT = int(sys.argv[1])
        HOST = 'localhost'
else:
    if len(sys.argv[1]) > 7:
        HOST = sys.argv[1]
        PORT = int(sys.argv[-1])
    else:
        PORT = int(sys.argv[1])
        HOST = sys.argv[-1]

print HOST,PORT


#HOST = 'localhost'
#PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)



while True:
    udpCliSock = socket(AF_INET,SOCK_DGRAM)
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data
    udpCliSock.close()
    
udpCliSock.close()

