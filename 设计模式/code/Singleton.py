#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/15 21:45:35
# @Author  :   Gary
# @Email   :   None

import threading
import time


class Singleton(object):  # 抽象单例
    # 这里使用方法__new__来实现单例模式
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class Bus(Singleton):
    # 总线
    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data...", data)
        self.lock.release()


class VisitEntity(threading.Thread):
    # 线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        print('id bus', id(self.my_bus))
        self.my_bus.sendData(self.name)


if __name__ == "__main__":
    for i in range(3):
        print("Entity %d begin to run..." % i)
        my_entity = VisitEntity()
        print('id my_entity', id(my_entity))
        my_entity.setName("Entity_"+str(i))
        my_entity.start()
