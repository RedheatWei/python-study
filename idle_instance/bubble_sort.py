#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/17 17:13'
@email = 'qjyyn@qq.com'
'''
'''
冒泡排序
'''
import random


def bubble_sort(l):
    for _ in l:
        index = 0
        while index < len(l) - 1:
            if l[index] > l[index + 1]:
                l[index], l[index + 1] = l[index + 1], l[index]
            index += 1
    return l


l = [random.randint(1, 100) for i in range(100)]
ll = l.copy()
print(l)
print(bubble_sort(ll))
l.sort()
print(l)
