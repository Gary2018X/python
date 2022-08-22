#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/18 20:18:20
# @Author  :   Gary
# @Email   :   None
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    # 抽象
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    # 实现
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    # 细化抽象
    name = '长方形'

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    # 如果要扩展形状，只需要添加形状类
    name = '圆形'

    def draw(self):
        self.color.paint(self)


class Red(Color):
    # 细化实现
    def paint(self, shape):
        print('画红色的%s' % shape.name)


class Green(Color):
    # 如果要扩展颜色，只需要添加颜色类
    def paint(self, shape):
        print('画绿色的%s' % shape.name)


class Blue(Color):
    # 如果要扩展颜色，只需要添加颜色类
    def paint(self, shape):
        print('画蓝色的%s' % shape.name)


rectangle = Rectangle(Red())
rectangle.draw()
circle = Circle(Blue())
circle.draw()
"""
画红色的长方形
画蓝色的圆形
"""
