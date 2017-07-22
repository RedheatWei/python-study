#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��3��4��

@author: Redheat
'''
import time
from random import choice

now_login = time.time()

def update_user_account():
    fpasswd = file('passwd','wb')
    for key in dict_passwd:
        fpasswd.write('%s %s %s \n' % (key,dict_passwd[key][0],dict_passwd[key][1]))
    fpasswd.close()
    

#��passwd��ȡ�������û��������뼰�ϴε�½ʱ�����Ϣ��ת��Ϊ�ֵ��ʽ
def dict_modul_passwd():
    r = file('passwd')
    dict_passwd = {}
    for each_line in r.readlines():
        user_name = each_line.split()[0].strip('\n')
        user_passwd = each_line.split()[1].strip('\n')
        last_login = each_line.split()[2].strip('\n')
        dict_passwd[user_name] = [user_passwd,last_login]
    r.close()
    return dict_passwd
#����һ�����û������û��passwd�ļ����Ͳ�����û��Ƿ���ڣ������������ļ����ͼ���û��Ƿ���ڡ�
def newuser():
    while True:
        name = raw_input('login desired: ')
        now_login = time.time()
        try:
            dict_passwd = dict_modul_passwd()
            if dict_passwd.has_key(name):
                print 'name taken,try anther: '
                continue          
            else:
                pwd = raw_input('Enter your password: ')
                f = file('passwd','a')
                f.write('%s %s %f \n' % (name,pwd,now_login))
                f.close()
                break
        except IOError,e:
            pwd = raw_input('Enter your password: ')
            f = file('passwd','a')
            f.write('%s %s %f \n' % (name,pwd,now_login))
            f.close()
            break

#���û���½���˶��û��������룬��������ϴε�½ʱ��С��4Сʱ������ʾ�ϴε�½ʱ��
def olduser():
    name = raw_input('login: ')
    pwd = raw_input('Enter your password: ')
    dict_passwd = dict_modul_passwd()
    last_login = float(dict_passwd[name][1])
    if dict_passwd[name][0] == pwd:
        dict_passwd[name][1] = now_login
        update_user_account()
        print 'welcome back',name
        if now_login - last_login <= 14400:
            timestr = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(last_login))
            print "You already logged in at: <%s>" % timestr      
    else:
        print 'login incorrect'
        
def delete():
    dict_passwd = dict_modul_passwd()
    account_name = []
    for key in dict_passwd:
        account_name.append(key)
    name = raw_input('''
account has: %s
Delete an account:''' % ' '.join(account_name))
    for key in dict_passwd:
        if name in account_name:
            del dict_passwd[name]
        else:
            print 'No account %s' % name
            break
    update_user_account()

def show_user():
    dict_passwd = dict_modul_passwd()
    for key in dict_passwd:
        print key,dict_passwd[key][0]
        
def previous():
    showmenu()
    
    

def admin():
    prompt_next = '''
(D)elete
(S)how
(P)revious
'''
    choice = raw_input(prompt_next).strip()[0].lower()
    if choice not in 'dsp':
        print 'invalid option'
    else:
        print '\nYou picked: [%s]' % choice
    if choice == 'd':delete()
    if choice == 's':show_user()
    if choice == 'p':previous()
    
        
def showmenu():
    prompt ="""
(A)dministrator
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice:"""

    done = False
    while not done:
        
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'neqa':
                print 'invalid option,try again'
            else:
                chosen = True
                
        if choice == 'q':done = True
        if choice == 'n':newuser()
        if choice == 'e':olduser()
        if choice == 'a':admin()
        
if __name__ == '__main__':
    showmenu()
    