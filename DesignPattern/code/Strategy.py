#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/31 09:35:00
# @Author  :   Gary
# @Email   :   None
from abc import abstractmethod, ABCMeta
from datetime import datetime

# 抽象策略


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass

# 具体策略


class FastStrategy(Strategy):
    def execute(self, data):
        print("使用较快的策略处理%s" % data)

# 具体策略


class SlowStrategy(Strategy):
    def execute(self, data):
        print("使用较慢的策略处理%s" % data)

# 上下文


class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy
        # 可以定义用户不知道的东西
        self.date = datetime.now()

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


data = "Hello!"
# 使用较快的策略处理
fast_strategy = FastStrategy()
context = Context(fast_strategy, data)
context.do_strategy()
# 使用较慢的策略处理
slow_strategy = SlowStrategy()
context = Context(slow_strategy, data)
context.do_strategy()
"""
使用较快的策略处理Hello!
使用较慢的策略处理Hello!
"""
