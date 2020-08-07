#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 15:43
# @Author  : fangbo

class linkedNode:
    def __init__(self,value):
        self.val = value
        self.next = None

class linkedqueue:
    def __init__(self):
        #用来记录队列头和尾
        self.head = None
        self.tail = None

    def push(self,val):
        testnode = linkedNode(val)
        if self.head is None:
            self.head = testnode
            self.tail = testnode
        else:
            self.tail.next = testnode
            self.tail = testnode

    def isempty(self):
        return self.head is None

    def getlinkedlength(self):
        testnode = self.next
        if testnode is None :
            return 0
        count = 0
        while testnode:
            count += 1
            testnode = testnode.next
        return count

    def stackheadvalue(self):
        if self.next is not None:
            return self.val
        else:
            return None

    def delqueue(self):
        if self.isempty():
            return None
        result = self.head.val
        self.head =self.head.next
        return result

    def headvalue(self):
        if self.head is None:
            return None
        return self.head.val


if __name__ == '__main__' :
    print (111)
    testqueue = linkedqueue()
    testqueue.push(1)
    testqueue.push(2)
    testqueue.push(3)
    testqueue.push(4)
    print(testqueue.headvalue())
    testqueue.delqueue()
    testqueue.delqueue()
    print(testqueue.headvalue())

