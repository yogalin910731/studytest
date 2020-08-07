#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 11:21
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

def combine2link(Node1,Node2):
    testnode1 = Node1
    testnode2 = Node2
    if testnode1 is None :
        return printlinklist(testnode2)
    if testnode2 is None :
        return printlinklist(testnode1)

    if testnode1.val >= testnode2.val :
        returnnode = Node(testnode2.val)
        testnode2 = testnode2.next
    else :
        returnnode = Node(testnode1.val)
        testnode1 = testnode1.next

    usenode = returnnode

    while testnode1 and testnode2:
        if testnode1.val >= testnode2.val:
            betweennode = Node(testnode2.val)
            usenode.next = betweennode
            usenode = usenode.next
            testnode2 = testnode2.next

        else :
            returnnode.next = Node(testnode1.val)
            testnode1 = testnode1.next

    while testnode1:
        usenode.next = testnode1
        testnode1 = testnode1.next
        usenode = usenode.next
    while testnode2:
        usenode.next = testnode2
        testnode2 = testnode2.next
        usenode = usenode.next
    return (printlinklist(returnnode))

if __name__=='__main__':
    testnode1 = Node(1)
    testnode2 = Node(3)
    testnode3 = Node(4)
    testnode4 = Node(2)
    testnode5 = Node(3)
    testnode1.next = testnode2
    testnode2.next = testnode3
    testnode4.next = testnode5
    print ("链表1：")
    print(printlinklist(testnode1))
    print("链表2：")
    print(printlinklist(testnode4))
    print (combine2link(testnode1,testnode4))
