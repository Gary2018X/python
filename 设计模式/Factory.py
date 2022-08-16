#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/16 19:45:58
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
    # 抽象工厂类
    def create(self):
        pass


class DogFactory(animalFactory):
    # 具体工厂类
    def create(self):
        return dog()


class CatFactory(animalFactory):
    # 具体工厂类
    def create(self):
        return cat()


if __name__ == "__main__":
    DOG = DogFactory()
    dog = DOG.create(dog)
    print(dog.get_name(), dog.get_weight())  # dog 40.0
