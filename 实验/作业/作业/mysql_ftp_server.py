#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月18日
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
        
class Socket_Server(object):
    'for socket send or receve'
    def __init__(self):
        self.HOST = ''
        self.PORT = 10751
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST,self.PORT)
        
    
    def UserReceve(self):
        try:
            self.tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            while True:
                try:
                    self.tcpSerSock.bind(self.ADDR)
                    self.tcpSerSock.listen(5)
                except Exception,e:
                    print e
                    time.sleep(3)
                    continue
                else:
                    while True:
                        tcpCliSock,addr = self.tcpSerSock.accept()
                        while True:
                            try:
                                rec = tcpCliSock.recv(self.BUFSIZE)
                                if len(rec.split()) == 3:
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
                                else:
                                    if rec == 'ls':
                                        res = subprocess.Popen(rec,shell=True,stdout=subprocess.PIPE)
                                        res.wait()
                                        data = res.stdout.read()
                                        tcpCliSock.send(data)
                                        continue
                            except Exception,e:
                                tcpCliSock.close()
                                self.tcpSerSock.close()
                                
                                
                                
        except Exception,e:
            self.tcpSerSock.close()
            tcpCliSock.close()
            print e
            
#    def InfoReceve(self):
#        try:
#            self.tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#            self.tcpSerSock.bind(self.ADDR)
#            self.tcpSerSock.listen(5)
#        except Exception,e:
#            print e
#            time.sleep(3)
#        else:
#            while True:
#                tcpCliSock,addr = self.tcpSerSock.accept()
#                while True:
#                    rec = tcpCliSock.recv(self.BUFSIZE)
#                    tcpCliSock.close()
#                    self.tcpSerSock.close()
#                    return rec
                             
            
    def InfoSend(self,data):
#        self.tcpClisock.timeout(1)
        try:
            self.tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.tcpSerSock.connect(self.ADDR)
        except Exception,e:
            print 'Error:%s' % e
        else:
            self.tcpSerSock.send(data)
            rec = self.tcpSerSock.recvfrom(self.BUFSIZE)
            return rec
    def FileSend(self,filename):
        self.tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcpClisock.timeout(1)
        try:
            self.tcpClisock.connect(self.ADDR)
        except Exception,e:
            print 'Error:%s' % e
        else:
#            FILEINFO_SIZE = struct.calcsize('128sI')
            data = struct.pack('128sI',filename,os.stat(filename).st_size)
            self.tcpClisock.send(data)
            fp = open(filename,'rb')
            while True:
                data = fp.read(self.BUFSIZE)
                if not data:
                    break
                self.tcpClisock.send(data)
            fp.close()
            
    def FileReceve(self,filename):
        self.tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcpSerSock.bind('',10751)
        self.tcpSerSock.listen(5)
        while True:
            self.tcpCliSock,self.addr = self.tcpSerSock.accept()
            fp = open(filename,'ab')
            while True:
                rec = self.tcpClisock.recv(self.BUFSIZE)
                fp.write(rec)
            fp.close()

    def __del__(self):
        self.tcpSerSock.close()
   

while True:
    Socket_Server().UserReceve()
    break
    while True:
        print Socket_Server().InfoReceve()
            
        

