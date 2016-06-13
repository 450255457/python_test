#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Created on 2016/05/04
File Name:python_test.py
author: LindenTao
Description : test
'''

db.app.insert({ name:'aiqiangua', cname:'爱牵挂', created_at:now()})


JS：http://www.w3school.com.cn/js/js_obj_date.asp
bootstrap:http://www.runoob.com/bootstrap/bootstrap-forms.html
curl
ui_methods
tornado
gevent

https://www.uedsc.com/ecshop-structure-of-the-database-and-table-introduction.html
http://www.aircheng.com/product
http://www.z139.cn/2015/%E4%B8%80%E6%AC%BE%E5%BC%80%E6%BA%90%E5%95%86%E5%9F%8E%E7%9A%84%E6%95%B0%E6%8D%AE%E8%A1%A8%E7%BB%93%E6%9E%84-%E5%85%B3%E4%BA%8E%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BE%E8%AE%A1%E6%80%9D%E8%B7%AF/206.html

get_remaining_power
http://120.24.47.205:8888/api/locationdata?/868219000080553
http://120.24.47.205:8888/api/device/868219000080553
http://127.0.0.1:8888/api/device/868219000080553
http://120.24.47.205:8888/api/device/868219000080116/get_wifi
http://120.24.47.205:8888/api/device/868219000080116/data/remaining_power
curl -v -A CURL -b cookies.txt http://127.0.0.1:8000/api/device/868219000080116/get_wifi

db.collection_name.update({"_id":ObjectId("57523baf36dc6a16940abdb6")},{"$unset":{"test":1}})   //从文档中移除指定的键
