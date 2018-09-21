#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 18:35
# @Author  : Bilon
# @File    : 私有变量和私有方法.py

'''私有变量'''

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def growup(self, i=1):
        if i > 0 and i < 90:   # 控制逻辑
            self.age += i

# p1 = Person('tom')
# p1.growup(20)       # 正常的范围
# p1.age = 160        # 超过了范围，并绕过了控制逻辑
# print(p1.age)
# 上例本来是想通过方法控制属性，但是由于属性在外部可以访问（或者说可见），就可以直接绕过方法直接修改这个属性

# Python提供了私有属性可以解决这个问题
class Person1:
    def __init__(self, name, age=18):
        self._name = name       # 保护变量
        self.__age = age        # 私有变量

    def growup(self, i=1):
        if 0 < i < 90:
            self.__age += i

    def getage(self):
        return self.__age

# tom = Person1('tom')
# tom.growup(2)
# #print(tom.__age)        # Erro 找不到
# print(tom.getage())
#
# print(tom.__dict__)      # 找到 _Person1__age
# tom._Person1__age = 200
# print(tom.getage())
# print(tom._name)
'''
私有变量的本质：
类定义的时候，如果声明一个实例变量使用双下划线开头，Python解释器会将其改名
转换名称为 _类名__变量名 ，所以用原来的名字访问不到了
用 实例.__dict__ 可以知道私有变量的新名称，就可以直接从外面访问并修改它

保护变量：
以一个下划线开头的变量 _name 叫保护变量
这个 _name 变量根本就没有改变名称，和普通的变量一样，解释器不做任何特殊处理
这只是开发者共同的约定，看见这种变量，就如同私有变量，不要直接使用
'''

# 私有方法
class Person2:
    def __init__(self, name, age=18):
        self._name = name       # 保护变量
        self.__age = age        # 私有变量

    def _getname(self):
        return self._name

    def __getage(self):
        return self.__age

tom = Person2('tom')
print(tom._getname())
# print(tom.__getage())         # Erro 无此属性
print(Person2.__dict__)         # 找到 _Person2__growup
print(tom._Person2__getage())   # 其实是被改名了
print(tom.__dict__)
'''
私有方法的本质
单下划线的方法只是开发者之间的约定，解释器不做任何改变
双下划綫的方法是私有方法，解释器会改名，改名的策略和私有变量相同： _类名__方法名
方法变量都可以在类的__dict__中找到
'''

'''
私有成员的总结
在Python中使用 _ 单下划线或 __双下划綫来标识一个成员被保护或者被私有化隐藏起来
但是，不管使用什么样的访问控制，都不能真正的阻止用户修改类的成员，Python中没有绝对安全的保护成员或者私有成员
因此，下划线只是一种警告或者提醒，请遵守这个约定
除非真有必要，否则不要修改或者使用保护成员或者私有成员，更不要修改它们
'''