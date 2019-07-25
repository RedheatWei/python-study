#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/6/11 16:36'
@email = 'qjyyn@qq.com'
'''
import math

start = 2
while True:
    if 8 * start ** 2 < 64 * start * math.log(start,2):
        print(start)
        start += 1
    else:
        break
