#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 17:43
# @Author  : fangbo

# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild =None

def beforeOrder(treenode):
    if treenode:
        print(treenode.data,end=",")
        beforeOrder(treenode.lchild)
        beforeOrder(treenode.rchild)

def middleOrder(treenode):
    if treenode:
        beforeOrder(treenode.lchild)
        print(treenode.data, end=",")
        beforeOrder(treenode.rchild)

def afterOrder(treenode):
    if treenode:
        beforeOrder(treenode.lchild)
        beforeOrder(treenode.rchild)
        print(treenode.data, end=",")


def guanduOrder(treenode):
    queen = deque()
    queen.append(treenode)
    while len(queen)>0 :
        betweenqueue = queen.popleft()
        print (betweenqueue.data,end=",")
        if betweenqueue.lchild:
            queen.append(betweenqueue.lchild)
        if betweenqueue.rchild:
            queen.append(betweenqueue.rchild)
if __name__ == '__main__':
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    g = TreeNode("G")
    # e的左边是a，右边是G
    # a的右孩子是c
    # c的左孩子是b，c的右孩子是d
    # g的右的孩子是f
    e.lchild = a
    e.rchild = g
    a.rchild = c
    c.lchild = b
    c.rchild = d
    g.rchild = f
    root = e
    beforeOrder(root)
    print("\n")
    middleOrder(root)
    print("\n")
    afterOrder(root)
    print("\n")
    guanduOrder(root)