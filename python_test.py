#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Created on 2016/05/07
File Name:py_test.py
author: LindenTao
Description : list test demo
'''

import pymongo

conn = pymongo.Connection("115.29.34.8", 27017)
db = conn.test
print db.collection_names()