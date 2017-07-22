#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月21日
Email: weipeng@sinashow.com
@author: Redheat

'''
import MySQLdb,socket,struct,os,time,subprocess

class MySqlConnect(object):
    'for connect mysql'
    def __init__(self):
        self.conn = MySQLdb.connect(host='183.131.72.142',user='test',passwd='test',db='user_info')
        self.cur = self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    
    def CreatTables(self,):
        self.cur.execute('CREATE TABLE account(user char(20) not null,password char(20) not null,UNIQUE (user))')
    
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
        
    def AddUser(self,username,password):
        sql = 'insert into account(user,password) values("%s","%s")' % (username,password)
        self.__mysql.Handle(sql)
    
    def DelUser(self,username):
        sql = 'delete from account where User="%s"' % username
        self.__mysql.Handle(sql)
        
    def GetUser(self,username):
        sql = 'select * from account where user="%s"' % username
        user_info = self.__mysql.Select(sql)
        return user_info
    
class ShowInfo():
    'for check user info'
    def __init__(self,username):
        self.user_info = Account().GetUser(username)
    
    def CheckUser(self):
        if self.user_info is None:
            return False
        else:
            return True
    
    def CheckPassword(self,password):
        if self.user_info['password'] == password:
            return True
        else:
            return False

def UserLogin():
    HOST = ''
    PORT = 10751
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            tcpSerSock.bind(ADDR)
            tcpSerSock.listen(5)
        except Exception,e:
            print e
            time.sleep(3)
            continue
        else:
            while True:
                tcpCliSock,addr = tcpSerSock.accept()
                while True:
                    try:
                        rec = tcpCliSock.recv(BUFSIZE)
                    except Exception,e:
                        print e
                        continue
                    else:
                        username = rec.split()[0]
                        password = rec.split()[1]
                        if ShowInfo(username).CheckUser() is True:
                            if ShowInfo(username).CheckPassword(password) is True:
                                tcpCliSock.send('True')
                                break
                            else:
                                tcpCliSock.send('Flase')
                                continue
                        else:
                            tcpCliSock.send('Flase')
                            continue
                    
                        
def ShowFile():
    HOST = ''
    PORT = 10752
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            tcpSerSock.bind(ADDR)
            tcpSerSock.listen(5)
        except Exception,e:
            print e
            time.sleep(3)
            continue
        else:
            while True:
                tcpCliSock,addr = tcpSerSock.accept()
                while True:
                    try:
                        rec = tcpCliSock.recv(BUFSIZE)
                    except Exception,e:
                        print e
                        continue
                    else:
                        res = subprocess.Popen(rec,shell=True,stdout=subprocess.PIPE)
                        res.wait()
                        data = res.stdout.read()
                        tcpCliSock.send(data)
                        continue

def GetFile():
    HOST = ''
    PORT = 10753
    BUFSIZE = 1024
    ADDR = (HOST,PORT)
    tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            tcpSerSock.bind(ADDR)
            tcpSerSock.listen(5)
        except Exception,e:
            print e
            time.sleep(3)
            continue
        else:
            while True:
                tcpCliSock,addr = tcpSerSock.accept()
                while True:
                    try:
                        rec = tcpCliSock.recv(BUFSIZE)
                        rec_len = rec.split()[-1]
                        rec_filename = rec.split()[0]
                    except Exception,e:
                        print e
                        continue
                    else:
                        tcpCliSock,addr = tcpSerSock.accept()
                        while True:
                            f = open(rec_filename,'ab')
                            while True:
                                if rec_len > 1024:
                                    rec = tcpCliSock.recv(BUFSIZE)
                                else:
                                    rec = tcpCliSock.recv(rec_len)
                                    f.write(rec)
                                    f.close()
                                    break
                                rec_len -= 1024
                                f.write(rec)
                                continue


    
    

