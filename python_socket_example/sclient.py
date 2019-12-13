#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 10:03
# @Author  : shenhao
# @File    : sclient.py
import socket, time

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9999))
    while True:
        msg = input('>>')
        if msg == 'bye':
            sock.send(msg)
            sock.close()
            break
        else:
            sock.send(msg.encode('utf-8'))
            data = sock.recv(1024)
            print(data.decode())
