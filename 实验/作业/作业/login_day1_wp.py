#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月1日
该程序有个bug，就是如果有多个用户的话，进行锁定时会写入错误的用户信息格式，但程序中只设置了创建单个用户，所以便没有修改这个bug。
要修改也比较简单，只需要count后面加一个换行符就可以解决此问题。
@author: Redheat
'''

import sys #载入sys模块

def write_log(file_name,count):#定义写日志函数，此函数为追加模式
    f = file(file_name,'a')
    f.write(count)
    f.close()

def read_log(file_name):#定义读文件函数。
    f = file(file_name)
    user_log = f.readlines()
    f.close()
    return user_log

file_name = 'login_day1'
user_key = 'act'
user_key_lock = 'lock'
user_dict = {}
user_id_list = [] 
error = 0

try:#尝试打开文件
    user_log = read_log(file_name)
    user = raw_input('Enter your username:')
    for line in user_log:#讲文件内的用户id等信息转换为字典，key是用户id，值是密码和锁定状态的列表
        userid = line.split()[0]
        user_id_list.append(userid)
        user_dict[userid] = line.split()[1:]
    if user in user_id_list and user_dict[user][-1] == user_key:#如果用户存在并且没有锁定
        while error < 3:#定义输错三次
            passwd_user = raw_input('Enter your password:')
            if passwd_user == user_dict[user][0]:#判断密码
                print 'Login success! Welcome back, %s' % user
                break
            else:
                error += 1
                print 'Login failure: passwd error %s!' % error
        else:
            user_dict[user][-1] = user_key_lock#在内存中讲user值改为锁定
            f = file(file_name,'w')#清空文件，准备重新写入
            f.close()
            for user in user_id_list:#逐用户写入信息
                count = user+' '+user_dict[user][0]+' '+user_dict[user][-1]
                write_log(file_name, count)
            print '%s has been locked!' % user
    elif user in userid:#用户名正确但是锁定了
        print 'Userid named %s has been locked!' % user
        sys.exit()
    else:#没被锁定，那就是用户名错误
        print 'have no userid named %s' % user
        sys.exit()

except IOError,e:#如果不存在用户信息文件
    user = raw_input('Creat a new userid:')
    while True:#死循环，让用户不断输入密码来判断，直到两个密码都正确
        passwd = raw_input('Enter a passwd')
        passwd_sec = raw_input('Enter a passwd again')
        if passwd != passwd_sec:
            print 'Error:Twince input is not consistent!'
            continue#跳出本次循环
        else:
            break#正确了就不用循环了
    count = user+' '+passwd+' '+user_key
    write_log(file_name, count)
        
