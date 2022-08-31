#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/31 10:16:59
# @Author  :   Gary
# @Email   :   None
class Medicine:
    # 抽象对象
    name = ""
    price = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def accept(self, visitor):
        pass


class Antibiotic(Medicine):
    # 具体对象
    def accept(self, visitor):
        visitor.visit(self)


class Coldrex(Medicine):
    # 具体对象
    def accept(self, visitor):
        visitor.visit(self)


class Visitor:
    # 抽象访问者
    name = ""

    def setName(self, name):
        self.name = name

    def visit(self, medicine):
        pass


class Charger(Visitor):
    # 具体访问者
    def visit(self, medicine):
        print("CHARGE: %s lists the Medicine %s. Price:%s " %
              (self.name, medicine.getName(), medicine.getPrice()))


class Pharmacy(Visitor):
    # 具体访问者
    def visit(self, medicine):
        print("PHARMACY:%s offers the Medicine %s. Price:%s" %
              (self.name, medicine.getName(), medicine.getPrice()))


class ObjectStructure:
    # 抽象对象结构
    pass


class Prescription(ObjectStructure):
    # 具体对象结构
    medicines = []

    def addMedicine(self, medicine):
        self.medicines.append(medicine)

    def rmvMedicine(self, medicine):
        self.medicines.append(medicine)

    def visit(self, visitor):
        for medc in self.medicines:
            medc.accept(visitor)


if __name__ == "__main__":
    yinqiao_pill = Coldrex("Yinqiao Pill", 2.0)
    penicillin = Antibiotic("Penicillin", 3.0)
    doctor_prsrp = Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)
    charger = Charger()
    charger.setName("Doctor Strange")
    pharmacy = Pharmacy()
    pharmacy.setName("Doctor Wei")
    doctor_prsrp.visit(charger)
    doctor_prsrp.visit(pharmacy)
