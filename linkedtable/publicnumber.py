#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 20:08
# @Author  : fangbo
#  两个链表的第一个公共结点
# 第一种就是把全部结点分别压入两个栈，利用栈的特性LIFO，然后同时pop出栈，一开始两边的元素肯定是相同的，当遇到不同的元素时，肯定已经遇到了最后一个节点，那就break
# 第二种就是分别从链表的头结点开始遍历，当两条链表有长度差时，先让长链表走他们的差值，当走到还剩下和短链表一样长时，两个链表同时遍历，这样就能找到第一个公共结点了

class node:
    def __init__(self,val):
        self.val = val
        self.next = None

#方法1
#stack 可以用列表模拟  append 进  pop 出
def findPublicvalueusestack(testnode1,testnode2):
    testlist1 = []
    testlist2 = []
    node1 = testnode1
    node2 = testnode2
    while node1 :
        testlist1.append(node1.val)
        node1 = node1.next
    while node2 :
        testlist2.append(node2.val)
        node2 = node2.next
    lastvalue = 0
    while len(testlist1) > 0 :
        pop1 = testlist1.pop()
        pop2 = testlist2.pop()
        if pop1 == pop2 :
            lastvalue = pop1
        else :
            return lastvalue
    return None

#方法2 求长度差值，长的减去差值，然后一起走
def findPublicvalue(testnode1,testnode2):
    node1 = testnode1
    node2 = testnode2
    count1 = 0
    count2 = 0
    while node1:
        count1 += 1
        node1 = node1.next
    while node2:
        count2 += 1
        node2 = node2.next
    if count1 ==0 or count2 ==0:
        return None
    if count1 >= count2 :
        betweencount = count1 - count2
        i = 0
        while i < betweencount:
            testnode1 = testnode1.next
            i += 1
    else:
        betweencount = count2 - count1
        i = 0

        while i < betweencount:
            testnode2 = testnode2.next
            i += 1
    #长度一样 ，一起往后找
    while testnode1:
        if testnode1.val == testnode2.val:
            return testnode1.val
        else:
            testnode1 = testnode1.next
            testnode2 = testnode2.next
    return None

def printnodelist(node):
    if node is None:
        return None
    while node:
        print (node.val,end="-")
        node = node.next


if __name__ == '__main__':
    testnode1 = node(1)
    testnode2 = node(2)
    testnode3 = node(3)
    testnode4 = node(4)
    testnode5 = node(5)
    testnode1.next = testnode2
    testnode2.next = testnode3
    testnode4.next = testnode5
    testnode5.next = testnode2
    #打印链表1
    print ("链表1:")
    printnodelist(testnode1)
    print("\n链表2:")
    #打印连表2
    printnodelist(testnode4)
    print ("\npublic node:")
    #print (findPublicvalue(testnode1,testnode4))
    print(findPublicvalueusestack(testnode1, testnode4))


