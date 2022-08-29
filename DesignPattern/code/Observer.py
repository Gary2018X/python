#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    :   2022/08/29 13:47:01
# @Author  :   Gary
# @Email   :   None
class Observer:
    # 抽象观察者
    def update(self):
        pass


class AlarmSensor(Observer):
    # 具体观察者
    def update(self, action):
        print("Alarm Got: %s" % action)
        self.runAlarm()

    def runAlarm(self):
        print("Alarm Ring...")


class WaterSprinker(Observer):
    # 具体观察者
    def update(self, action):
        print("Sprinker Got: %s" % action)
        self.runSprinker()

    def runSprinker(self):
        print("Spray Water...")


class EmergencyDialer(Observer):
    # 具体观察者
    def update(self, action):
        print("Dialer Got: %s" % action)
        self.runDialer()

    def runDialer(self):
        print("Dial 119...")


class Observed:
    # 抽象被观察者
    observers = []
    action = ""

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)


class smokeSensor(Observed):
    # 具体观察者
    def setAction(self, action):
        self.action = action

    def isFire(self):
        return True


if __name__ == "__main__":
    alarm = AlarmSensor()
    sprinker = WaterSprinker()
    dialer = EmergencyDialer()

    smoke_sensor = smokeSensor()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)

    if smoke_sensor.isFire():
        smoke_sensor.setAction("On Fire!")
        smoke_sensor.notifyAll()
