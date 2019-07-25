#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/7/25 10:41'
@email = 'qjyyn@qq.com'
'''


def parametrized_short_repr(max_width=8):
    '''缩短表示的参数化装饰器'''

    def parametrized(cls):
        '''内部包装函数，是实际的装饰器'''

        class ShortlyRepresented(cls):
            '''提供装饰器行为的子类'''

            def __repr__(self):
                return super().__repr__()[:max_width]

        return ShortlyRepresented

    return parametrized


@parametrized_short_repr(10)
class ClassWithLittleBitLongerLongName:
    pass


print(ClassWithLittleBitLongerLongName().__class__)
print(ClassWithLittleBitLongerLongName().__doc__)
