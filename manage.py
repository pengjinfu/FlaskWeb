#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Dreamer
# Time:2018.9.1
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    content = "我是第一个模板"
    return render_template('index.html', content=content)


@app.route('/service')
def service():
    return "Service"


@app.route('/about')
def about():
    return "About"


@app.route('/user/<int:user_id>')
def user(user_id):
    return "User %d" % user_id


if __name__ == '__main__':
    app.run(debug=True)
