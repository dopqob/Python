#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 9:02
# @Author  : Bilon
# @File    : 远程操作.py

import paramiko

# 创建SSHClient实例对象
ssh = paramiko.SSHClient()

# 调用方法，表示没有储存远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程机器 地址、端口、用户名密码
ssh.connect('116.62.170.64', 22, 'root', 'Ejuster2017')

# 创建目录
cmd = 'mkdir bilon2222222'
ssh.exec_command(cmd)

# 将内容写入文件
cmd = '''echo '1234
5678
90abc' > myfile
'''
ssh.exec_command(cmd)

# 获取命令的执行结果
# cmd = 'cat myfile'
# stdin, stdout, stderr = ssh.exec_command(cmd)

# stdin, stdout, stderr = ssh.exec_command('rm -rf bilon2222222; rm myfile', get_pty=True)
stdin, stdout, stderr = ssh.exec_command('rm -rf bilon2222222; rm myfile')

print(stdout.read() + stderr.read())
ssh.close()
