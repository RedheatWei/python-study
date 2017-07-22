#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年8月25日
Email: weipeng@sinashow.com
@author: Redheat

'''
import os
import re
import sys
import json
import time
import getopt
import urllib2
import tornado.web
import tornado.ioloop

def Auth_get(url,header):
    data = json.dumps({"jsonrpc":"2.0","method":"user.login","params":{"user":"zabbix","password":"QO7C0uZWVAnnepQPEqzpZ7Bv"},"id":0})
    
    request = urllib2.Request(url,data)
    for key in header:
        request.add_header(key,header[key])
    try:
        result = urllib2.urlopen(request)
    except urllib2.URLError as e:
        print "Auth Failed,Please Check Your Name And Password:",e.code
    else:
        response = json.loads(result.read())
        result.close()
        return response['result']

def Host_get(url,header,auth):
    hostinfos = {}
    data = json.dumps({"jsonrpc":"2.0","method":"host.get","params":{"output":["hostid","status","name","host"]},"auth":auth,"id":1})
    request = urllib2.Request(url,data)
    
    for key in header:
        request.add_header(key,header[key])

    try:
        result = urllib2.urlopen(request)
    except Exception,e:
        pass
    else:
        response = json.loads(result.read())
        result.close()
        hostinfo =  response['result']
        for host in hostinfo:
            infos = {}
            infos['status'] = host['status']
            infos['HostName'] = host['name']
            
            hostinfos[host['host']] = infos
    
    return hostinfos

def Tigger_get(url,header,auth):
    Trigger_info = {}
    data = json.dumps(
    {
        "jsonrpc":"2.0",
        "method":"trigger.get",
        "params":{
                  "monitored":1,
                  "skipDependent":1,
                  "filter":{"value":1},
                  "output":["description",'lastchange'],
                  "selectHosts":['host','name'],
                 },
        "auth":auth,
        "id":1})
    
    request = urllib2.Request(url,data)
    for key in header:
        request.add_header(key,header[key])

    def gettype(message):
        Trigger_type= ""
        
        if "network traffic on" in message:
            Trigger_type = "流量报警"    
        elif "Free disk space is less" in message and "Physical Memory" not in message:
            Trigger_type = "磁盘报警"
        elif "/etc/passwd has been changed" in message:
            Trigger_type = "文件报警"
        elif "Processor load is too high" in message:
            Trigger_type = "负载报警"
        elif "is unreachable for " in message or "unavailable by ICMP" in message:
            Trigger_type = "宕机报警"
        else:
            return
            
        return Trigger_type


    try:
        result = urllib2.urlopen(request)
    except Exception,e:
        pass
    else:
        response = json.loads(result.read())
        result.close()
        hostinfos = response['result']
        for host in hostinfos:
            Time = time.strftime("%Y:%m:%d %H:%M:%S",time.localtime(int(host['lastchange'])))
            mess = host['description']
            if "{HOST.NAME}" in mess:
                mess = re.sub("{HOST.NAME}",host['hosts'][0]['name'],mess)
            ip = host['hosts'][0]['host']
            type = gettype(mess)
            if type:
                content = []
                type = gettype(mess)
                infos = {"mess":mess,"Time":Time,"type":type}
            
                if Trigger_info.get(ip):
                    content.append(infos)
                    Trigger_info[ip] += content
                else:
                    content.append(infos)
                    Trigger_info[ip] = content


    return Trigger_info

class GetHostList(tornado.web.RequestHandler):
    def get(self):
        args = self.request.arguments
        info = Host_get(url,header,auth)
        self.write(json.dumps(info))
    
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')
        
class GetTiggerInfo(tornado.web.RequestHandler):
    def get(self):
        starttime = time.time() - 5*60
        endtime = time.time()

        args = self.request.arguments
        info = Tigger_get(url,header,auth)
        if len(info) == 0:
            self.write(json.dumps({'0.0.0.0':{"mess": "null", "type": "null", "Time": "null"}}))
        else:
            self.write(json.dumps(info))
    
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

if __name__ == "__main__":

    url = "http://10.192.17.199/api_jsonrpc.php"
    header = {"Content-Type":"application/json"}
    #auth = Auth_get(url,header)
    auth = '5b0b948ac843512ba89ebd26d3d0491f'
    
    '''将程序放在后台执行, 0: 不放在后台; 1: 放在后台'''
    damoe = 1
    if damoe ==1:
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError,e:
            print >> sys.stderr,"fork #1 failed: %d (%s)" % (e.errno,e.strerror)
            sys.exit(1)
        os.setsid()
        os.umask(0)

    application = tornado.web.Application([
        (r'/get_host_list.fcgi',GetHostList),
        (r'/get_tigger_info.fcgi',GetTiggerInfo)
    ])

    if len(sys.argv) < 2:
        print 'param is error'
        sys.exit(0)
    
    try:
        opts,args = getopt.getopt(sys.argv[1:],"p:")
    except Exception,e:
        print str(e)
        sys.exit(2)
        
    for opt,arg in opts:
        if opt in ("-p"):
            port = arg
        else:
            print "unknown options"
            sys.exit(0)

    application.listen(int(port), "0.0.0.0")
    tornado.ioloop.IOLoop.instance().start()

