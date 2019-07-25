#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/7/25 10:32'
@email = 'qjyyn@qq.com'
'''
def short_repr(cls):
    cls.__repr__ = lambda self:super(cls,self).__repr__()[:8]
    return cls

@short_repr
class ClassWithRelativelyLongName:
    pass

print(ClassWithRelativelyLongName())
