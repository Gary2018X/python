#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/26 15:26:00
# @Author  :   Gary
# @Email   :   None
from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    # 抽象的处理者
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):
    # 具体的处理者
    def handle_leave(self, day):
        if day <= 30:
            print('总经理准假%d' % day)
        else:
            print('可以辞职了！')


class DepartmentManager(Handler):
    # 具体的处理者
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 7:
            print('部门经理准假%d' % day)
        else:
            print('部门经理职权不足')
            self.next.handle_leave(day)


class ProjectDirector(Handler):
    # 具体的处理者
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print('项目主管准假%d' % day)
        else:
            print('项目主管职权不足')
            self.next.handle_leave(day)


day = 20
p = ProjectDirector()
p.handle_leave(day)
"""
项目主管职权不足
部门经理职权不足
总经理准假20
"""
