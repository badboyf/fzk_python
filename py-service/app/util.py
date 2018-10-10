# -*- coding: utf-8 -*-
'''
Created on 2018年10月10日

@author: Administrator
'''
import json
from datetime import datetime
import time


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return int(time.mktime(obj.timetuple()) * 1000)
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, date):
#             return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def to_json(value):
    return json.dumps(value, cls = ComplexEncoder, ensure_ascii=False)
