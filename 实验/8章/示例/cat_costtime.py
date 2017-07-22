#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��3��10��

@author: Redheat
'''
key_str = 'Cost time'
f = file('D:\UCChatHall-445588-12366-201503100520.log')
for line in f.xreadlines():
    if key_str in line:
        A = line.strip('\n').split(',')
        print A[-1],A[-2]
f.close()
#        print A[-1]
        
    