#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 14:47
# @Author  : Bilon
# @File    : mydir.py

'''
mydir.py: a module that list the namespaces of other modules
列出模块的命名空间
'''
seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)

    count = 0
    for attr in module.__dict__:
        print('{:02}) {:<12} '.format(count, attr), end= ' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has {} names'.format(count))
        print(sepline)

if __name__ == '__main__':
    import list_module
    listing(list_module)
