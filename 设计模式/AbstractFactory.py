#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/16 19:45:45
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


class Animal1():
    # 抽象产品类1
    name = ""
    weight = 0.0
    type = "Animal1"

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.price = weight

    def get_name(self):
        return self.name


class dog1(Animal1):
    # 具体产品类
    def __init__(self):
        self.name = "dog1"
        self.weight = 410.0


class cat1(Animal1):
    # 具体产品类
    def __init__(self):
        self.name = "cat1"
        self.weight = 51.0


class animalFactory():
    # 抽象工厂类
    def create_dog(self):
        pass

    def create_cat(self):
        pass


class Factory(animalFactory):
    # 具体工厂类
    def create_dog(self):
        animalIns = dog()
        return animalIns

    def create_cat(self):
        animalIns = cat()
        return animalIns


class Factory1(animalFactory):

    # 具体工厂类
    def create_dog(self):
        animalIns = dog1()
        return animalIns

    def create_cat(self):
        animalIns = cat1()
        return animalIns


if __name__ == "__main__":
    DOG = Factory1()
    dog = DOG.create_cat()
    print(dog.get_name(), dog.get_weight())  # dog 40.0
