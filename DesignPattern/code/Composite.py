#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/22 09:34:32
# @Author  :   Gary
# @Email   :   None
from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):

    # 抽象组件
    @abstractmethod
    def draw(self):
        pass


class Point(Graphic):
    # 叶子组件
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点(%s,%s)' % (self.x, self.y)

    def draw(self):
        print(self)


class Line(Graphic):
    # 叶子组件
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '线段[(%s,%s)]' % (self.p1, self.p2)

    def draw(self):
        print(self)


class Picture(Graphic):
    # 复合组件
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        for g in self.children:
            g.draw()


# 简单图形
print('------简单图形------')
p = Point(1, 2)
l1 = Line(Point(1, 2), Point(3, 4))
l2 = Line(Point(5, 6), Point(7, 8))
print(p)
print(l1)
print(l2)
print('------复合图形(p,l1,l2)------')
# 复合图形
pic = Picture([p, l1, l2])
pic.draw()
