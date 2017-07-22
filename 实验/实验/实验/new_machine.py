#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月31日

@author: Redheat
'''
import ftplib
import os
import socket

HOST = 'ftp.intra.sinashow.com'
user = 'weipeng'
passwd = 'weipeng##231'
file_name = 'config_file.rar'

def ftp_download(HOST,user,passwd,file_name):
    
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror),e:
        print 'Error: cannot reach %s!' % HOST
    #    return
    print 'connected to host %s' % HOST
    
    try:
        f.login(user,passwd)
    except ftplib.error_perm:
        print 'Error: cannot login %s!' % user
        f.quit()
    #    return
    print 'login in success!'
    
    try:
        f.retrbinary('RETR %s' % file_name, open(file_name,'wb').write)
    except ftplib.error_perm:
        print 'Error: cannot read file %s' % file_name
    else:
        print 'Download %s success!' % file_name
    f.quit()

    
ftp_download(HOST, user, passwd, file_name)