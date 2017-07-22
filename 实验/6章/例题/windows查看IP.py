#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��2��26��

@author: Redheat
'''
import wmi
c = wmi.WMI()
for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
    print interface.IPAddress,interface.DNSServerSearchOrder,interface.caption