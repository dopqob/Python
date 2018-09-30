#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/30 9:40
# @Author  : Bilon
# @File    : practice.py

""" 1 继承 """


class Adder:
    def add(self, x, y):
        print('not implemented!')

    def __init__(self, start=[]):
        self.data = start

    def __add__(self, other):
        return self.add(self.data, other)


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        new = {}
        for key in x.keys():
            new[key] = x[key]
        for key in y.keys():
            new[key] = y[key]
        return new


""" 2 运算符重载 """


class Mylist:
    def __init__(self, start):
        self.wrapped = []
        for x in start:
            self.wrapped.append(x)

    def __add__(self, other):
        return Mylist(self.wrapped + other)

    def __mul__(self, time):
        return Mylist(self.wrapped + time)

    def __getitem__(self, item):
        return self.wrapped[item]

    def __len__(self):
        return len(self.wrapped)

    def __getslice__(self, low, high):
        return Mylist(self.wrapped[low:high])

    def append(self, node):
        self.wrapped.append(node)

    def __getattr__(self, item):
        return getattr(self.wrapped, item)

    def __repr__(self):
        return repr(self.wrapped)