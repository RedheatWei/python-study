#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年8月31日
Email: weipeng@sinashow.com
@author: Redheat
ver 1.0
用于在数据库中取出数据压缩成json格式供ajax使用
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
#数据库里的表名
ip_list=["61_150_126_10_u","122_141_228_194_u","60_220_213_194_u","60_165_99_207_u","115_236_20_201_u","115_231_78_10_u","183_136_132_10_u","124_95_161_130_u","124_95_165_66_u","182_118_65_130_u"]

for ip in ip_list:
    rate=Account().GetRate(ip)
    time=Account().GetTime(ip)
    ratelist=[]
    timelist=[]
    finalrate=[]
    finaltime=[]
    num=200#num控制每个段的大小，200就是200个一段
    #取出所有数值
    for i in rate:
        aa=i[0]
        ratelist.append(float(aa)*100)
    for i in time:
        bb=i[0]
        timelist.append(float(bb))
    con=1
    t_list=[]
    #按照num进行分段计算
    for i in ratelist:
        if divmod(con, num)[-1] != 0:
            t_list.append(i)
        else:
            finalrate.append(sum(t_list)/len(t_list))
            t_list=[]
        con+=1
    finaltime=timelist[::num]
    #print finalrate,finaltime
    avgrate=sum(ratelist)/len(ratelist)
    print ip,avgrate
    #生成json文件
    json_dict={"datalist":finalrate,"timelist":finaltime}
    f=open(ip,'w')
    json.dump(json_dict,f)
    f.close()
