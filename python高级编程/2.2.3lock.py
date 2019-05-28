#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/28 14:11'
@email = 'qjyyn@qq.com'
'''
from threading import RLock

lock = RLock()


def synchronized(function):
    def _synchronized(*args, **kw):
        lock.acquire()
        try:
            return function(*args, **kw)
        finally:
            lock.release()
        return _synchronized


@synchronized
def thread_safe():
    pass
