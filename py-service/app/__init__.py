# -*- coding: utf-8 -*-  
'''
Created on 2018-10-09

@author: Administrator
'''

from flask import Flask
from app.article import article

# def create_app():
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/health')
    def health_check():
        return 'ok'

    app.register_blueprint(article.blueprint)
    
    app.add_url_rule('/', endpoint='health_check')
    
    return app

