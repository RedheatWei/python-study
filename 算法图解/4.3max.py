#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/22 15:57'
@email = 'qjyyn@qq.com'
'''
'''
找出列表最大数
'''
def max_func(l):
    if len(l) == 2:
        return l[0] if l[0] > l[1] else l[1]
    part_max = max_func(l[1:])
    return part_max if part_max > l[0] else l[0]

print(max_func([1,2,5,3,4]))