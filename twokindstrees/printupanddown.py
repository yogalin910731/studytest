#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 10:38
# @Author  : fangbo
#三种难度
#打印 [1,2,3,4,5,6,7],
#打印 [[1], [2,3], [4,5,6,7]]
#打印 [[1], [3,2], [4,5,6,7]] 偶数层倒序
#
class Treenode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None


def printTree1(Nodetest):
    root = Nodetest
    queue = []
    testresult = []
    queue.append(root)
    while (len(queue) > 0):
        popnode = queue.pop(0)
        testresult.append(popnode.val)
        if popnode.lchild :
            queue.append(popnode.lchild)
        if popnode.rchild :
            queue.append(popnode.rchild)
    print (testresult)

def printTree2(Nodetest):
    if Nodetest is None :
        return None
    root = Nodetest
    queue = []
    testresult = []
    queue.append(root)
    while (len(queue) > 0):
        poplist = []
        poplistval =[]
        while (len(queue) > 0):
            popnode = queue.pop(0)
            poplist.append(popnode)
            poplistval.append(popnode.val)
        testresult.append(poplistval)
        for i in poplist:
            if i.lchild :
                queue.append(i.lchild)
            if i.rchild :
                queue.append(i.rchild)
    print (testresult)

def printTree3(Nodetest):
    if Nodetest is None :
        return None
    root = Nodetest
    queue = []
    testresult = []
    queue.append(root)
    count = 0
    while (len(queue) > 0):
        poplist = []
        poplistval =[]
        while (len(queue) > 0):
            popnode = queue.pop(0)
            poplist.append(popnode)
            poplistval.append(popnode.val)
        count += 1
        if count%2 == 1:
            testresult.append(poplistval)
        else:
            testresult.append(poplistval[::-1])
        for i in poplist:
            if i.lchild :
                queue.append(i.lchild)
            if i.rchild :
                queue.append(i.rchild)
    print (testresult)

if __name__=='__main__':
    testnode1 = Treenode(1)
    testnode2 = Treenode(2)
    testnode3 = Treenode(3)
    testnode4 = Treenode(4)
    testnode5 = Treenode(5)
    testnode6 = Treenode(6)
    testnode7 = Treenode(7)
    testnode1.lchild = testnode2
    testnode1.rchild = testnode3
    testnode2.lchild = testnode4
    testnode2.rchild = testnode5
    testnode3.lchild = testnode6
    testnode3.rchild = testnode7
    #第一种打印
    #printTree1(testnode1)
    #第一种打印
    #printTree2(testnode1)
    #第三种打印
    #printTree3(testnode1)
