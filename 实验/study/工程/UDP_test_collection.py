#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年3月5日

@author: Redheat
'''
cut_str = 'loast pack ratio'
f = file('sendd.log')
w = file('temp_sendd.log','a')
for line in f.xreadlines():
    if cut_str in line:
        w.write(line)
f.close()
w.close()
  