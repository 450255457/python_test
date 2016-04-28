#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Created on 2016/4/28
File Name:tcp_server.py
author: LindenTao
Description : a so easy tcp server
'''

import socket
import threading
import time

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    while True:
        data = sock.recv(1024)
        print('recvbuf :%s'% data)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

# 创建socket  
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
sockfd.bind(('0.0.0.0', 8090))
sockfd.listen(5)
print 'Waiting for connection...'
while True:
    # 接受一个新连接:
    sock, addr = sockfd.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    
