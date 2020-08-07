#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 15:08
# @Author  : fangbo
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def delete01linkedlist(node,todelete):
    nodeindex = node
    nodeindex2 = node
    for i  in range (todelete-2):
        nodeindex = nodeindex.next
    for i  in range (todelete):
        nodeindex2 = nodeindex2.next
    nodeindex.next = nodeindex2
    return printTotallist(node)


def printTotallist(node):
    if node is None :
        return None
    returnlist =[]
    while node :
        returnlist.append(node.val)
        node = node.next
    return returnlist

if __name__=='__main__':
    BeginNode = Node(1)
    vartest = BeginNode
    ValueDate = 2
    while ValueDate < 4:
        testvalue = Node(ValueDate)
        vartest.next = testvalue
        ValueDate += 1
        vartest = testvalue
    print (printTotallist(BeginNode))
    inputword = input("输入要删的第几个元素：")

    print (delete01linkedlist(BeginNode,int(inputword)))
