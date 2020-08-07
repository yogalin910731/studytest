#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 10:34
# @Author  : fangbo
class treeNode:
    def __init__(self,nodeval):
        self.val = nodeval
        self.leftnode = None
        self.rightnode = None

def rebuildworkstree(testlist1,testlist2):
    while len(testlist1)>0 :
        newtreeNode = treeNode(testlist1[0])
        pcur = list2.index(testlist1[0])
        newtreeNode.leftnode = rebuildworkstree(testlist1[1:1+pcur],testlist2[0:pcur])
        newtreeNode.rightnode = rebuildworkstree(testlist1[1+pcur:],testlist2[pcur+1:])
        return newtreeNode

def guangdudayin(treetestnode):
    listqueue = []
    listqueue.append(treetestnode)
    while len(listqueue) >0 :
        testvalue = listqueue.pop(0)
        print (testvalue.val,end = ",")
        if testvalue.leftnode:
            listqueue.append(testvalue.leftnode)
        if testvalue.rightnode:
            listqueue.append(testvalue.rightnode)

if __name__ == '__main__':
    list1 = ["a","b","d","c","e"]
    list2 = ["d","b","a","c","e"]

    testkey=rebuildworkstree(list1,list2)
    print (testkey.val)
    guangdudayin(testkey)
    #广度搜索打印 使用队列  先进先出 可以用queue的leftpop  也可以用list pop(0)模拟