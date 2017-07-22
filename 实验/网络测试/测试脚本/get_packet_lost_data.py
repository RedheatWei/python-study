#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月11日
Email: weipeng@sinashow.com
@author: Redheat
ver 2.0
'''
import MySQLdb,sys
#还是mysqldb的三层架构
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
#查询udp的丢包率        
    def GetRate(self,tablename):
        sql = 'select rate from %s order by id desc limit 1' % tablename
        data = self.__mysql.Select(sql)
        return data
#查询tcp的建立所花时间    
    def GetDelay(self,tablename):
        sql = 'select delay from %s order by id desc limit 1' % tablename
        data = self.__mysql.Select(sql)
        return data

#获取表，暂时没用到        
    def GetTableName(self):
        sql = 'show tables'
        data = self.__mysql.ShowTables(sql)
        return data

#把IP地址中的.换成_    
def IpTransform(ip):
    return ip.replace('.','_')

parameter = sys.argv[1:]
for i in parameter:
    if len(i) > 1:
        ip = i
    else:
        mode = i
        
tablename = IpTransform(ip)+'_'+mode
if mode is 'u':
    print Account().GetRate(tablename)[0]
else:
    if Account().GetDelay(tablename)[0] != 'None':
        print Account().GetDelay(tablename)[0]
    else:#如果建立时间是None，那么肯定是超时了，这里设置的默认时间为3秒（没有tcp连接需要建立3秒钟，那肯定早就超时了）
        print '3'
