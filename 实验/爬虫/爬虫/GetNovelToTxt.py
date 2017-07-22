#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年7月23日
Email: weipeng@sinashow.com
@author: Redheat

'''
import urllib2,re


response = urllib2.urlopen('http://www.44pq.com/read/15/15021/') 
html = response.read()

def FileWrite(text):
    f = open('sihai.txt','a')
    f.write(text)
    f.close()

def HandleText(url2):
    url = 'http://www.44pq.com/read/15/15021/'+url2
    res = urllib2.urlopen(url)
    text = res.read()
    for i in text.split('<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;'):
        try:
            text = i.decode('gbk').encode('utf-8')+'\n'
#            print text
            FileWrite(text)
        except Exception,e:
            print e
            pass

for i in html.split('<td class="ccss">'):
    m = re.search('\d{7}\.html',i)
    if m is not None:
        url2 = m.group()
        HandleText(url2)
        continue
    else:
        continue
   
