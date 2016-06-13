#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2016/4/28
File Name:tcp_client.py
author: LindenTao
Description : a so easy tcp c
'''

import socket

#HOST, PORT = "115.29.34.8", 8090
HOST, PORT = "127.0.0.1", 8090
data = '@B#@,V01,1,111112222233333,8888888888888888,@E#@'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	sock.connect((HOST,PORT))
	sendlen = sock.send(data)
	print('send ok,%d' % sendlen)
	#received = sock.recv(1024)
finally:
	sock.close()

print("Sent:{}".format(data))
#print("Received:{}".format(received))