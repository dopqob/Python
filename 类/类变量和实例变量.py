#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 15:46
# @Author  : Bilon
# @File    : 类变量和实例变量.py

'''面向对象三要素'''
'''
1.封装
    组装：将数据和操作组装到一起（属性和方法的封装）
    隐藏数据：对外只暴露一些接口，通过接口访问对象
    
2.继承
    多复用，继承来的就不用自己写了
    多继承少修改，OCP（Open-closed Principle），使用继承来改变，来体现个性

3.多态
    面向对象编程最灵活的地方——动态绑定
'''

class MyClass:
    '''this is a class'''
    x = 123

    def __init__(self):     # 初始化 构造器 构造方法
        pass

    def foo(self):
        return 'foo = {}'.format(self.x)


# a = MyClass()   # 实例化时就会调用 __init__
# print(a.foo())



class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age


    def showage(self):
        print('{} is {}'.format(self.name, self.age))

# tom = Person('Tom', 25)
# jerry = Person('Jerry', 20)
#
# tom.showage()
# jerry.showage()
# jerry.age += 1
# print(jerry.age)
# jerry.showage()

'''
实例对象instance
类实例化后一定会获得一个对象，就是实例对象
上例中的tom、jerry就是Person类的实例

__init__方法的第一个参数self就是指代某一个实例
类实例化出一个实例对象，实例对象会绑定方法，调用方法时采用jerry.showage()的方式
但是定义是showage(self),少传一个参数吗？
这个self就是jerry，Python会把方法的调用者作为第一参数self的实参传入
self.name就是jerry对象的name,name是保存在了jerry对象上，而不是Person类上，所以称为
实例变量
'''

class MyClass2:
    def __init__(self):
        print('self in init = {}'.format(id(self)))


# c = MyClass2()      # 会调用__init__
# print('c = {}'.format(id(c)))
# 运行结果
# self in init = 2390528870048
# c = 2390528870048


'''
实例变量是每个实例自己的变量，是自己独有的；
类变量是类的变量，是类的所有实例共享的属性和方法；

特殊属性              含义
__name__            对象名
__class__           对象的类型
__dict__            对象的属性的字典
__qualname__        类的限定名
'''

a = Person('Marry')
b = Person('John', 20)

print(a.__class__, b.__class__)
print(a.__class__.__qualname__, a.__class__.__name__)

print(sorted(Person.__dict__.items()), end='\n\n')
print(sorted(a.__dict__.items()), end='\n\n')
print(b.__dict__)


# 例子
class Person1:
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

tom = Person1('tom')
jerry = Person1('jerry', 20)

Person1.age = 30
print(Person1.age, tom.age, jerry.age)

print(Person1.__dict__, tom.__dict__, jerry.__dict__, sep='\n')
print(Person1.height, tom.height, jerry.height)
Person1.height += 20
print(Person1.height, tom.height, jerry.height)
print(Person1.__dict__, tom.__dict__, jerry.__dict__, sep='\n')

tom.height = 168
print(Person1.height, tom.height, jerry.height)
print(Person1.__dict__, tom.__dict__, jerry.__dict__, sep='\n')

jerry.height += 30
print(Person1.height, tom.height, jerry.height)
print(Person1.__dict__, tom.__dict__, jerry.__dict__, sep='\n')

Person1.weight = 70
print(Person1.weight, tom.weight, jerry.weight)

print(tom.__class__.__dict__ == Person1.__dict__)


'''
是类的，也是这个类所有实例的，实例都可以访问到
是实例的，就是这个实例自己的，通过类访问不到
类变量是属于类的变量，这类的所有实例可以共享这个变量

实例可以动态的给自己增加一个属性，实例.__dict__[变量名]和实例.变量名都可以访问到
实例的同名变量会隐藏这个类变量，或者说是覆盖了这个类变量

实例属性的查找顺序
指的是实例使用.来访问属性，会先找到自己的__dict__，如果没有，就会通过属性__class__找到自己的类，再去类的__dict__中找
注意，如果实例使用__dict__[变量名]访问变量，将不会按照上面的顺序查找变量了

一般来说，类变量使用全大写来命名
'''