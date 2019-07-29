#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/7/25 17:49'
@email = 'qjyyn@qq.com'
'''


class InstanceCountingClass:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print("__new__ called with:", cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance

    def __init__(self, attribute):
        print("__init__() called with:", self, attribute)
        self.attribute = attribute


instance1 = InstanceCountingClass("abc")
print(instance1)
instance2 = InstanceCountingClass("xyz")
print(instance2)
print(instance1.number, instance1.instances_created)
print(instance2.number, instance2.instances_created)
