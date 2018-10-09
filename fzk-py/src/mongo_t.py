# -*- coding: utf-8 -*-  
'''
Created on 2018年9月29日

@author: Administrator
'''
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId
import re

mongo_host='local.vm.sss.com'
mongo_port=27017

client = MongoClient(mongo_host, mongo_port)

db_platform_tk = client['platform-tk']
ygbase_data_c = db_platform_tk['ygbaseData']

data=ygbase_data_c.find_one()
pprint(data)

print(ObjectId())
print('*'*100)
print(ygbase_data_c.find({"error" : False, '_id': re.compile('^BFEGZSX060')}).count())
# print(ygbase_data_c.find({"error" : False, '_id': {'$regex' : '^BFEGZSX060'}}).count())

max_time=None
min_time=None
cnt=0
for index, data in enumerate(ygbase_data_c.find({'_id': re.compile('^BFEGZSX060')})):
    tmp = data['date']
    max_time = tmp if max_time == None or max_time < tmp else max_time
    min_time = tmp if min_time == None or min_time > tmp else min_time
    cnt = index + 1
print(max_time)
print(min_time)
print(cnt)
print((max_time - min_time).seconds / cnt)
