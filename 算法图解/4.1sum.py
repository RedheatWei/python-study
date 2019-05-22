#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/22 15:38'
@email = 'qjyyn@qq.com'
'''
'''
实现sum函数
'''
def sum_func(l):
    if l == []:
        return 0
    return l[0]+sum_func(l[1:])


print(sum_func([1,2,3,4,5]))