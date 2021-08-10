# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask
from flask import request
from flask import current_app
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1>'+'<p>Your browser is {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, again  {}!</h1>'.format(name)+"your app is "+current_app.name



if __name__ == '__main__':
    app.run(port=8081,host='0.0.0.0',debug=True)
