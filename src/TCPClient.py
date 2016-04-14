'''
Created on 2016年3月29日
File Name:TCPClient.py
@author: LindenTao
Description : TCPClient
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
#import sys

HOST, PORT = "localhost", 9999
print('Please input data:')
data = input()
# data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))