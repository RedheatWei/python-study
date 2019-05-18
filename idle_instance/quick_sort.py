#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/17 17:34'
@email = 'qjyyn@qq.com'
'''
'''
快速排序
'''
import random

def quick(l):
    if len(l) < 2:
        return l
    left = []
    right = []
    mid = l[0]
    for i in l[1:]:
        if i < mid:
            left.append(i)
        else:
            right.append(i)
    return quick(left) + [mid] + quick(right)

l = [random.randint(1, 100) for i in range(100)]
ll = l.copy()
print(l)
print(quick(ll))
l.sort()
print(l)