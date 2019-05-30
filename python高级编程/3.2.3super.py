#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/30 16:01'
@email = 'qjyyn@qq.com'
'''


class B:
    def __init__(self):
        print("B")
        super().__init__()


class A:
    def __init__(self):
        print("A")
        super().__init__()


class C(A,B):
    def __init__(self):
        print("C")
        A.__init__(self)
        B.__init__(self)


print([x.__name__ for x in C.__mro__])
C()
