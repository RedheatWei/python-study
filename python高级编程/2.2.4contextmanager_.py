#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/28 15:02'
@email = 'qjyyn@qq.com'
'''
from contextlib import contextmanager

@contextmanager
def context_illustration():
    print("entering context")
    try:
        yield
    except Exception as e:
        print("leaving context")
        print("with an error (%s)" % e)
        raise
    else:
        print("leaving content")
        print("with no error")