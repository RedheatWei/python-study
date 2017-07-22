import time
while True:
    name = raw_input('login desired: ')
    now_login = time.time()
    try:
        test_open = file('passwd','r')
        for each_line in test_open.readlines():
            user_name = []
            user_name.append(each_line.split()[0].strip('\n'))
            print user_name
            if name in user_name:
                print 'name taken,try anther: '
                test_open.close()
                continue    
            else:
                pwd = raw_input('Enter your password(1): ')
                f = file('passwd','a')
                f.write('%s %s %s \n' % (name,pwd,now_login))
                f.close()
    #                    break
    except IOError,e:
        pwd = raw_input('Enter your password(2): ')
        f = file('passwd','a')
        f.write('%s %s %s \n' % (name,pwd,now_login))
        f.close()