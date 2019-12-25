#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : ws_client.py
@Author: sh
@Date  : 2019/5/24
@Desc  :
"""
import re


# a=[1,2,45,67,89,5,3,]
# a.sort(reverse=True)
# print(a)
# class A():
#     _a=None
#     def __new__(cls, *args, **kwargs):
#         if not cls._a:
#             cls._a=super().__new__(cls, *args, **kwargs)
#         return cls._a
# a.reverse()


class Node(object):
    def __init__(self, val, node=None):
        self.val = val
        self.next = node

    def __str__(self):
        return str(self.val)


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        if not self.__head:
            return True
        else:
            return False

    def first(self):
        return self.__head

    def length(self):
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def append(self, val):
        if self.__head == None:
            self.__head = Node(val)
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(val)

    def __str__(self):
        if self.__head == None:
            return []
        else:
            cur = self.__head
            result = [cur.val]
            while cur.next != None:
                cur = cur.next
                result = result + [cur.val]
            return str(result)


def aaa(head_a, head_b):
    a = [head_a.val]
    b = [head_b.val]
    cur_a = head_a.next
    cur_b = head_b.next
    while cur_a:
        a.append(cur_a.val)
        cur_a = cur_a.next
    while cur_b:
        b.append(cur_b.val)
        cur_b = cur_b.next
    for i in range(1, min(len(a), len(b)) + 1):
        if a[-1] != b[-1]:
            return False
        if a[-i] != b[-i]:
            return (b[-i + 1])


if __name__ == '__main__':
    a = [1, 2, 3, 7, 9, 1, 7]
    b = [4, 5, 7, 9, 1, 5]
    list = SingleLinkList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(7)
    list.append(9)
    list2 = SingleLinkList()
    list2.append(5)
    list2.append(4)
    list2.append(7)
    list2.append(9)
    head_a = list.first()
    head_b = list2.first()
    print(aaa(head_a, head_b))
