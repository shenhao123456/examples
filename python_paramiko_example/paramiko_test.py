#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : paramiko_test.py
@Author: sh
@Date  : 2019/5/7
@Desc  :
"""
import paramiko

#上传文件到服务器，并执行脚本，并返回输出
def upload_and_exe_script(host, username, password, port, filename, sh, cmd):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    #上传文件
    if filename:
        sftp.put('path/' + filename, '/usr/local/' + filename)
    #上传脚本
    sftp.put('path/' + sh, '/usr/local/' + sh)

    #下载文件
    # sftp.get(remotepath, localpath)
    transport.close()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    #执行脚本命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    #返回执行脚本结果
    return stdout.readlines()

    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect('21.254.248.121', 22, 'root', 'root')
    # stdin, stdout, stderr = ssh.exec_command('python /usr/local/test2.py', get_pty=True)
    # while True:
    #     nextline = stdout.readline().strip()  # 读取脚本输出内容
    #     print(nextline)  # 发送消息到客户端
    #     if not nextline:
    #         break
    # ssh.close()  # 关闭ssh连接
