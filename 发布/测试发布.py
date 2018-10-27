#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 10:52
# @Author  : Bilon
# @File    : 测试发布.py

import paramiko, sys
from selenium import webdriver

# 创建SSHClient实例对象
ssh = paramiko.SSHClient()

# 调用方法，表示没有储存远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程机器 地址、端口、用户名密码
ssh.connect('116.62.170.64', 22, 'root', 'Ejuster2017')     # 测试

# 测试环境
local = r'F:\ccloud2.0\ccloud-web-admin-test.war'
server = '/usr/www/ccloud-web-admin-test.war'
path = '/usr/www/ccloud.ejuster.com'
bakpath = '/usr/www/ccloud.ejuster.com.bak'


# 执行cmd重复性太高，可以抽象成函数
def remoteRun(cmd, printOutput = True):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode()  # stdout.read()读出来的是字节串，用decode()转换为字符串
    errinfo = stderr.read().decode()
    if printOutput:
        print(output + errinfo)
    return output + errinfo


# 检查应用是否运行
cmd = 'ps -ef | grep tomcat-ccloud | grep -v grep'
output = remoteRun(cmd)

# 如果存在，则杀死进程
if '-Dcatalina.home=/usr/local/tomcat-ccloud' in output:
    print('服务运行中，停止服务...')

    parts = output.split(' ')       # 将输出用空格分割成列表

    # 去掉空字符串
    parts = [part for part in parts if part]
    print(parts)

    # 获取进程id
    pid = parts[1]

    # 杀掉进程
    output = remoteRun(f'kill -9 {pid}')
    if '-Dcatalina.home=/usr/local/tomcat-ccloud' in output:
        print('无法杀死进程！！！')
        # 退出程序
        sys.exit(3)

    else:
        print('停止成功')

# 删除旧的代码包
print('删除旧的代码包...')
remoteRun(f'rm -rf {server}')

# 上传安装包
print('上传安装包...', end='')
sftp = ssh.open_sftp()
sftp.put(local, server)
sftp.close()
print('ok')

# 删除旧备份，生成新备份
print('删除旧备份，生成新备份')
remoteRun(f'rm -rf {bakpath}; \
          cp -r {path} {bakpath}')

# 解压安装包
print('解压安装包...', end='')
remoteRun(f'unzip -o {server} -d {path}', printOutput = False)
print('ok')

# 修改配置文件
print('修改配置文件')
remoteRun(f'cp -r {bakpath}/WEB-INF/classes/db.properties {path}/WEB-INF/classes/; \
          cp -r {bakpath}/WEB-INF/classes/j2cache.properties {path}/WEB-INF/classes/')

# 启动服务,需先用source /etc/profile读入环境变量的数据才能启动
print('启动服务...')
remoteRun('source /etc/profile; /usr/local/tomcat-ccloud/bin/startup.sh')

# 检查是否运行成功
print('检查是否启动成功')
output = remoteRun('sleep 20; ps -ef | grep tomcat-ccloud | grep -v grep')
if '-Dcatalina.home=/usr/local/tomcat-ccloud' in output:
    print('服务运行成功')
else:
    print('服务启动失败！！')
    sys.exit()

# 浏览器访问登录页面验证服务是否启动
webdriver.Chrome().get('http://test.juster.com.cn/admin')       # 测试
