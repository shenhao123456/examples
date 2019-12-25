#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 15:24
# @Author  : shenhao
# @File    : ws_client.py


# websocket-client	0.56.0
import websocket


def on_message(ws, message):
    # print(ws)
    print(message)


def on_error(ws, error):
    # print(ws)
    print(error)


def on_close(ws):
    # print(ws)
    print("### closed ###")


websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws/v1.0/probe_device/48",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()