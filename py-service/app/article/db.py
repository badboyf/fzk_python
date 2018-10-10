# -*- coding: utf-8 -*-
'''
Created on 2018年10月10日

@author: Administrator
'''

from ..config import get_config
from pymongo import MongoClient

ARTICAL = 'artical'

_article_c = None

def init_db():
    cfg = get_config()
    host = cfg["mongo"]["host"]
    port = cfg["mongo"]["port"]
    db = cfg["mongo"]["db"]
    client = MongoClient(host, port)

    return client[db]


def get_article_c():
    global _article_c
    if(_article_c == None):
        _article_c = init_db()[ARTICAL]
    return _article_c

def create(article):
    get_article_c().insert(article.__dict__)

def get_all():
    return get_article_c().find()

def get_one(article_id):
    return get_article_c().find_one({'_id' : article_id})

def delete(article_id):
    get_article_c().remove({"_id": article_id})