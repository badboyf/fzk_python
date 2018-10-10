# -*- coding: utf-8 -*-
'''
Created on 2018年10月10日

@author: Administrator
'''

from bson.objectid import ObjectId
import datetime

class Article(object):
    def __init__(self, **args):
        self._id = ObjectId().__str__()
        self.content = args.get('content')
        self.author = args.get('author')
        self.create_time = datetime.datetime.utcnow()
        if(args.get('update_time')):
            self.update_time = datetime.datetime.fromtimestamp(args.get('update_time') / 1000)
        else:
            self.update_time = datetime.datetime.utcnow()

