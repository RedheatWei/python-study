#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月11日
Email: weipeng@sinashow.com
@author: Redheat
ver 2.0
'''
from socket import *
import time


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

#mysqldb三层架构，这里没有用到显示，只用了两层
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

#程序主体，接收数据并判断数据类型插入数据库
#这里用的连接为tcp
class ReceveDataInMysql(object):
    'for receve data in mysql'
    def __init__(self):
        self.HOST = ''
        self.PORT = 21567
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
    
    def TcpReceveForMysql(self):
        tcpSerSock = socket(AF_INET,SOCK_STREAM)
        while True:
            try:
                tcpSerSock.bind(self.ADDR)
                tcpSerSock.listen(5)
            except Exception,e:#绑定套接字失败就会等待30秒再次绑定（比如上个程序意外终止，导致端口被占用）
                print e
                time.sleep(30)
                continue
            else:
                while True:
                    tcpCliSock, addr = tcpSerSock.accept()
                    while True:
                        data_rec = tcpCliSock.recv(self.BUFSIZE)
                        tcpCliSock.close()
                        StateData = data_rec.split()#把接收到的数据转换成列表形式处理
                        mode = StateData[0]
                        time_time = StateData[1]
                        ip_ip = StateData[2]
                        tablename = IpTransform(addr[0])+'_'+mode
                        if mode is 'u':
                            lengh = StateData[3]
                            success = StateData[4]
                            dropped = StateData[5]
                            rate = StateData[6]
                            while True:
                                try:
                                    Account().UdpAdd(tablename, time_time, ip_ip, lengh, success, dropped, rate)#插入mysql
                                except Exception,e:
                                    print e
                                    Account().CreatTables(tablename)
                                    continue
                                break
                        else:
                            delay = StateData[3]
                            time_out = StateData[4]
                            while True:
                                try:
                                    Account().TcpAdd(tablename, time_time, ip_ip, delay, time_out)
                                except Exception,e:
                                    print e
                                    Account().CreatTables(tablename)
                                    continue
                                break
                        break
                tcpSerSock.close()
if __name__ == '__main__':
    ReceveDataInMysql().TcpReceveForMysql()
