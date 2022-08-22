#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/18 19:48:38
# @Author  :   Gary
# @Email   :   None
# 类适配器模式使用示例：
from abc import ABCMeta, abstractmethod


class Payment(object, metaclass=ABCMeta):
    # 目标接口
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print('支付了%d' % money)


class BankPay():
    # 待适配的类
    def cost(self, money):
        print('银联支付了%d' % money)


class PaymentAdapter(Payment, BankPay):
    # 类适配器
    """
    把不兼容cost转换成pay
    """

    def pay(self, money):
        self.cost(money)


p = PaymentAdapter()
p.pay(100)
"""
银联支付了100
"""

# 类适配器模式使用示例：


class Payment(object, metaclass=ABCMeta):
    # 目标接口
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print('支付了%d' % money)


class BankPay():
    # 待适配的类
    def cost(self, money):
        print('银联支付了%d' % money)


class ApplePay():
    # 待适配的类
    def cost(self, money):
        print('苹果支付了%d' % money)


class PaymentAdapter(Payment):
    # 对象适配器
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = PaymentAdapter(ApplePay())
p.pay(100)
p = PaymentAdapter(BankPay())
p.pay(100)
"""
苹果支付了100
银联支付了100
"""
