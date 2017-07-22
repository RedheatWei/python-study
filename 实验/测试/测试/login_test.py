#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月2日

@author: Redheat
'''

user = 'root'
passwd = 'admin'
error = 0

user_id = raw_input('Enter your username:')

while error < 3:
    password = raw_input('Enter your paswd:')
    if passwd != password:
        error += 1
        print 'Login failed! Error %s' % error
        continue
    else:
        print 'Login success!'
        break
else:
    print 'user %s login failed!' % user