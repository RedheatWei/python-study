#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年6月29日
Email: weipeng@sinashow.com
@author: Redheat

'''
from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR='smtp.qq.com'
POP3SVR='pop.qq.com'

origHdrs = ['From:qjyyn@qq.com','To:qjyyn@vip.qq.com','Subject:test msg']
origBody = ['xxx','yyy','zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('qjyyn@qq.com', 'qjyyn@vip.qq.com', origMsg)
sendSvr.quit()

assert len(errs) == 0,errs
sleep(10)
