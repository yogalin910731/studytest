#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 9:29
# @Author  : fangbo

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def printnodelist(node):
    if node is None:
        print (None)
    while node :
        print (node.val,end="-")
        node = node.next

def outputvalue(node):
    if node is None:
        return None
    testlist = []
    while node :
        testlist.append(node.val)
        node = node.next
    return testlist[::-1]

if __name__=='__main__':
    testnode1 = Node(1)
    testnode2 = Node(2)
    testnode3 = Node(3)
    testnode1.next = testnode2
    testnode2.next = testnode3
    print ("处理前：")
    printnodelist(testnode1)
    print("处理后：")
    print(outputvalue(testnode1))
     #list1.reverse()
    #list1[::-1] #切片的格式 [0:3:1]，其中下标0 指的是序列的第一个元素(左边界)，下标3可以指是切片的数量(右边界)，参数1表示切片的步长为1，如果是-1则表示从右边开始进行切片且步长为1。切片不包括右边界下标。

