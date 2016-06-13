#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Created on 2016/05/13
File Name:py_pymongo.py
author: LindenTao
Description : mongo demo
'''

import pymongo
from pymongo import MongoClient
import datetime

#连接mongo
client = MongoClient()
#client = MongoClient("localhost", 27017)
#client = MongoClient('mongodb://localhost:27017/')

#创建/连接数据库
db = client.test
#db = client['test']

#添加数据
db.test_collection.save({"x": 10})
db['test_collection'].save({"x": 8})
db.test_collection.save({"x": 11})

post = {"author": "Mike",
"text": "My first blog post!",
"tags": ["mongodb", "python", "pymongo"],
"date": datetime.datetime.utcnow()}

posts = db.posts

#增加数据并返回其_id值
post_id = posts.insert_one(post).inserted_id
print post_id
print posts.find_one({"_id": post_id})

new_posts = [{"author": "Mike",
"text": "Another post!",
"tags": ["bulk", "insert"],
"date": datetime.datetime(2009, 11, 12, 11, 14)},
{"author": "Eliot",
"title": "MongoDB is fun",
"text": "and pretty easy too!",
"date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
print result.inserted_ids

#查询
#查看数据库名
print db.name

#查看集合信息
print db.test_collection
#print db['test_collection']

#查看集合中的第一个文档
print db.test_collection.find_one()
print posts.find_one({"author": "Mike"})

#遍历集合，输出
for item in db.test_collection.find():
    print item["x"]

#查看非系统集合
print db.collection_names(include_system_collections=False)

#计数
print posts.count()
posts.find({"author": "Mike"}).count()

#创建索引
db.test_collection.create_index("x")
#遍历，排序输出
for item in db.test_collection.find().sort("x", pymongo.ASCENDING):
    print item["x"]