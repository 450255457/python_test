#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Created on 2016/05/07
File Name:py_mongoengine.py
@author: LindenTao
@Description : python模块之mongoengine
'''

from mongoengine import *
from datetime import datetime

#连接数据库:test
# connect('test')    # 连接本地test数据库
connect('test', host='115.29.34.8', port=27017)

# Defining our documents
# 定义文档user,post,对应集合user,post
class User(Document):
    # required为True则必须赋予初始值
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    date = DateTimeField(default=datetime.now(), required=True)
    
# Embedded documents,it doesn’t have its own collection in the database
class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)
      
class Post(Document):
    title = StringField(max_length=120, required=True)
    # ReferenceField相当于foreign key
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    # 允许继承
    meta = {'allow_inheritance': True}
 
class TextPost(Post):
    content = StringField()
 
class ImagePost(Post):
    image_path = StringField()
 
class LinkPost(Post):
    link_url = StringField()

# Dynamic document schemas:DynamicDocument documents work in the same way as Document but any data / attributes set to them will also be saved
class Page(DynamicDocument):
    title = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.now())
     
# # 添加数据
# john = User(email='john@example.com', first_name='John', last_name='Tao').save()
# ross = User(email='ross@example.com')
# ross.first_name = 'Ross'
# ross.last_name = 'Lawley'
# ross.save()
# 
# comment1 = Comment(content='Good work!',name = 'LindenTao')
# comment2 = Comment(content='Nice article!')
# post0 = Post(title = 'post0',tags = ['post_0_tag'])
# post0.comments = [comment1,comment2]
# post0.save()
#    
# post1 = TextPost(title='Fun with MongoEngine', author=john)
# post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
# post1.tags = ['mongodb', 'mongoengine']
# post1.save()
#      
# post2 = LinkPost(title='MongoEngine Documentation', author=ross)
# post2.link_url = 'http://docs.mongoengine.com/'
# post2.tags = ['mongoengine']
# post2.save()
#  
# # Create a new page and add tags
# page = Page(title='Using MongoEngine')
# page.tags = ['mongodb', 'mongoengine']
# page.save()

## 查看数据
#for post in Post.objects:
#    print post.title
#    print '=' * len(post.title)
      
#    if isinstance(post, TextPost):
#        print post.content
      
#    if isinstance(post, LinkPost):
#        print 'Link:', post.link_url
         
## 通过引用字段直接获取引用文档对象    
#for post in TextPost.objects:
#    print post.content
#    print post.author.email  
#au = TextPost.objects.all().first().author
#print au.email
      
## 通过标签查询    
#for post in Post.objects(tags='mongodb'):
#    print post.title
          
#num_posts = Post.objects(tags='mongodb').count()
#print 'Found %d posts with tag "mongodb"' % num_posts
  
## 更新文档
ross = User.objects(first_name = 'Ross')
ross.delete()
#ross.update(date = datetime.now())
#User.objects(first_name='John').update(set__email='123456@qq.com')