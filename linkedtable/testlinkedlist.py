#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 14:21
# @Author  : fangbo
class node:
    def __init__(self,value):
        self.val = value
        self.next = None

def printNodelist(headnode):
    if headnode is None:
        return None
    returnlist =[]
    while headnode :
        returnlist.append(headnode.val)
        headnode = headnode.next
    return returnlist

#在链表头部插入元素
def addNodeheadlist(headnode,value):
    headtest = headnode
    testnode = node(value)
    testnode.next = headtest
    return testnode

#在链表中任意位置插入元素0.1.2.3
def addNodebodylist(headnode,value,index):
    linkedlength = getnodelength(headnode)
    headtest = headnode
    testnode = node(value)
    if index == 0 :
        testnode.next = headtest
        return testnode
    elif index == linkedlength :
        while headnode.next:
            headnode = headnode.next
        headnode.next = testnode
        return  headtest
    elif index >linkedlength:
        return headtest
    else:
        for i in range(1,index):
            headnode = headnode.next
        testnodebegin = headnode
        testnodeend = headnode.next
        testnodebegin.next =testnode
        testnode.next =testnodeend
        return headtest

#删除链表节点
def delnode(headnode,index):
    headtest = headnode
    linkedlength = getnodelength(headnode)
    if index == 0 :
        return headtest.next
    elif index >linkedlength-1 :
        return headtest
    elif index == linkedlength-1 :
        for i in range(1,index):
            headnode =headnode.next
        headnode.next = None
        return headtest
    else:
        for i in range(1, index):
            headnode = headnode.next
        testbeginnode = headnode
        testendnode = headnode.next.next
        testbeginnode.next =testendnode
        return headtest

#得到链表长度
def getnodelength(headnode):
    if headnode is None:
        return 0
    count = 0
    while headnode :
        count += 1
        headnode = headnode.next
    return count


if __name__ =='__main__':
    testnode1 = node(1)
    testnode2 = node(2)
    testnode3 = node(3)
    testnode1.next = testnode2
    testnode2.next = testnode3
    print (printNodelist(testnode1))
    # testnode = addNodebodylist(testnode1,666,0)
    testnode = delnode(testnode1,1)
    print (printNodelist(testnode))


