#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月11日
Email: weipeng@sinashow.com
@author: Redheat

'''

import json,time




class UserAbout(object):
    '''This is a class for user info.You can user this class creat or delete a user even change a user's lock state.'''
#    def __init__(self,username,password):
#    self.username = username
#    self.password = password
    user_info_file = 'info_file.log'
    user_info_dict = {}
    def __InputUserName(self):
        username = raw_input('Enter your user name:')
        return username
    class __CreatUserInfo(object):
        def __init__(self,username,password,state):
            self.username = username
            self.password = password
            self.state = state
            self.user_info_file = UserAbout.user_info_file
        def __CreatInfo(self):
            self.user_info_dict = UserAbout.user_info_dict
            self.user_info_dict[self.username] = {self.username:[self.password,self.state]}
            f = open(self.user_info_file,'a')
            f.json.dump(self.user_info_dict)
            f.close()
        def __NewUser(self):
            self.__CreatInfo = UserAbout.__CheckUserInfo.__CreatInfo
            self.__CreatInfo
        
        def __ChangeUserInfo(self):
            f = open(self.user_info_file)
            user_dict = f.json.load()
            f.close()
#            user_dict[self.username] = {self.username:[self.password,self.state]}
            self.
                
    def __CheckUserInfo(self):
        try:
            f = open(self.user_info_file)
        except IOError:
            
        username = UserAbout.__InputUserName(self)
        