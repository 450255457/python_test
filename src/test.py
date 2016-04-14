#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from mongoengine import *
from mongoengine.connection import connect

connect('test')

class BlogPost(Document):
    title = StringField(required=True, max_length=200)
    posted = DateTimeField(default=datetime.datetime.now)
    tags = ListField(StringField(max_length=50))

class TextPost(BlogPost):
    content = StringField(required=True)

class LinkPost(BlogPost):
    url = StringField(required=True)

# Create a text-based post
post1 = TextPost(title='Using MongoEngine', content='See the tutorial')
post1.tags = ['mongodb', 'mongoengine']
post1.save()
    
