#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 17:52
# @Author  : Bilon
# @File    : employees.py

""" OOP和继承的关系： “是一个(is-a)” """


class Employee:
    """员工的统称 超类"""
    def __init__(self, name, pay=0):
        self.name = name
        self.pay = pay

    def give_raise(self, percent):
        # self.pay = self.pay + (self.pay * percent)
        self.pay = int(self.pay * (1 + percent))

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return '[Employee: name = {}, pay = {}]'.format(self.name, self.pay)


class Chef(Employee):
    """厨师 薪水8000 工作是烹饪美食"""
    def __init__(self, name):
        Employee.__init__(self, name, 8000)

    def work(self):
        print(self.name, 'makes food')


class Server(Employee):
    """服务员 薪水5000 工作是服务客户"""
    def __init__(self, name):
        Employee.__init__(self, name, 5000)

    def work(self):
        print(self.name, 'interfaces with customer')


class PizzaRobot(Chef):
    """披萨机器人 继承厨师 专门做披萨"""
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, 'makes pizza')


if __name__ == '__main__':
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.give_raise(.20)
    print(bob)
    print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
