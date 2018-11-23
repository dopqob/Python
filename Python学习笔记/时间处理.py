#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 18:47
# @Author  : Bilon
# @File    : 时间处理.py
import calendar
import time
import datetime
import dateutil


"""
# =============================================
# Time模块
# =============================================
"""


def calc_num():
    """计算十万行代码运行的时间"""
    num = 1
    for i in range(1, 100000):
        num = num * i
    return num


# print('-'*20, '计算十万行代码运行时间', '-'*20)
print('{:-^50}'.format('计算十万行代码运行时间'))
start_time = time.time()
# num = calc_num()
end_time = time.time()
# print('结果是 {} 位数'.format(len(str(num))))
print('运行耗时 {} 秒'.format(end_time - start_time))
print('{:-^54}'.format('计算结束'))
# print('-'*20, '      计算结束      ', '-'*20)


"""
# ==============================================
# Datetime模块
# ==============================================
"""
# 获取当前时间
print(datetime.datetime.now())

# 获取当前日期
print(datetime.date.today())

# 获取离圣诞节的时间差
chrismas_day_gap = datetime.datetime(2018, 12, 25, 0, 0, 0) - datetime.datetime.now()
print(chrismas_day_gap)


"""
# ==============================================
# Datetime模块--timedelta子模块
# ==============================================
"""
# 计算某天的前后100天
d1 = datetime.datetime(2018, 10, 13)
print(d1 + datetime.timedelta(days=100))
print(d1 - datetime.timedelta(days=100))

# 计算两个日期相差多少天
d2 = datetime.datetime(2018, 11, 11)
d3 = datetime.datetime(1988, 4, 17)
print(d2 - d3)


"""
# ==============================================
# Dateutil模块--处理复杂的日期问题（时区、月份等）
# ==============================================
"""
d4 = datetime.datetime(2018, 11, 13)
# print(d4 + dateutil.relativedelta.relativedelta(months=3))  # 三个月后的日期
# print(d4 - dateutil.relativedelta.relativedelta(months=20))  # 二十个月前的日期


"""
# =============================================
# Calendar模块--日历
# =============================================
"""
# 打印某年某月的日历
print(calendar.month(2018, 11))

# 计算本月的最后一天
today = datetime.date.today()
_, last_day_num = calendar.monthrange(today.year, today.month)
print(last_day_num)

# 计算2008-2017年2月份的天数，有多少闰年
for year in range(2008, 2018):
    _, last_day_num = calendar.monthrange(year, 2)
    print(year, last_day_num)

# 简单的写法
print(list(year for year in range(2008, 2018) if calendar.monthrange(year, 2)[1] == 29))


"""
# =============================================
# 字符串和日期的转换
# %y    显示两位数的年份（00-99）
# %Y    显示四位数的年份（000-9999）
# %m    月份（01-12）
# %d    日（1-31）
# %H    24小时制小时数（0-23）
# %I    12小时制小时数（01-12）
# %M    分钟数（00-59）
# %S    秒（00-59）
# =============================================
"""
# 把字符串转日期
cday = datetime.datetime.strptime('2018-2-6 15:33:25', '%Y-%m-%d %H:%M:%S')
print(cday, type(cday))

# 把日期转字符串
now = datetime.datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
