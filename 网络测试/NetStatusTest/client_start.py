#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月7日
Email: weipeng@sinashow.com
@author: Redheat

'''

import subprocess,os,sys
import zipfile,ftplib,socket

dir_name = '/data0/NetStatus' 
file_name = dir_name + '/NetStatusTest.zip'
python_progream_ser = ['tcp_server.py','udp_server.py']
python_progream_cli = ['tcp_client.py','udp_client.py']


def mk_dir(dir_name):#创建目录
    if os.path.isdir(dir_name) is False:
        print 'Have no dir %s,mkdir %s' % (dir_name,dir_name)
        os.mkdir(dir_name)
    else:
        print 'Check dir OK.'
def un_zip():
    try:
        f = zipfile.ZipFile(file_name,'r')
        f.extractall(dir_name+'/')
        'Unzip %s OK.' % file_name
    except Exception,e:
        print 'ERROR: %s\nProgram quit!' % e
        sys.exit()
    
def ftp_get(dir_name,file_name):
    HOST = 'ftp.intra.sinashow.com'
    FILE = 'NetStatusTest.zip'
    username = 'weipeng'
    passwd = 'weipeng##231'
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror),e:
        print 'ERROR: cannot reach "%s"\n Program quit!' % HOST
        sys.exit()
    print 'Connect to host "%s" success!' % HOST
    try:
        f.login(username,passwd)
        print 'FTP login success!'
        f.retrbinary('RETR %s' % FILE,open(file_name,'wb').write)
    except Exception,e:
        print 'ERROR: %s\n Program quit!' % e
        f.quit()
        sys.exit()
    else:
        print 'Download to %s' % dir_name
        f.quit()

def progream_check(i):
    f = subprocess.Popen('ps axuf | grep -v grep | grep -c '+'"'+dir_name+'/'+i+'"',shell=True,stdout=subprocess.PIPE)
    f.wait()
    data = f.stdout.readlines()
    return int(data[0].split('\n')[0])

def progream_start(i,host):
    f = subprocess.Popen('python %s/%s %s' % (dir_name,i,host),shell=True)

if __name__ == '__main__':
    print '''*********************************************************************************
When you start this progream ,you must input "python progream_name c/s host".
For example :
"python client_start.py c 123.56.92.243"
It's means start for client mode and host is 123.53.92.243.
But when you star for Server mode,you can input "s" only and not need to input host.
Be careful!
*********************************************************************************
    '''
    try:
        choice = sys.argv[1].split()[0].lower()
    except Exception,e:
        print '%s! Please choice a right mode "c/s",progream quit!' % e
        sys.exit()
    if choice in 'sc':
        if choice == 's':
            python_progream = python_progream_ser
        else:
            if sys.argv[2] == None:
                print 'ERROR:Have no host for client,Progream quit!'
                sys.exit()
            else:
                host = sys.argv[2].split()[0].lower()
                python_progream = python_progream_cli
        mk_dir(dir_name)
        if os.path.exists(file_name) is False:
            ftp_get(dir_name,file_name)
        un_zip()
        for i in python_progream:
            check_number = progream_check(i)
            if check_number > 0:
                print 'Progream %s is running %s.' % (i,check_number)
                if check_number > 1:
                    print 'More than 1 progream is running,Please check!'
            else:
                progream_start(i,host)
                print 'start %s.' % i
                continue
    else:
        print 'Please choice a right mode "c/s",progream quit!'
        sys.exit()