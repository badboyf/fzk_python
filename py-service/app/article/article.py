# -*- coding: utf-8 -*-  
'''
Created on 2018年10月10日

@author: Administrator
'''

from flask import Blueprint, request
from app.article import db
from .. import util
from .model import Article
import json

blueprint = Blueprint('article', __name__, url_prefix='/article')

@blueprint.route('/', methods = ['GET'])
def get_all():
    result = []
    for tmp in db.get_all():
        result.append(tmp)
    return util.to_json(result)

@blueprint.route('/', methods = ['POST'])
def create_article():
    body =  json.loads(request.data)
    article = Article(**body)
    db.create(article)
    return "success"

@blueprint.route('/<string:article_id>', methods = ['DELETE'])
def delete(article_id):
    db.delete(article_id)
    return 'sucess'

@blueprint.route('/<string:article_id>', methods = ['GET'])
def get_one(article_id):
    data = db.get_one(article_id)
    return util.to_json(data)


