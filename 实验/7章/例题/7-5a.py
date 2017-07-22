#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015��2��28��

@author: Redheat
'''
import time

now_login = time.time()

#在passwd内取出包含用户名、密码及上次登陆时间的信息并转换为字典格式
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
#创建一个新用户，如果没有passwd文件，就不检查用户是否存在，如果存在这个文件，就检查用户是否存在。
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

#老用户登陆，核对用户名和密码，如果距离上次登陆时间小于4小时，就提示上次登陆时间
def olduser():
    name = raw_input('login: ')
    pwd = raw_input('Enter your password: ')
    dict_passwd = dict_modul_passwd()
    last_login = float(dict_passwd[name][1])
    if dict_passwd[name][0] == pwd:
        dict_passwd[name][1] = now_login
        fpasswd = file('passwd','wb')
        for key in dict_passwd:
            fpasswd.write('%s %s %s \n' % (key,dict_passwd[key][0],dict_passwd[key][1]))
        fpasswd.close()
#        for line in write_passwd.readlines():
#            if line.split()[0] == name:
#                write_passwd.write('%s %s %f \n' % (name,pwd,time.time()))
#        write_passwd.close()
        print 'welcome back',name
        if now_login - last_login <= 14400:
            timestr = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(last_login))
            print "You already logged in at: <%s>" % timestr      
    else:
        print 'login incorrect'

def showmenu():
    prompt ="""
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
            if choice not in 'neq':
                print 'invalid option,try again'
            else:
                chosen = True
                
        if choice == 'q':done = True
        if choice == 'n':newuser()
        if choice == 'e':olduser()
        
if __name__ == '__main__':
    showmenu()
    