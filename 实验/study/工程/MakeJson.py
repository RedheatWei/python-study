#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年8月31日
Email: weipeng@sinashow.com
@author: Redheat

'''
import MySQLdb,json

class MySqlConnect(object):
    'for connect mysql'
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='x5xuan',db='network_info')
        self.cur = self.conn.cursor()#cursorclass = MySQLdb.cursors.DictCursor)

    def Select(self,sql):
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


    def GetRate(self,ipname):
        sql = 'select rate from %s' % ipname
        rate_info = self.__mysql.Select(sql)
        return rate_info

    def GetTime(self,ipname):
        sql = 'select time from %s' % ipname
        time_info = self.__mysql.Select(sql)
        return time_info
ip_list=[]
for ip in ip_list:
    rate=Account().GetRate(ip)
    time=Account().GetTime(ip)
    ratelist=[]
    timelist=[]
    finalrate=[]
    finaltime=[]
    num=200
    for i in rate:
        aa=i[0]
        ratelist.append(float(aa)*100)
    for i in time:
        bb=i[0]
        timelist.append(float(bb))
    con=1
    t_list=[]
    for i in ratelist:
        if divmod(con, num)[-1] != 0:
            t_list.append(i)
        else:
            finalrate.append(sum(t_list)/len(t_list))
            t_list=[]
        con+=1
    finaltime=timelist[::num]
    #print finalrate,finaltime
    #avgrate=sum(ratelist)/len(ratelist)
    #print avgrate
    json_dict={"datalist":finalrate,"timelist":finaltime}
    f=open(ip,'w')
    json.dump(json_dict,f)
    f.close()