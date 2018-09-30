#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 16:02
# @Author  : Bilon
# @File    : 定制构造函数.py

"""
OOP(面向对象程序设计)的重要概念：
实例创建————填充实例属性 (__init__)
行为方法————在类方法中封装逻辑   (giveRaise())
运算符重载————为打印这样的内置操作提供行为 (__str__)
定制行为————重新定义子类中的方法以使其特殊化
"""


class Person:
    # 初始化 姓名、岗位、薪资
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    # 加薪
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # 扩展类以给出一个定制的 print ，当类的实例作为一个整体显示的时候会列出属性
    def __str__(self):
        return '[Person: {}, {}]'.format(self.name, self.pay)


# 编写一个Person的子类
class Manager(Person):
    """
    假设当一个Manager要涨工资的时候，他像往常一样接受一个传入的百分比
    但会获得一个默认为 10% 的额外奖金
    """
    # 扩展 giveRaise方法
    def give_raise(self, percent, bonus=.10):
        # self.pay = int(self.pay * (1 + percent + bonus))    # 虽然便于理解，但此方式不好
        Person.give_raise(self, percent + bonus)               # 好的方式，便于维护

    '''
    当我们创建Manager对象的时候，必须为它提供一个 'mgr' 工作名称似乎是没有意义的
    我们想要重新定义 Manager 中的 __init__ 方法，提供 'mgr' 字符串
    '''
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)
    print(bob)
    print(sue)
    # print(bob.lastName(), sue.lastName())
    sue.give_raise(.10)
    print(sue)

    # 重新定义 Manager 中的 __init__ 后，这里就不用传 'mgr' 了
    # tom = Manager('Tom Jones', 'mgr', 20000)
    tom = Manager('Tom Jones', 20000)
    tom.give_raise(.10)
    # print(tom.lastName())
    print(tom)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


# development = Department(bob, sue)
# development.add_member(tom)
# development.give_raises(.10)
# development.show_all()
