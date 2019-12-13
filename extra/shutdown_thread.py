#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 15:07
# @Author  : shenhao
# @File    : shutdown_thread.py

import threading
import time
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def test():
    while True:
        print(threading.current_thread().getName())
        time.sleep(1)


if __name__ == "__main__":
    t_list = []


    def get_t(name):
        for t in t_list:
            if t.getName() == '线程' + name and t.is_alive():
                return t
        return None


    for i in range(4):
        t = threading.Thread(target=test, name="线程" + str(i))
        t_list.append(t)
        t.start()
    print(len(t_list))
    time.sleep(1)
    print("main thread sleep finish")
    stop_thread(get_t('2'))
    for t in t_list:
        print(t.getName(), t.is_alive())
    t = threading.Thread(target=test, name="线程2")
    t_list.append(t)
    t.start()
    while True:
        time.sleep(1)
        for t in t_list:
            print(t.getName(), t.is_alive())
