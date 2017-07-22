#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月21日
Email: weipeng@sinashow.com
@author: Redheat

'''
from socket import *

def UserLogin():
    username = raw_input('Enter your username:')
    password = raw_input('Enter your password:')
    data = username + ' '+password
    HOST = '123.56.92.243'
    PORT = 10751
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    tcpClisock = socket(AF_INET,SOCK_STREAM)
    while True:       
        try:
            tcpClisock.connect(ADDR)
        except Exception,e:
            print 'Error:%s' % e
            continue
        else:
            tcpClisock.send(data)
            rec = tcpClisock.recvfrom(BUFSIZE)
            tcpClisock.close()
            return rec

def SendCommands():
    HOST = '123.56.92.243'
    PORT = 10752
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    tcpClisock = socket(AF_INET,SOCK_STREAM)
    while True:
        try:
            tcpClisock.connect(ADDR)
        except Exception,e:
            print e
            continue
        else:
            while True:
                data = raw_input('-->')
                tcpClisock.send(data)
                rec = tcpClisock.recv(BUFSIZE)
                tcpClisock.close()
                return rec
            
def SendFiles(filename):
    HOST = '123.56.92.243'
    PORT = 10753
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    tcpClisock = socket(AF_INET,SOCK_STREAM)
    while True:
        try:
            tcpClisock.connect(ADDR)
        except Exception,e:
            print e
            continue
        else:
            while True:
                data = filename+' '+os.path.getsize(filename)
                tcpClisock.send(data)
                f = open(filename,'rb')
                while True:
                    data = f.read(BUFSIZE)
                    if not data:
                        break
                    tcpClisock.send(data)
                    continue

while True:
    if UserLogin() == 'True':
        while True:
            file_list = SendCommands()
            for i in file_list[:-1]:
                print i,
                while True:
                    filename = 
                    
    





    