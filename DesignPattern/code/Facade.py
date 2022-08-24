#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/24 15:41:27
# @Author  :   Gary
# @Email   :   None

class CPU:
    # 子系统类
    def run(self):
        print('CPU start to run...')

    def stop(self):
        print('CPU stop to run...')


class Disk:
    # 子系统类
    def run(self):
        print('Disk start to run...')

    def stop(self):
        print('Disk stop to run...')


class Memory:
    # 子系统类
    def run(self):
        print('Memory start to run...')

    def stop(self):
        print('Memory stop to run...')


class Computer():
    # 外观
    def __init__(self):
        self.CPU = CPU()
        self.Disc = Disk()
        self.Member = Memory()

    def run(self):
        self.CPU.run()
        self.Disc.run()
        self.Member.run()

    def stop(self):
        self.CPU.stop()
        self.Disc.stop()
        self.Member.stop()


# 客户端，高层代码
c = Computer()
c.run()
c.stop()
