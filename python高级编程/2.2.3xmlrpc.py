#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/27 17:01'
@email = 'qjyyn@qq.com'
'''
rpc_info = {}


def xmlrpm(in_=(), out=(type(None),)):
    def _xmlrpc(function):
        func_name = function.__name__
        rpc_info[func_name] = (in_, out)

        def _check_types(elements, types):
            if len(elements) != len(types):
                raise TypeError("argument count is wrong")
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError('arg #%d should %s' % (index, of_the_right_type))

        def __xmlrpc(*args):
            checkable_args = args[1:]
            _check_types(checkable_args, in_)
            res = function(*args)
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out)
            return res

        return __xmlrpc

    return _xmlrpc


class RPCView:
    @xmlrpm((int, int))
    def meth1(self, int1, int2):
        print("received %d and %d" % (int1, int2))

    @xmlrpm((str,), (int,))
    def meth2(self, phrase):
        print("received %s" % phrase)
        return 12

my = RPCView()
my.meth2(2)