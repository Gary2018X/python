#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/24 16:05:50
# @Author  :   Gary
# @Email   :   None
class Coffee:
    # 具体类
    name = ''
    price = 0

    def __init__(self, name):
        self.name = name
        # 在实际业务中，咖啡价格应该是由配置表进行配置，或者调用接口获取等方式得到，此处为说明享元模式，将咖啡价格定为名称长度，只是一种简化
        self.price = len(name)

    def show(self):
        print("Coffee Name:%s Price:%s" % (self.name, self.price))


class Customer:
    # 顾客类
    coffee_factory = ""
    name = ""

    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffee_name):
        print("%s ordered a cup of coffee:%s" % (self.name, coffee_name))
        # return Coffee(coffee_name) # 传统做法直接调用Coffee类
        return self.coffee_factory.getCoffee(coffee_name)


class CoffeeFactory():
    # 亨元工厂类
    coffee_dict = {}

    def getCoffee(self, name):
        if self.coffee_dict.get(name) is None:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def getCoffeeCount(self):
        return len(self.coffee_dict)


if __name__ == "__main__":
    coffee_factory = CoffeeFactory()
    customer_1 = Customer("A Client", coffee_factory)
    customer_2 = Customer("B Client", coffee_factory)
    customer_3 = Customer("C Client", coffee_factory)
    customer_4 = Customer("C Client", coffee_factory)
    c1_capp = customer_1.order("cappuccino")
    c1_capp.show()
    c2_mocha = customer_2.order("mocha")
    c2_mocha.show()
    c3_capp = customer_3.order("cappuccino")
    c3_capp.show()
    c4_capp = customer_4.order("cappuccino")
    c4_capp.show()
    print("Num of Coffee Instance:%s" % coffee_factory.getCoffeeCount())
