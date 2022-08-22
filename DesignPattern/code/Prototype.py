#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/17 19:00:31
# @Author  :   Gary
# @Email   :   None

from collections import OrderedDict
import copy


class Book:
    # 具体书本类
    def __init__(self, name, authors, price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == "price":
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:
    # 抽象copy类
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(
                'Incorrect object identifier {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    # 新增b1
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Richie'),
              price=118, publisher='Prentice Hall', length=228,
              publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    # 复制
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, publication_date='1988-04-01', edition=2)
    for i in (b1, b2):
        print(i)
    print("ID b1 : {} , ID b2 : {}".format(id(b1), id(b2)))


if __name__ == '__main__':
    main()
