#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月20日
Email: weipeng@sinashow.com
@author: Redheat

'''
import time,re,subprocess,sys
import socket,threading
import fcntl,struct
from socket import *


class TcpStatusServer(object):
    def __init__(self):
        self.HOST = ''
        self.PORT = 21568
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
    
    def TcpServer(self):
        tcpSerSock = socket(AF_INET,SOCK_STREAM)
        while True:
            try:
                tcpSerSock.bind(self.ADDR)
                tcpSerSock.listen(5)
            except Exception,e:
                print e
                time.sleep(30)
                continue
            else:
                while True:
                    tcpCliSock, addr = tcpSerSock.accept()
                    while True:
                        data_rec = tcpCliSock.recv(self.BUFSIZE)
                        print data_rec
                        tcpCliSock.send(data_rec)
                        tcpCliSock.close()
                        break
                tcpSerSock.close()

class TcpStatusAgent(object):
    def __init__(self,ServerIp):
        self.HOST = ServerIp
        self.PORT = 21568
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
        self.data_sen = '1' * (2**9)
        
    def TcpAgent(self,tablename):
        while True:
            tcpCliSock = socket(AF_INET,SOCK_STREAM)
            try:
                tcpCliSock.connect(self.ADDR)
            except Exception,e:
                print e
                time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                ip_ip = self.HOST
                delay = None
                time_out = 1
                Account().TcpAdd(tablename,time_time, ip_ip, delay, time_out)
                time.sleep(30)
                continue
            else:
                tcpCliSock.send(str(time.time()))
                data_s = (tcpCliSock.recv(self.BUFSIZE),time.time())
                tcpCliSock.close()
                ip_ip = self.HOST
                time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(data_s[-1]))
                delay = float(data_s[-1]) - float(data_s[0])
                time_out = None
                Account().TcpAdd(tablename,time_time, ip_ip, delay, time_out)
                time.sleep(30)

class  UdpStatusServer(object):
    def __init__(self):
        self.HOST = ''
        self.PORT = 21569
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)                       
                    
    def UdpServer(self):
        while True:
            udpSerSock = socket(AF_INET,SOCK_DGRAM)
            try:
                udpSerSock.bind(self.ADDR)
            except Exception,e:
                print e
                time.sleep(30)
                continue
            else:
                while True:
                    number = 0
                    data, addr = udpSerSock.recvfrom(self.BUFSIZE)
                    while number < 40:
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
        self.data_sen = '1' * (2**9)
            
    def UdpAgent(self,tablename):
        udpCliSock = socket(AF_INET,SOCK_DGRAM)
        udpCliSock.settimeout(5)
        while True:
            udpCliSock.sendto(self.data_sen,self.ADDR)
            time_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
            number = 0
            while True:
                try:
                    data_rec,ADDR = udpCliSock.recvfrom(self.BUFSIZE)
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
            Account().UdpAdd(tablename, time_time, ip_ip, lengh, success, dropped,rate)
            print 'success'
            time.sleep(30)
            continue

class MySqlConnect(object):
    'for connect mysql'
    def __init__(self):
        import MySQLdb
        while True:
            try:
                self.conn = MySQLdb.connect(host='183.131.72.142',user='network',passwd='redheat@sinashow',db='network_info')
                self.cur = self.conn.cursor()
                break
            except Exception,e:
                print e
                continue

    def Handle(self,sql):
        self.cur.execute(sql)
        self.conn.commit()
    
    def Select(self,sql):
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
    
class Account(object):
    'for add or del user'
    def __init__(self):
        self.__mysql = MySqlConnect()
        
    def TcpAdd(self,tablename,time_time,ip_ip,delay,time_out):
        sql = 'insert into %s(time,ip,delay,timeout) values("%s","%s","%s","%s")' % (tablename,time_time,ip_ip,delay,time_out)
        self.__mysql.Handle(sql)
    
    def UdpAdd(self,tablename,time_time,ip_ip,lengh,success,dropped,rate):
        sql = 'insert into %s(time,ip,lengh,success,dropped,rate) values("%s","%s","%s","%s","%s","%s")' % (tablename,time_time,ip_ip,lengh,success,dropped,rate)
        self.__mysql.Handle(sql)
        
    def CreatTables(self,tablename):
        sql = 'create table if not exists %s( id int not null primary key auto_increment,time char(20) not null,ip char(20) not null,delay char(20),timeout char(20),lengh char(20),success char(20),dropped char(20),rate char(20));' % tablename
        self.__mysql.Handle(sql)

def IpTransform(ip):
    return ip.replace('.','_')

class GetIp(object):
    def __init__(self):
        pass
    
    def GetIpInfo(self,ethname):
        s = socket(AF_INET,SOCK_DGRAM)
        return inet_ntoa(fcntl.ioctl(s.fileno(), 0X8915, struct.pack('256s',ethname[:15]))[20:24])
    
    def CatchIp(self):
        IP = []
        try:
            for i in range(5):
                if not re.search(r'^(10\.|192|172)',GetIp().GetIpInfo('eth'+str(i))):
                    addr = GetIp().GetIpInfo('eth'+str(i))
                    IP.append(addr)
                    
        except Exception:
            pass
        return IP[0]
def InstallMsqldb():
    try:
        import MySQLdb
    except Exception:
        print 'MySQLdb is installing,please wait...'
        for cmd in ['pip install MySQL-python','yum -y install mysql-devel']:
            res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            res.wait()
        print 'MySQLdb has been installed!'

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
                
    if mode == 's':
        if socket_mode == 't':
            TcpStatusServer().TcpServer()
        else:
            UdpStatusServer().UdpServer()
    else:
        InstallMsqldb()
        local_ip = GetIp().CatchIp()
        tablename = IpTransform(local_ip)+'_'+socket_mode
        Account().CreatTables(tablename)
        if socket_mode == 't':
            TcpStatusAgent(ServerIp).TcpAgent(tablename)
        else:
            UdpStatusAgent(ServerIp).UdpAgent(tablename)
