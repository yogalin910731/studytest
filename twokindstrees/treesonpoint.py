#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 10:35
# @Author  : fangbo

class treenode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None

def iseuqual(root1,root2):
    # 如果B树为空，那么可以算B是A的子结构
    # 如果A树空，而B树不空，那么B不是A的子结构
    # 根节点值相同，再判断左右子树是否都相同
    if not root2:
        return True
    if not root1:
        return False
    if root1.val != root2.val:
        return False
    return iseuqual(root1.lchild, root2.lchild) and iseuqual(root1.rchild, root2.rchild)

def guangduprint(treenodetest) :
    Nodetest = treenodetest
    testlist = []
    testlist.append(Nodetest)
    while len(testlist) > 0 :
        popnode = testlist.pop(0)
        print (popnode.val,end=",")
        if popnode.lchild:
            testlist.append(popnode.lchild)
        if popnode.rchild:
            testlist.append(popnode.rchild)
    return treenodetest

def judgesonpoint(allnode,sonnode):
    totalnode = allnode
    judgenode = sonnode
    #找到相同的根节点
    keeplist = []
    judgelist = []
    judgelist.append(totalnode)
    while len(judgelist) > 0:
        testpop = judgelist.pop(0)
        if testpop.val == judgenode.val:
            keeplist.append(testpop)
        if testpop.lchild:
            judgelist.append(testpop.lchild)
        if testpop.rchild:
            judgelist.append(testpop.rchild)
    for i in keeplist:
        if iseuqual(i, judgenode):
            return True
    return False


if __name__ == '__main__':
    a = treenode("A")
    b = treenode("B")
    c = treenode("C")
    d = treenode("D")
    e = treenode("E")
    f = treenode("F")
    g = treenode("G")
    e.lchild = a
    e.rchild = g
    a.rchild = c
    c.lchild = b
    c.rchild = d
    g.rchild = f
    h = treenode("C")
    i = treenode("D")
    h.rchild = i
    root = e
    print(judgesonpoint(e,h))