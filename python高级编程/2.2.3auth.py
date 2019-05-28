#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/28 11:08'
@email = 'qjyyn@qq.com'
'''


class User(object):
    def __init__(self, roles):
        self.roles = roles


class Unauthorized(Exception):
    pass


def protect(role):
    def _protect(function):
        def __protect(*args, **kw):
            user = globals().get("user")
            print(globals())
            if user is None or role not in user.roles:
                raise Unauthorized("I won't tell you")
            return function(*args, **kw)

        return __protect

    return _protect


tarek = User(('admin', 'user'))
bill = User(('user',))


class MySecrets(object):
    @protect('admin')
    def waffle_recipe(self):
        print("use tons of butter!")


there_are = MySecrets()

user = tarek
there_are.waffle_recipe()

user = bill
there_are.waffle_recipe()
