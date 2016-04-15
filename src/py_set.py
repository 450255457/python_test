#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Created on 2016/4/15
File Name:py_set.py
author: LindenTao
Description : set(集合)
'''

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)     # create a set without duplicates
print(fruit)
print('orange' in fruit)    # fast membership testing
print('crabgrass' in fruit)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a,b)      # unique letters in a, b
# 差补/相对补集( - ),等价方法：difference()，letters in a but not in b
print('a - b : ', a - b, a.difference(b))
# 联合( | ),等价方法：union()，letters in either a or b
print('a | b : ', a | b, a.union(b))
# 交集( & ),等价方法：intersection(),letters in both a and b
print('a & b : ', a & b, a.intersection())
# 对称差分( ^ ),等价方法：symmetric_difference,letters in a or b but not both
print('a ^ b : ', a ^ b, a.symmetric_difference(b))