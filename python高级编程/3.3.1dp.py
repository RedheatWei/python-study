#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/6/11 13:51'
@email = 'qjyyn@qq.com'
'''


class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, instance, value):
        print("updateing", self.name)
        self.val = value


class MyClass(object):
    x = RevealAccess(10, "var x")
    y = 5


m = MyClass()
m.x

m.x = 20
m.x
m.y
