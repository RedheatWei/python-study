#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月1日
Email: weipeng@sinashow.com
@author: Redheat

'''
import MySQLdb,sys
class MySqlConnect(object):
    'for connect mysql'
    def __init__(self):
        while True:
            try:
                self.conn = MySQLdb.connect(host='183.131.72.142',user='network',passwd='redheat@sinashow',db='network_info')
                self.cur = self.conn.cursor()
                break
            except Exception,e:
                print e
                continue
    
    def Select(self,sql):
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data
    def ShowTables(self,sql):
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
    
class Account(object):
    'for add or del user'
    def __init__(self):
        self.__mysql = MySqlConnect()
        
    def GetRate(self,tablename):
        sql = 'select rate from %s order by id desc limit 1' % tablename
        data = self.__mysql.Select(sql)
        return data
    def GetTableName(self):
        sql = 'show tables'
        data = self.__mysql.ShowTables(sql)
        return data
    
def IpTransform(ip):
    return ip.replace('.','_')

parameter = sys.argv[1:]
for i in parameter:
    if len(i) > 1:
        ip = i
    else:
        mode = i
tablename = IpTransform(ip)+'_'+mode
print Account().GetRate(tablename)[0]

#A = Account().GetRate(tablename)
#print A
#ipList = Account().GetTableName()
#for i in ipList:
#    t = i[0].split('_')[-1]
#    if t == 'u':
#        tablename = i[0]
#        print Account().GetRate(tablename)[0],