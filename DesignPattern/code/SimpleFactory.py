#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/16 19:41:50
# @Author  :   Gary
# @Email   :   None

class Animal():
    # 抽象产品类
    name = ""
    weight = 0.0
    type = "Animal"

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.price = weight

    def get_name(self):
        return self.name


class dog(Animal):
    # 具体产品类
    def __init__(self):
        self.name = "dog"
        self.weight = 40.0


class cat(Animal):
    # 具体产品类
    def __init__(self):
        self.name = "cat"
        self.weight = 5.0


class animalFactory():
    # 简单工厂类
    def create(self, animal):
        if animal == 'dog':
            animalIns = dog()
        elif animal == 'cat':
            animalIns = cat()
        return animalIns


if __name__ == "__main__":
    animal_factory = animalFactory()
    dog = animal_factory.create("dog")
    print(dog.get_name(), dog.get_weight())  # dog 40.0
