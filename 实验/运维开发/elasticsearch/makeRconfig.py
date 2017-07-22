#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年6月27日
Email: weipeng@sinashow.com
@author: Redheat
'''

def readfile(filename):
    f = open(filename,'r')
    con = f.readlines()
    f.close()
    return con;

def clientconf(filename):
    text = readfile(filename)
    for line in text:
        linelist = line.split()
        print '''input(type="imfile" File="/data0/logs/%s/%s" Tag="%s-%s" Severity="info")''' % (linelist[1],linelist[0],linelist[2],linelist[1][0])
        
def serverconf(filename):
    text = readfile(filename)
    for line in text:
        linelist = line.split()
        print '''if ($syslogtag == '%s-%s') then { action(type="omelasticsearch" server="127.0.0.1" serverport="9200" template="%s-access" searchIndex="%s" searchType="%s" bulkmode="on" queue.type="linkedlist" queue.size="5000" queue.dequeuebatchsize="300" action.resumeretrycount="-1" dynSearchIndex="on")}''' % (linelist[2],linelist[1][0],linelist[1],linelist[3],linelist[1])

def servertem(filename):
    text = readfile(filename)
    for line in text:
        linelist = line.split()
        print '''template(name="%s" type="list"){ constant(value="%s-") property(name="timereported" dateFormat="rfc3339" position.from="1" position.to="4") constant(value=".") property(name="timereported" dateFormat="rfc3339" position.from="6" position.to="7") constant(value=".") property(name="timereported" dateFormat="rfc3339" position.from="9" position.to="10") }''' % (linelist[3],linelist[3])
# clientconf('e:/file.txt')
serverconf('e:/file.txt')
# servertem('e:/file.txt')