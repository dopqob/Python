#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 17:18
# @Author  : Bilon
# @File    : flask_app.py
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_from():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123456':
        return render_template('signin-ok.html')
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()
