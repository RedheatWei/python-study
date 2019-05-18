#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/17 20:35'
@email = 'qjyyn@qq.com'
'''
'''
链表
'''

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head.next = node
            self.length += 1
        else:
            current_node = self.head.next
            while current_node.next != Node:
                current_node = current_node.next
            current_node.next = None
            self.length += 1


l = LinkedList()

l.append(1)
print(len(l))
