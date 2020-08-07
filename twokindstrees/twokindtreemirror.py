#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 10:03
# @Author  : fangbo

class Treenode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None


def printTree(Nodetest):
    root = Nodetest
    queue = []
    queue.append(root)
    while (len(queue) > 0):
        popnode = queue.pop(0)
        print (popnode.val,end=",")
        if popnode.lchild :
            queue.append(popnode.lchild)
        if popnode.rchild :
            queue.append(popnode.rchild)

def mirrortree(nodetest):
    if nodetest is None :
        return None
    testnode = nodetest
    testnode.lchild,testnode.rchild = testnode.rchild,testnode.lchild
    mirrortree(testnode.lchild)
    mirrortree(testnode.rchild)

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
    printTree(testnode1)
    mirrortree(testnode1)
    print ("\n")
    printTree(testnode1)