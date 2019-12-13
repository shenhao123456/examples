#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : pyvmomi_test.py
@Author: sh
@Date  : 2019/5/7
@Desc  :
"""
from pyVmomi import vim
from pyVim.connect import SmartConnectNoSSL, Disconnect
import atexit

host = "20.26.24.234"
user = "root"
pwd = "root"
port = 443


# 获得vcenter上下文
def get_content():
    si = SmartConnectNoSSL(host=host, user=user, pwd=pwd, port=port, connectionPoolTimeout=-1)
    atexit.register(Disconnect, si)
    content = si.RetrieveContent()
    return content


# 获得vcenter所有集群
def get_all_clusters():
    content = get_content()
    return content.viewManager.CreateContainerView(content.rootFolder, [vim.ComputeResource], True).view


# 获得vcenter所有主机
def get_all_hosts():
    content = get_content()
    return content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True).view


# 获得vcenter所有虚拟机
def get_all_vms():
    content = get_content()
    return content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True).view


# 解决folder嵌套
def getComputeResource(Folder, computeResourceList):
    if hasattr(Folder, 'childEntity'):
        for computeResource in Folder.childEntity:
            getComputeResource(computeResource, computeResourceList)
    else:
        computeResourceList.append(Folder)
    return computeResourceList


# 获得某个名称的集群
def get_cluster_by_name(cluster_name):
    for cluster in get_all_clusters():
        if cluster.name == cluster_name:
            return cluster
    return None


# 获得某个主机
def get_host_by_name(host_name):
    for host in get_all_hosts():
        if host.name == host_name:
            return host
    return None


# 获得某个虚拟机
def get_vm_by_name(vm_name):
    for vm in get_all_vms():
        if vm.name == vm_name:
            return vm
    return None


# 获得虚拟机属性==============================
vm = object
vm.name
vm.runtime.powerState  # 电源状态
vm.config.hardware.numCPU  # cup内核总数
vm.config.hardware.memoryMB  # 内存(总数MB)
vm.config.guestFullName  # 系统信息
vm.guest.ipAddress  # ip
vm.summary #查看详情

# 主机属性=========================================
host = object
host.name   #主机名
host.summary.hardware.vendor   #主机品牌
host.summary.hardware.model
host.summary.hardware.numCpuCores  #cpu核数
round(host.summary.hardware.memorySize / 1024 / 1024, 1)   #内存
'%.1f%%' % ((host.summary.quickStats.overallMemoryUsage /
             (host.summary.hardware.memorySize / 1024 / 1024)) * 100) #内存使用率
host.summary.config.product.fullName  #系统
host.summary #查看详情

#存储器===============================================
datastore=object
round((datastore.summary.capacity) / 1024 / 1024 / 1024,2) #容量
round((datastore.summary.freeSpace) / 1024 / 1024 / 1024, 2) #剩余容量
datastore.summary #查看详情

#触发警报=============================================
alarm=object.triggeredAlarmState


#获得任务与事件======================================
# 根据主机名获得主机以及主机下虚拟机的任务信息
def get_task_by_host_name(host_name, start_date, end_date):
    host = get_host_by_name(host_name)
    vms = host.vm
    filterSpec = vim.TaskFilterSpec()
    byEntity = vim.TaskFilterSpec.ByEntity(entity=host, recursion="self")
    filterSpec.entity = byEntity
    time_filter = vim.TaskFilterSpec.ByTime(beginTime=start_date, endTime=end_date, timeType='queuedTime')
    filterSpec.time = time_filter
    taskManager = get_content().taskManager
    tasks_collector = taskManager.CreateCollectorForTasks(filterSpec)
    tasks = tasks_collector.ReadNextTasks(maxCount=1000)
    tasks_collector.DestroyCollector()
    tasks_list = tasks
    print(taskManager.maxCollector)
    for vm in vms:
        byEntity = vim.TaskFilterSpec.ByEntity(entity=vm, recursion="self")
        filterSpec.entity = byEntity
        tasks_collector = taskManager.CreateCollectorForTasks(filterSpec)
        tasks = tasks_collector.ReadNextTasks(maxCount=1000)
        tasks_collector.DestroyCollector()
        tasks_list = tasks_list + tasks
    return tasks_list

# 根据主机名获得主机以及主机下虚拟机的事件信息
def get_event_by_host_name(host_name, start_date, end_date):
    host = get_host_by_name(host_name)
    vms = host.vm
    filterSpec = vim.event.EventFilterSpec()
    byEntity = vim.event.EventFilterSpec.ByEntity(entity=host, recursion="self")
    filterSpec.entity = byEntity
    time_filter = vim.event.EventFilterSpec.ByTime(beginTime=start_date, endTime=end_date)
    filterSpec.time = time_filter
    eventManager = get_content().eventManager
    events = eventManager.QueryEvents(filterSpec)
    event_list = events
    for vm in vms:
        byEntity = vim.event.EventFilterSpec.ByEntity(entity=vm, recursion="self")
        filterSpec.entity = byEntity
        events = eventManager.QueryEvents(filterSpec)
        event_list = event_list + events
    return event_list
