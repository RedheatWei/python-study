#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/28 19:28'
@email = 'qjyyn@qq.com'
'''


class Folder(list):
    def __init__(self, name):
        self.name = name

    def dir(self, nesting=0):
        offset = " " * nesting
        print('%s%s/' % (offset, self.name))

        for element in self:
            if hasattr(element, 'dir'):
                element.dir(nesting + 1)
            else:
                print("%s %s" % (offset, element))

tree = Folder("project")
tree.append("README.md")
tree.dir()

src = Folder("src")
src.append("script.py")
tree.append(src)
tree.dir()