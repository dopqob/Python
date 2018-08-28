# 表10-1: Python语句

# 赋值
a, b, c = 'good', 'bad', 'ugly'

# 调用
log .write("spam, ham")

# if/elif/else 选择动作
text = 'hello world'
if "python" in text:
    print(text)

# for/else 序列迭代
mylist = ['a', 'b', 'c']
for x in mylist:
    print (x)

# while/else 一般循环
while 1 > 0:
    print ('hello')

# pass 空占位符
while True:
    pass

# break 循环退出
while True:
    if exittest(): break

# continue循环继续
while True:
    if skiptest(): continue

# def 函数和方法
def f1(a, b, C=1, *d):
    print(a+b+c+d[0])

# return 函数结果
def f(a, b, C=1, *d):
    return a+b+c+d[0]

# yield 生成器函数
def gen(n):
    for i in n: yield i*2

# global 命名空间
x = 'old'
def function():
    global x, y; x = 'new'

# nonlocal 命名空间
def outer():
    x = 'old'
    def function():
        nonlocal x; x = 'new'

# import 模块访问
import sys

# from 属性访问
from sys import stdin

#class 创建对象
class Subclass(Superclass):
    staticData = []
    def method(self): pass

#try/except/finally 捕捉异常
try:
    action()
except:
    print ('action error' )

# raise 触发异常
raise EndSearch( location)

# assert 调试检查
assert X > Y,'X too small'

# with/as 环境管理器(2.6)
with open('data') as myfile:
    process(myfle)

# del 删除引用
del data[k]
del data[i:j]
del obj.attr
del variable
