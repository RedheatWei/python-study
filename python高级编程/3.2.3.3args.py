#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/31 11:41'
@email = 'qjyyn@qq.com'
'''


class CommonBase:
    def __init__(self):
        print("CommonBase")
        super().__init__()


class Base1(CommonBase):
    def __init__(self):
        print("Base1")


class Base2(CommonBase):
    def __init__(self, arg):
        print("Base2")
        super().__init__()


class MyClass(Base1, Base2):
    def __init__(self, arg):
        print("my base")
        super().__init__(arg)


MyClass(1)
