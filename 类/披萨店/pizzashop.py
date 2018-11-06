#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 9:50
# @Author  : Bilon
# @File    : pizzashop.py

""" OOP和组合的关系： “有一个(has-a)” """

from employees import PizzaRobot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print('{} orders from {}'.format(self.name, server))

    def pay(self, server):
        print('{} pays for item to {}'.format(self.name, server))


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')
