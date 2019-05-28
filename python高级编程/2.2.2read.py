#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/24 15:11'
@email = 'qjyyn@qq.com'
'''
import tokenize

reader = open("/Users/Redheat/Desktop/TBCDB_1.7.0_ANewHope.sql").readline
tokens = tokenize.generate_tokens(reader)

for i in range(10):
    print(tokens.__next__())