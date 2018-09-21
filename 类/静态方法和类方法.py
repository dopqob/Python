#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 9:53
# @Author  : Bilon
# @File    : 静态方法和类方法.py

'''静态方法和类方法'''

'''装饰一个类'''
# 增加类变量
def setnameproperty(cls, name):
    cls.NAME = name     # 动态增加类属性

# 改进成装饰器
def setnameproperty(name):
    def wrapper(cls):           # 英文释义 wrapper：包装材料
        cls.NAME = name
        return cls
    return wrapper

@setnameproperty('MY CLASS')
class MyClass1:
    pass

# 之所以能够装饰，本质上是为类对象动态的添加了一个属性
print(MyClass1.NAME)
print(MyClass1.__dict__)


'''类方法和静态方法'''

class MyClass:
    xxx = 'XXX'

    def foo(self):      # 普通方法（跟实例相关）
        print('foo')

    @classmethod        # 类方法装饰器
    def clsmtd(cls):
        # print('{}.xxx={}'.format(cls.__name__, cls.xxx))
        print('{0.__name__}.xxx={0.xxx}'.format(cls))   # 两种写法都可以

    @staticmethod       # 静态方法装饰器
    def staticmtd():
        print('static')

a = MyClass()
a.foo()
# MyClass.foo()     # Erro
MyClass.foo(a)

MyClass.clsmtd()
a.clsmtd()

MyClass.staticmtd()
a.staticmtd()

'''
总结：
类除了普通方法都可以调用，如果调用普通方法需要类的实例作为第一参数 例：MyClass.foo(a)
实例可以调用所有类中定义的方法（包括类方法、静态方法），普通方法传入实例自身，静态方法和类方法会先找到类，再通过类找到静态方法和类方法
'''