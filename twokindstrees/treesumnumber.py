#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 14:18
# @Author  : fangbo
class Treenode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None


def treesummun(testnode,sum):

        return list



def FindPath(root, expectNumber):
    if not root:
        return []
    result = []

    def FindPath2(root, path, currentNum):
        currentNum += root.val
        path.append(root)
        # 判断是不是到叶子节点了，到叶子节点了就要判断值的和是不是相等
        flag = root.lchild == None and root.rchild == None
        # 返回值是一个等于整数的序列
        if currentNum == expectNumber and flag:
            onepath = []
            for node in path:
                onepath.append(node.val)
            result.append(onepath)

        if currentNum < expectNumber:
            if root.lchild:
                FindPath2(root.lchild, path, currentNum)
            if root.rchild:
                FindPath2(root.rchild, path, currentNum)
        # 拿到一个正确的路径后要弹出，回到上一次父节点继续递归
        path.pop()

    FindPath2(root, [], 0)
    return result

if __name__ == '__main__':
    testnode1 = Treenode(10)
    testnode2 = Treenode(5)
    testnode3 = Treenode(12)
    testnode4 = Treenode(4)
    testnode5 = Treenode(7)
    testnode1.lchild = testnode2
    testnode1.rchild = testnode3
    testnode2.lchild = testnode4
    testnode2.rchild = testnode5

    print (FindPath(testnode1,22))