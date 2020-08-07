#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 17:17
# @Author  : fangbo
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def printlinklist(node):
    if node is None:
        return None
    returnlist = []
    while node :
        returnlist.append(node.val)
        node = node.next
    return returnlist

def delallsinglevalue(headnode,val):
#找到第一个不为val的元素，然后再处理中间的
    while(headnode != None and headnode.val == val):
        headnode = headnode.next
    if headnode is None:
        return None
    returnheadnode = headnode
    while (headnode.next != None):
        if headnode.next.val == val:
            testnode = headnode.next.next
            headnode.next = testnode
        else:
            headnode = headnode.next
    return returnheadnode


def delallsinglevaluedummy(headnode,val):
    dummynode = Node(-1)
    dummynode.next = headnode
    testnode = dummynode
    while (testnode.next != None):
        if testnode.next.val == val:
            testnode.next = testnode.next.next
        else:
            testnode = testnode.next
    return dummynode.next

if __name__ == '__main__':
    testnode1 = Node(2)
    testnode2 = Node(2)
    testnode3 = Node(5)
    testnode4 = Node(2)
    testnode5 = Node(1)
    testnode1.next = testnode2
    testnode2.next = testnode3
    testnode3.next = testnode4
    testnode4.next = testnode5
    # print (printlinklist(testnode1))
    #testnode = delallsinglevalue(testnode1,2)
    testnode = delallsinglevalue(testnode1,2)
    print(printlinklist(testnode))
    #

