#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 15:54
# @Author  : shenhao
# @File    : node.py

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
                print(result)
            return str(result)


def reverse(head):  # 单链表逆序
    if head == None:
        return None
    cur = head.next
    newhead = head
    newhead.next = None
    tem = newhead
    while cur:
        newhead = cur
        cur = cur.next
        newhead.next = tem
        tem = newhead
    return newhead
    # def ReverseList(self):
    #     # write code here
    #     if self.__head == None:
    #         return self.__head
    #     cur=self.__head.next
    #     newhead=self.__head
    #     newhead.next=None
    #     a=newhead
    #     while cur :
    #         newhead=cur
    #         cur=cur.next
    #         newhead.next=a
    #         a=newhead
    #     return newhead


class treeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def font(root):
    if root == None:
        return None
    print(root.val)
    font(root.left)
    font(root.right)


def mid(root):
    if root == None:
        return None
    mid(root.left)
    print(root.val)
    mid(root.right)


def end(root):
    if root == None:
        return None
    end(root.left)
    end(root.right)
    print(root.val)


def a(root):
    if root == None:
        return None
    queue = []
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)


def b(root):
    if root == None:
        return None
    queue = []
    queue.append(root)
    while queue:
        cur = queue.pop()
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)


if __name__ == '__main__':
    # list = SingleLinkList()
    # list.append(1)
    # list.append(2)
    # list.append(3)
    # list.append(4)
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = c
    list = SingleLinkList(a)
    head = list.first()
    res = {}
    res[head.val] = head.val
    cur = head.next
    flag = False
    while cur:
        if cur.val in res:
            print('有环')
            flag = True
            break
        res[cur.val] = cur.val
        cur = cur.next
        # print('1')
    if flag:
        pass
    else:
        print(1)
