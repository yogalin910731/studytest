#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 16:12
# @Author  : fangbo
class compxnode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random = None

def printnodelist(node):
    if node is None:
        return None
    returnlist =[]
    while node :
        returnlist.append(node.val)
        node = node.next
    return returnlist
def complexlinkedlist(node):
        #拷贝一遍
        pcur = node
        while pcur:
            newnode = compxnode(pcur.val)
            newnode.next = pcur.next
            pcur.next = newnode
            pcur = pcur.next.next
        #复制复杂节点
        pcur = node
        while pcur:
            if pcur.random != None:
                pcur.next.random = pcur.random
            pcur =pcur.next.next
        pcur = node
        pusecur = pcur
        ncur = node.next
        nusecur = ncur
        #拆开奇和偶
        while pusecur :
            pusecur.next = pusecur.next.next
            if nusecur.next != None:
                nusecur.next = nusecur.next.next
            pusecur = pusecur.next
            nusecur = nusecur.next
        print("拆封1：",printnodelist(pcur))
        print("拆封2：",printnodelist(ncur))
        return printnodelist(node)
if __name__ =='__main__':
    testnode1 = compxnode(1)
    testnode2 = compxnode(2)
    testnode3 = compxnode(3)
    testnode4 = compxnode(4)
    testnode1.next = testnode2
    testnode2.next = testnode3
    testnode3.next = testnode4
    testnode1.random = testnode3
    testnode4.random = testnode2
    print ("原复杂链表：")
    print (printnodelist(testnode1))
    complexlinkedlist(testnode1)
