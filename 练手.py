#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 10:56
# @Author  : Bilon
# @File    : 练手.py


# 将一个数组里面的奇数的数进行重新排列,0不是奇数
def sort_array(arr):
    """熟手解法"""
    odds = [x if x%2 == 0 else 0 for x in arr]
    evens = sorted([x for x in arr if x%2 == 1])
    even_index = 0
    for index, e in enumerate(odds):
        if e == 0:
            odds[index] = evens[even_index]
            even_index += 1
    return odds

def sort_array1(arr):
    """大神解法"""
    odds = sorted((x for x in arr if x%2 != 0), reverse = True)
    print([x if x%2 == 0 else odds.pop() for x in arr])

# sort_array1([5, 3, 1, 2, 4, 8, 7])


# ATM机允许4或者6位数字，但是这4位或者6位只能是纯数字
def validate_pin(pin):
    """小白解法"""
    try:
        if len(pin) == 4 or len(pin) == 6:
            for n in pin:
                if int(n) >= 0 and int(n) <= 9:
                    return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

def validate_pin(pin):
    """大神解法"""
    return len(pin) in (4,6) and pin.isdigit()

print(validate_pin('1234'))
print(validate_pin('12345'))
print(validate_pin('a234'))
print(validate_pin('-1.234'))