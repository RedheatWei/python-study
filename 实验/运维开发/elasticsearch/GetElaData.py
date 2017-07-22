#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年6月13日
Email: weipeng@sinashow.com
@author: Redheat

'''
import sys,time
import urllib2,json

#########配置项#########
ELA_HOST='http://127.0.0.1:9200/'
HAN_INDEX_INCLUDE = ['web'] #定义要处理的索引必须包含的词
FILED_LIST = ['clientip','xff','request','response']  #收集的内容
DELETE_TIME = 1 #保留日志的天数
IS_DENY_INDEX=True#true or false.定义LIST_INDEX里放的到底是被拒绝的索引还是被允许的索引
LIST_INDEX = ['.marvel-es-data-1']
LOG_NAME = 'log_getElaData.log' #日志名
#########配置项#########

#获取报错时所在的模块
def get_cur_info():
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    return f.f_code.co_name
#log记录模块
def log_write(text):
    try:
        f = open(LOG_NAME,'a')
        f.write(time_now() +' '+ text + '\n')
        f.close()
    except Exception:
        pass
#当前时间        
def time_now():
    return time.strftime('%Y-%m-%d %H:%M:%S')        
#http请求的几种方式
class HttpMethod(object):
    '''define http method about get put post delete'''
    #get
    def http_get(self,ref=None):
        url=ELA_HOST+ref
        try:
            response = urllib2.urlopen(url)
            log_write('get %s success' % url)
        except Exception,e:
            log_write("get %s error. Module : %s. %s : %s." % (url,get_cur_info(),Exception,e))
        else:
            return response.read()
    #post
    def http_post(self,ref=None,values={}):
        url=ELA_HOST+ref
        jdata = json.dumps(values)
        try:
            request = urllib2.Request(url, jdata)
            request.get_method = lambda:'POST'
            response = urllib2.urlopen(request)
            log_write('post %s success' % url)
        except Exception,e:
            log_write("post %s error. Module : %s. %s : %s." % (url,get_cur_info(),Exception,e))
        else:
            return response.read()
    #put
    def http_put(self,ref=None,values={}):
        url=ELA_HOST+ref
        jdata = json.dumps(values)
        try:
            request = urllib2.Request(url, jdata)
            request.get_method = lambda:'PUT'
            request = urllib2.urlopen(request)
            log_write('put %s success' % url)
        except Exception,e:
            log_write("put %s error. Module : %s. %s : %s." % (url,get_cur_info(),Exception,e))
        else:
            return request.read()
    #delete
    def http_delete(self,ref=None,values={}):
        url=ELA_HOST+ref
        jdata = json.dumps(values)
        try:
            request = urllib2.Request(url, jdata)
            request.get_method = lambda:'DELETE'
            request = urllib2.urlopen(request)
            log_write('delete %s success' % url)
        except Exception,e:
            log_write("delete %s error. Module : %s. %s : %s." % (url,get_cur_info(),Exception,e))
        else:
            return request.read()

#获取一些有用的信息
class HanSomeInfo(object):
    def __init__(self):
        self.http = HttpMethod()
    #获取所有索引
    def get_index(self):
        ref = '_stats/indexes'
        jsonget = json.loads(self.http.http_get(ref))
        index_list = []
        if IS_DENY_INDEX:
            for i in jsonget['indices']:
                if i not in LIST_INDEX:
                    index_list.append(i)
        else:
            for i in jsonget['indices']:
                if i in LIST_INDEX:
                    index_list.append(i)
        log_write("all index list get success:%s" % ','.join(index_list))
        return index_list
    #获取字段值
    def get_field(self,index,field,method="_search",size=10):
        ref = index + "/" + method
        datavalue = {"size":0,
             "aggs":{
                 "top-terms-aggregation":{
                  "terms" : {
                         "field" : field,
                         "size" : size
                         }
                  }
             }
         }
        log_write("will get %s data" % field)
        filedstr= self.http.http_post(ref, datavalue)
        filedjson = json.loads(filedstr)
        return filedjson['aggregations']['top-terms-aggregation']['buckets']
    #添加数据
    def post_data(self,index,datavalue={},datatype="unknown"):
        ref = index + "/" +datatype
        return self.http.http_post(ref,datavalue)
    #删除数据
    def delete_data(self,index):
        ref = index
        return self.http.http_delete(ref)
#时间处理
class TimeCalc(object):
    def calc_stamp(self,timestr):
        timearray = time.strptime(timestr, "%Y.%m.%d")
        createtimestamp =  int(time.mktime(timearray))
        return createtimestamp

#索引处理
class IndexHan(object):
    def __init__(self):
        self.index_list  = HanSomeInfo().get_index()
        self.stamp = DELETE_TIME * 60 * 60 * 24
    #需要删除或者统计的索引
    def need_han(self,mode):
        index_list_remove = []
        for i in self.index_list:
            isplit = i.split('-')
            if len(isplit) > 1:
                createtime = isplit[-1]
                if time.time() - TimeCalc().calc_stamp(createtime) < self.stamp:
                    index_list_remove.append(i)
            else:
                index_list_remove.append(i)
        if mode == 'add':
            for j in self.index_list:
                jsplit = j.split('-')
                if len(jsplit) > 1:
                    if jsplit[0] not in  HAN_INDEX_INCLUDE:
                        index_list_remove.append(j)
        index_list = list(set(self.index_list).difference(set(index_list_remove)))
        log_write("need index list get success:%s" % ','.join(index_list))        
        return index_list

#处理数据
class HanData(object):
    #收集数据
    def collect_data(self):
        self.index_list = IndexHan().need_han('add')
        for i in self.index_list:
            indexname = i.split('-')[1]
            createtime = i.split('-')[-1]
            for j in FILED_LIST:
                colldata = HanSomeInfo().get_field(i, j)
                if len(colldata) != 0 :
                    for k in colldata:
                        key = k['key']
                        number = k['doc_count']
                        datavalue = {
                             "time" : createtime,
                             j : key,
                             "index_name" : indexname,
                             "count" : number
                         }
                        log_write("collect data success.")
                        HanSomeInfo().post_data(j, datavalue, j)
                        log_write("add data to %s success" % j)
    #删除没用的数据
    def del_data(self):
        self.index_list = IndexHan().need_han('delete')
        log_write('will delete index list %s' % ','.join(self.index_list))
        for i in self.index_list:
            log_write("will delete %s" % i)
            HanSomeInfo().delete_data(i)
            log_write("delete %s success" % i)
            

log_write("getElaData.py begining run!\n")            
HanData().collect_data()
log_write("collect data success!\n")
HanData().del_data()
log_write("delete data success!\n")