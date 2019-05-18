#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/18 14:16'
@email = 'qjyyn@qq.com'
'''
import os
'''
进程派生
https://foofish.net/thread-and-process.html
'''
print('当前进程:%s 启动中 ....' % os.getpid())
pid = os.fork()
if pid == 0:
    print('子进程:%s,父进程是:%s' % (os.getpid(), os.getppid()))
else:
    print('进程:%s 创建了子进程:%s' % (os.getpid(), pid))
