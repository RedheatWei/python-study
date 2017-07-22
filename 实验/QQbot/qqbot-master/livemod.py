#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年10月21日
Email: weipeng@sinashow.com
@author: Redheat

'''
import urllib2,json,time
room_id = 5232509

class LiveModelFunc(object):
    def __init__(self,room_id):
        self.room_id = room_id
        self.time_str = time.strftime("%Y%m%d%H%M", time.localtime())
    def openUrl(self,url_str,isjson):
        for i in range(3):
            try:
                html_res = urllib2.urlopen(url_str)
            except Exception,e:
                time.sleep(3)
            else:
                if isjson:
                    return html_res.read()
                else:
                    return True
        return False
    def checkLiveStartJson(self):
        url_str = 'http://www.quanmin.tv/json/rooms/%s/info4.json?_t=%s' % (self.room_id,self.time_str)
        json_str = self.openUrl(url_str,True)
        # print json_str
        if json.loads(json_str)['video'] == "":
            return False
        else:
            return True
    def checkLiveStartVideo(self):
        url_str = "http://livebd.quanmin.tv/live/%s.flv" % (self.room_id)
        return self.openUrl(url_str,False)


# live = LiveModelFunc(room_id)
# print live.checkLiveStartVideo()
