# -*- coding: utf-8 -*-  
'''
Created on 2018-10-09

@author: Administrator
'''

from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return "ok"

# app.run('localhost', 9000)