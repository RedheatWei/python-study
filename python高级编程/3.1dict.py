#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/28 19:13'
@email = 'qjyyn@qq.com'
'''


class DistinctError(ValueError):
    pass


class distinctdict(dict):
    def __setitem__(self, key, value):
        if value in self.values():
            if (key in self and self[key] != value) or key not in self:
                raise DistinctError("This value already exists for different key")
        super().__setitem__(key, value)

my = distinctdict()
my["key"] = "value"

my["other_key"] = "value"