#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 10:56
# @Author  : Bilon
# @File    : 5道练手题.py


# 将一个数组里面的奇数的数进行重新排列,0不是奇数
def sort_array(arr):
    """熟手解法"""
    odds = [x if x % 2 == 0 else 0 for x in arr]
    evens = sorted([x for x in arr if x % 2 == 1])
    even_index = 0
    for index, e in enumerate(odds):
        if e == 0:
            odds[index] = evens[even_index]
            even_index += 1
    return odds


def sort_array1(arr):
    """大神解法"""
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    print([x if x % 2 == 0 else odds.pop() for x in arr])

# sort_array1([5, 3, 1, 2, 4, 8, 7])


# ATM机允许4或者6位数字，但是这4位或者6位只能是纯数字
def validate_pin(pin):
    """小白解法"""
    try:
        if len(pin) == 4 or len(pin) == 6:
            for n in pin:
                if 0 <= int(n) <= 9:
                    return True
        else:
            return False

    except Exception as e:
        print(e)
        return False


def validate_pin1(pin):
    """大神解法"""
    return len(pin) in (4, 6) and pin.isdigit()

# print(validate_pin('1234'))
# print(validate_pin('12345'))
# print(validate_pin('a234'))
# print(validate_pin('-1.234'))


# 给你几个字符串，按照下面的规则编写一个函数输出，指定格式的字符串:
# accm("abcd") #A-Bb-Ccc-Dddd
# accm("RqaEzty") #R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy
# accm("cwAt") # C-Ww-Aaa-Tttt
def accm(chars):
    """小白解法"""
    new_chars = []
    for index, c in enumerate(chars):
        words = []
        [words.append(c) for x in range(0, index+1)]
        # capitalize()将字符串的第一个字母变成大写,其他字母变小写
        new_chars.append(''.join(words).capitalize())

    return '-'.join(new_chars)


def accm1(chars):
    """大牛解法"""
    return '-'.join(c.upper() + c.lower()*index for index, c in enumerate(chars))


# print(accm1('cwAt'))


# 推导一个数组：给你数组的前三个数字，后一个数字是前3个数字之和，要求返回前n个数字
def tri(nums_list, n):
    """小白解法"""
    a, b, c = nums_list[0], nums_list[1], nums_list[2]
    count = len(nums_list)
    while count < n:
        a, b, c = b, c, a+b+c
        count += 1
        nums_list.append(c)

    print(nums_list)


def tri1(nums_list, n):
    """熟手解法： 用闭包+生成器来搞定"""
    def gen():
        a, b, c = nums_list[0], nums_list[1], nums_list[2]
        count = len(nums_list)
        while count < n:
            a, b, c = b, c, a+b+c
            count += 1
            yield c

    print(nums_list + list(gen()))


def tri2(nums_list, n):
    """大牛解法：巧妙的利用了列表的切片和负数index"""
    res = nums_list[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))

    print(res)


# tri([0, 0, 1], 10)
# tri1([0, 0, 1], 10)
# tri2([0, 0, 1], 10)


# 字符天平秤
# 每个问号(?)的权重是3，每个感叹号(!)的权重是2,把两个字符放左边，把两个字符放右边，看看它们是否平衡?
# Example:
#     balance("!!","??")=="Right"
#     balance("!??","?!!")=="Left"
#     balance("!?!!","?!?")=="Left"
#     balance("!!???!????","??!!?!!!!!!!")=="Balance"
def balance(left, right):
    """小白解法"""
    weight = {'?': 3, '!': 2}
    left_num = sum([weight.get(e) for e in left])
    right_num = sum([weight.get(e) for e in right])

    if left_num == right_num:
        return 'Balance'
    elif left_num > right_num:
        return 'Left'
    else:
        return 'Right'


def balance1(left, right):
    """大神解法"""
    v1 = left.count('!')*2 + left.count('?')*3
    v2 = right.count('!')*2 + right.count('?')*3
    val = v1 - v2
    return 'Right' if val < 0 else 'Left' if val > 0 else 'Balance'


# Python assert 断言函数是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常
assert balance('!!', '??') == 'Right'
assert balance("!??", "?!!") == "Left"
assert balance("!?!!", "?!?") == "Left"
assert balance("!!???!????", "??!!?!!!!!!!") == "Balance"
print(balance1("!!", "??"))
print(balance1("!??", "?!!"))
print(balance1("!?!!", "?!?"))
print(balance1("!!???!????", "??!!?!!!!!!!"))
