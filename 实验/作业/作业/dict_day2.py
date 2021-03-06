#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年4月3日

@author: Redheat
'''
import sys

file_name = 'dict_day2'

def write_message(file_name,info_content):
    f = open(file_name,'a')
    f.write(info_content)
    f.close()
    
    
def read_message(file_name):
    f = open(file_name)
    all_message = f.readlines()
    f.close()
    return all_message

def serch_message(all_message):
    dict_message = {}
    for line in all_message:
#        print '%s' % line,
        dict_message[line.split()[0]] = line.split()[1:]
    return dict_message


print 'Welcome to message manager system:'
pr = '''

(S)erch a number.
(A)dd a new message.
(Q)uit.

Enter a choice:'''
while True:
    while True:
        try:
            choice = raw_input(pr).split()[0].lower()
        except (EOFError,KeyboardInterrupt,ImportError):
            choice = 'q'
        if choice not in 'saq':
            print 'Invalid option,try again\n'
        else:
            break
    while choice == 'a':
        message_number = raw_input('\nEnert a new number(enter a "." to exit):')
        if message_number != '.':
            message_info = raw_input('''message number has been creat,please enter 
部门 姓名 邮箱   职位 手机    \n''') 
            info_content = message_number+' '+message_info+'\n'
    
            write_message(file_name, info_content)
            print '%s creat success!' % message_number
        else:
            break
    
    while choice == 's':
        all_message = read_message(file_name)
        dict_message = serch_message(all_message)
        message_number = raw_input('\nEnter a number(enter a "." to exit):')
        if message_number != '.':
            for key in dict_message:
                if message_number in key :
                    print '工号：%-10s 部门 :%-10s 姓名 :%-10s 邮箱 :%-10s 职位:%-10s 电话 :%-10s' % (key,dict_message[key][0],dict_message[key][1],dict_message[key][2],dict_message[key][3],dict_message[key][4])
        else:
            break
    
    while choice == 'q':
        print 'Quit success!'
        sys.exit()
