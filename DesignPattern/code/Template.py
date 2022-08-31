#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/31 10:02:27
# @Author  :   Gary
# @Email   :   None
from abc import ABCMeta, abstractmethod
from time import sleep

# 抽象类


class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):  # 原子操作/钩子操作
        pass

    @abstractmethod
    def repaint(self):  # 原子操作/钩子操作
        pass

    @abstractmethod
    def stop(self):  # 原子操作/钩子操作
        pass

    def run(self):
        """
        模板方法(具体方法)，这个大逻辑就不需要自己写了
        :return:
        """
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()

# 具体类


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print('窗口开始运行！')

    def stop(self):
        print('窗口停止运行！')

    def repaint(self):
        print(self.msg)


MyWindow("Hello...").run()
