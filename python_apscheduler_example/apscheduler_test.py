#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 17:18
# @Author  : shenhao
# @File    : apscheduler_test.py
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

executors = {
    'default': ThreadPoolExecutor(10),
}

scheduler = BackgroundScheduler(executors=executors)
scheduler.start()


def fun():
    pass


job = scheduler.add_job(fun, 'interval', minutes=2)
job.remove()
# id删除
scheduler.add_job(fun, 'interval', minutes=2, id='my_job_id')
scheduler.remove_job('my_job_id')
scheduler.get_jobs()
scheduler.get_job(job_id='123')


# import os
#
# from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_JOB_REMOVED, EVENT_JOB_ADDED
# from apscheduler.executors.pool import ProcessPoolExecutor
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.date import DateTrigger
# from apscheduler.triggers.interval import IntervalTrigger
# from apscheduler.triggers.cron import CronTrigger
# from datetime import datetime, timedelta
#
# executors = {
#     'default': ProcessPoolExecutor(os.cpu_count()),
# }
#
# # 后台循环任务管理器
# scheduler = BackgroundScheduler()
#
# trigger = IntervalTrigger(
#     # 开始时间
#     start_date=datetime.now() + timedelta(seconds=3),
#     # 结束时间
#     end_date=datetime.now() + timedelta(seconds=3) + timedelta(seconds=((3 - 1) * 4)),
#     # 每隔多少时间
#     seconds=4
# )
#
#
# def test():
#     print(datetime.now())
#     # print(1 / 0)
#     print('----------------------')
#
#
# def test3():
#     print('success')
#
#
# def test2(scheduler):
#     print(scheduler.get_jobs())
#
#
# def my_listener(event):
#     # print(event.job_id)
#     print(event.code)
#
#
# # scheduler.add_listener(my_listener, EVENT_JOB_REMOVED | EVENT_JOB_ADDED)
#
# # scheduler.add_job(test, 'date', run_date='2016-02-14 15:01:05')  # 在指定的时间，只执行一次
# scheduler.add_job(test, args=(), trigger=trigger, id='1', max_instances=3, misfire_grace_time=30)
# scheduler.add_job(test, args=(), trigger=trigger, id='1', max_instances=3, misfire_grace_time=30)
# # scheduler.add_job(test3, args=(), trigger=DateTrigger(
# #     run_date=(datetime.strptime('2019-09-02 14:52:00', "%Y-%m-%d %H:%M:%S") + timedelta(seconds=3)),
# # ), id='2', max_instances=3, misfire_grace_time=30)
# # scheduler.remove_job('1234')
# # scheduler.add_job(test, args=(), trigger=CronTrigger(hour=9, minute=21))
# # scheduler.add_job(test2, args=([scheduler]), trigger=IntervalTrigger(
# #     # 开始时间
# #     start_date=datetime.now() + timedelta(seconds=2),
# #     # 结束时间
# #     end_date=datetime.now() + timedelta(seconds=2) + timedelta(seconds=((4 - 1) * 3)),
# #     # 每隔多少时间
# #     seconds=3
# # ))
# scheduler.start()
#
# while True:
#     pass


scheduler.shutdown()
