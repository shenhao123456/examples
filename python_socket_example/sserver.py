#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 10:04
# @Author  : shenhao
# @File    : sserver.py
import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 5000))
    sock.listen(10)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        print(data)
        if data == 'bye':
            break
        else:
            msg = input('>>')
            conn.send(msg.encode('utf-8'))
    sock.close()
