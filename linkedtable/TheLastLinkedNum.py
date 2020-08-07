#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 16:41
# @Author  : fangbo
# 求单链表中的倒数第k个结点
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def printvalue(Node):
    if Node is None:
        return None
    if Node.next is None:
        return Node.value
    listtest = []
    while Node :
        listtest.append(Node.value)
        Node = Node.next
    return listtest

def printLastvalue(Node,inputvalue):
    if inputvalue == 0:
        return "请输入范围内的数"
    curNode = Node
    if inputvalue != 0:
        for i in range(inputvalue):
            curNode = curNode.next
    while curNode:
        Node = Node.next
        curNode = curNode.next
    return Node.value

if __name__== '__main__':
    BeginNode = Node(1)
    vartest = BeginNode
    ValueDate = 2
    while ValueDate < 6 :
        testvalue = Node(ValueDate)
        vartest.next = testvalue
        ValueDate += 1
        vartest = testvalue
    print (printvalue(BeginNode))
    inputvalue = int(input("请输入倒数第几个数，现在目前总长度%d :"%len(printvalue(BeginNode))))
    print (printLastvalue(BeginNode,inputvalue))

