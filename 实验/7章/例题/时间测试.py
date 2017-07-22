import time

now_login = time.time()

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

def olduser():
    name = raw_input('login: ')
    pwd = raw_input('Enter your password: ')
    dict_passwd = dict_modul_passwd()
    last_login = float(dict_passwd[name][1])
    if dict_passwd[name][0] == pwd:
        print 'welcome back',name
        print dict_passwd
        dict_passwd[name][1] = time.time()
        print dict_passwd
        print now_login - last_login
#        if now_login - last_login <= 14400:
#            timestr = time.strftime('%Y-%m-%d %H:%M:%S',last_login)
#            print "You already logged in at: <%s>" % timestr            
    else:
        print 'login incorrect'
        
olduser()