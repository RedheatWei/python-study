#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/28 14:50'
@email = 'qjyyn@qq.com'
'''


class ContextIllustration:
    def __enter__(self):
        print("entering context")

    def __exit__(self, exc_type, exc_val, traceback):
        print("leaving context")

        if exc_type is None:
            print("with no error")
        else:
            print("with an error (%s)" % exc_val)


with ContextIllustration():
    print("inside")

with ContextIllustration():
    raise RuntimeError("raised within 'with'")
