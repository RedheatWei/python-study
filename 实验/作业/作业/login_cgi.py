#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年2月13日

@author: Redheat
'''
try:
    open('login', 'r')
except IOError, e:
    open('login', 'w')
    new_login = raw_input('Make a new login name:')
    new_passwd = raw_input('Make a new password:')
    new_passwd_second = raw_input('Please enter your password again:')
    while new_passwd  != new_passwd_second:
        new_passwd = raw_input('The input is not consistent, please input again:')
        new_passwd_second = raw_input('Please enter your password again:')
    else:
        a = 'dict' + new_login
        exec(a+'={new_login:new_passwd}')
        
        
    
#while True:
#    print_name = raw_input('Enter your login name:')
#    print_passwd = raw_input('Enter your password:')
#    fob_login = open('login', 'r')
#    fob_nologin = open('nologin', 'r')
    
    
    