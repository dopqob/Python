#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 10:45
# @Author  : Bilon
# @File    : 运算符重载.py

"""
运算符重载只是意味着在类方法中拦截内置的操作，当类中提供了某个特殊名称的方法，在该类的实例出现
在它们相关的表达式时，Python自动调用它们
●   运算符重载让类拦截常规的Python运算
●   类可重载所有Python表达式运算符
●   类也可重载打印、函数调用、属性点号运算等内置运算
●   重载使类实例的行为像内置类型
●   重载是通过提供特殊名称的类方法来实现的

常见运算符重载方法：
方法                      重载                      调用
__init__                 构造函数                   对象建立：X = Class(args)
__del__                  析构函数                   X对象收回
__add__                  运算符+                    如果没有_iadd_, X + Y, X += Y
__or__                   运算符|（位OR)              如果没有_ior_, X | Y, X |= Y
__repr__, __str__        转换，打印                  print(X), repr(X), str(X)
__call__                 函数调用                   X(*args, **kwargs)
__getattr__              点号运算                   X.undefined
__setattr__              属性赋值语句                X.any = value
__delattr__              属性删除                   del X.any
__getattribute__         属性获取                   X.any
__getitem__              索引运算                   X[key],X[i:j],没__iter__时的for循环和其他迭代器
__setitem__              索引赋值语句                X[key] = value, X[i:j] = sequence
__delitem__              索引和分片删除               del X[key], del X[i:j]
__len__                  长度                       len(X), 如果没有__bool__,真值测试
__bool__                 布尔测试                   bool(X), 真测试(在Python 2.7中叫做__nonzero__)
__lt__,__gt__,           特定的比较                  X < Y, X > Y, X <= Y, X >= Y
__le__,__ge__,                                     X == Y, X != Y
__eq__,__ne__                                      (在Python 2.7中只有__cmp__)
__radd__                 右侧加法                   Other + X
__iadd__                 实地（增强的）加法           X += Y(or else __add__)
__iter__, __next__       迭代环境                   I = iter(X), next(I); for loops;
                                                  in if no __contains__, all comprehensions, map(F,X)
__contains__             成员关系测试                item in X （任何可迭代的）
__index__                整数值                     hex(X), bin(X), oct(X), O[X], O[X:]
__enter__, __exit__      环境管理器                  with obj as var:
__get__, __set__,        描述符属性                  X.attr, X.attr = value, del X.attr
__delete
__new__                  创建                       在 __init__ 之前创建对象
"""
