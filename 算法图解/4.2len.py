#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/22 15:49'
@email = 'qjyyn@qq.com'
'''
'''
计算列表元素数
'''
def len_func(l):
    if l ==[]:
        return 0
    return 1 + len_func(l[1:])


print(len_func([1,2,3,4,5,6]))