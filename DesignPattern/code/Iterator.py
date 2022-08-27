#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/27 14:32:45
# @Author  :   Gary
# @Email   :   None

class BinaryTree:
    # 可迭代对象
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        self.height = 0

    def insertLeft(self, newNode):
        tree = BinaryTree(newNode)
        if not self.leftChild:
            self.leftChild = tree
        else:
            # 如果插入位置已有节点，则整体向下挪
            # 新的子节点与旧的子节点链接，旧的父节点与新的子节点链接
            tree.leftChild = self.leftChild
            self.leftChild = tree
        self.height += 1

    def insertRight(self, newNode):
        tree = BinaryTree(newNode)
        if not self.rightChild:
            self.rightChild = tree
        else:
            tree.rightChild = self.rightChild
            self.rightChild = tree
        self.height += 1

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __iter__(self):
        return TreeIterator(tree=self)

    def __str__(self):
        return "<class 'BinaryTree' value: %r >" % self.getRootVal()


class TreeIterator:
    # 迭代器
    def __init__(self, tree) -> None:
        self.tree = tree
        self.treeLst = [self.tree]

    def __iter__(self):
        return self

    def __next__(self):
        # 采用层级遍历
        while len(self.treeLst) > 0:
            node = self.treeLst.pop(0)
            if node.leftChild:
                self.treeLst.append(node.getLeftChild())
            if node.rightChild:
                self.treeLst.append(node.getRightChild())
            return node
        raise StopIteration("Tree iter end")


if __name__ == '__main__':
    binaryTree = BinaryTree("a")
    binaryTree.insertLeft("b")
    binaryTree.insertRight("c")
    binaryTree.leftChild.insertLeft("d")
    binaryTree.leftChild.insertRight("e")
    binaryTree.rightChild.insertLeft("f")
    for node in binaryTree:
        print(node)
