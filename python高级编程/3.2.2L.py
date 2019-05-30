#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/29 14:30'
@email = 'qjyyn@qq.com'
'''
class CommobBase:
    def method(self):
        print("CommonBase")

class Base1(CommobBase):
    pass

class Base2(CommobBase):
    def method(self):
        print("base2")
class MyClass(Base1,Base2):
    pass

def L(klass):
    return [k.__name__ for k in klass.__mro__]

print(L(MyClass))