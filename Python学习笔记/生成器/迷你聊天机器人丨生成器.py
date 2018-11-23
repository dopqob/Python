#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 19:26
# @Author  : Bilon
# @File    : 迷你聊天机器人丨生成器.py


def chat_robot():
    res = ''
    while True:
        receive = yield res
        if 'hi' in receive or 'hello' in receive or '你好' in receive:
            res = '你好，主人'
        elif 'name' in receive or '名字' in receive or '姓名' in receive or '叫什么' in receive:
            res = '我叫暖暖，我是你的专属机器人'
        elif 'age' in receive or '年龄' in receive or '几岁' in receive:
            res = '我还未满一岁呢'
        elif 'sex' in receive or '性别' in receive:
            res = '我是无敌美少女,哈哈'
        elif 'where' in receive or '哪人' in receive:
            res = '荸荠制造了我'
        elif 'height' in receive or '身高' in receive:
            res = '不告诉你'
        elif 'help' in receive or '命令' in receive:
            res = '您可以尝试问我一些简单的问题，比如身高、姓名、性别等等'
        elif '哈哈' in receive:
            res = '什么事让您这么高兴呢，能跟暖暖分享一下吗？'
        elif 'bye' in receive or '再见' in receive or '拜拜' in receive:
            res = '拜拜，See U la la'
        else:
            res = '很抱歉，我没能理解您的指令 [{}],请输入help了解更多指令'.format(receive)


Chat = chat_robot()
next(Chat)

while True:
    order = input('请输入您的指令，主人： ')
    if order == 'quit' or order == '退出':
        print('Robot exit...')
        break
    response = Chat.send(order)
    print('Robot: {}\n'.format(response))
    if '拜拜' in response:
        break
Chat.close()
