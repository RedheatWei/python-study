#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/24 11:46'
@email = 'qjyyn@qq.com'
'''


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()

for i in range(10):
    print(fib.__next__())