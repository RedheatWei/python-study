#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年5月4日
Email: weipeng@sinashow.com
@author: Redheat
That's not a good idea!
'''

import json,time


class FileHandle(object):
    'for file read or write'
    
    def __init__(self,file_name,log):
        self.file_name = file_name
        self.log = log
    
    def log_write_a(self):
        f = open(self.file_name,'a')
        json.dump(self.log,f)
    
    def log_write_w(self):
        f = open(self.file_name,'w')
        json.dump(self.log,f)
        
    def log_read(self):
        f = open(self.file_name)
        log_content = json.load(f)
        return log_content


class login(object):
    'for login check'
    error = 0
    file_name = 'account.log'
    while True:
        file_read = FileHandle(file_name)
        info_dict = file_read.log_read()
        username = raw_input('Enter your card id:')
        try:
            passwd = info_dict[username][0]
        except KeyError:
            print 'Have no card id: %s' % username
            continue
        else:
            while info_dict[username][-1] == 'act':
                passwd_enter = raw_input('Enter your password:')
                if passwd_enter == passwd:
                    return ('1',username)
                else:
                    error += 1
                    print 'Password error: %s' % error
                    while error > 2:
                        info_dict[username][-1] = 'loc'
                        file_write = FileHandle(file_name,info_dict)
                        file_write.log_write_w()
                        print 'Card id %s has been locked!' % username
                        break
            else:
                print 'Your card id %s has been locked!' % username
                continue

class balance_info():
    'for query balance info '
    file_name = 'balance.log'
    def __init__(self,cost):
        self.cost = cost
        
    def custom(self):
        return self.cost
    
    def counter_fee(self):
        return self.cost * (1 + 5.0/100)

class shopping():
    shop_list = '''1.'''






user_info = {'10750':['admin','act']}

log_id = login
while log_id[0] == '1':
    username = log_id[-1]
#显示余额，距离还款日等信息
    menu_list = '''
    1.to shopping
    2.take cash
    3.check bill
    4.repayment
    Enter a choice:'''
    choice = raw_input(menu_list).split().lower()
    while choice = '1':
        







