#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月24日
Email: weipeng@sinashow.com
@author: Redheat

'''
import MySQLdb,sys

class MySqlConnect(object):
    'for connect mysql'
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='login')
        self.cur = self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        
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
                   
    def GetUser(self,username):
        sql = 'select acct from accounts where login="%s"' % username
        user_info = self.__mysql.Select(sql)
        return user_info
     
class MySqlUpdate(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='game')
        self.cur = self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        
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

class Game(object):
    'for add or del user'
    def __init__(self):
        self.__mysql = MySqlUpdate()
                   
    def UpdateGold(self,id):
        sql = 'update characters set gold=99999999 where acct=%s' % id
        user_info = self.__mysql.Handle(sql)
        return user_info    

username = sys.argv[1]        
id = Account().GetUser(username)
print id
print Game().UpdateGold(id)
