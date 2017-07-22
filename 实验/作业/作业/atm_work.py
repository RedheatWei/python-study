#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月11日
Email: weipeng@sinashow.com
@author: Redheat

'''
import json,time

class AboutUser(object):
    '''This is a class for user info.You can user this class creat or delete a user even change a user's lock state.'''
    user_info_file = 'user_info'
    user_info_dict = {}
    def __init__(self,username='username',password='password',state='act'):
        self.username = username
        self.password = password
        self.state = state
    
    def CheckUserInfo(self):
        try:
            f = open(self.user_info_file)
        except IOError:
            return 0
        else:
            user_info_dict = f.json.load()
            return user_info_dict
    def RePassword(self,username):
        self.user_info_dict = self.CheckUserInfo()
        if self.username in self.user_info_dict.has_key():
            if self.user_info_dict[self.username]['static'] == 'act':
                return self.user_info_dict[self.username]['password']
            else:
                return 2
        else:
            return 1
    def CreatNewUser(self):
        if self.username not in 








if AboutUser.CheckUserInfo() == 0:
    print 'Have no user,creat new:\n'
    if 
    


    