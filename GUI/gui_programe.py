#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 9:08
# @Author  : Bilon
# @File    : gui_programe.py
import wx


app = wx.App()  # 创建应用
win = wx.Frame(None, title='Bilon‘s 文本编辑器', size=(400, 320))    # 创建框架
pan = wx.Panel(win)
pan.SetBackgroundColour('#666666')
win.Show()
app.MainLoop()
