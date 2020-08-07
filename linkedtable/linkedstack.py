#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 15:43
# @Author  : fangbo

class linkedNode:
    def __init__(self,value):
        self.val = value
        self.next = None

class linkedstack:
    def __init__(self):
        #用来记录栈顶的元素和栈
        self.val = None
        self.next = None

    def push(self,val):
        testnode = linkedNode(val)
        testnode.next = self.next
        self.next = testnode
        self.val = val

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

    def pop(self):
        headvalue = self.next
        if headvalue.next is None :
            self.val = None
            self.next = None
        self.val = headvalue.next.val
        self.next = headvalue.next

if __name__ == '__main__' :

    teststack = linkedstack()
    teststack.push(11)
    teststack.push(22)
    teststack.pop()
    teststack.push(33)
    print (teststack.getlinkedlength())
    print(teststack.stackheadvalue())
    teststack.pop()
    print(teststack.getlinkedlength())
    print(teststack.stackheadvalue())
