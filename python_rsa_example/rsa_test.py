#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : rsa_test.py
@Author: sh
@Date  : 2019/5/7
@Desc  :
"""
import rsa

# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)

# 保存密钥
with open('public.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode())

with open('private.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode())

# 导入密钥
with open('public.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

with open('private.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

#公钥向私钥发送
# 明文
message = '这是机密'

#用公钥加密明文
crypto_email_text = rsa.encrypt(message.encode(), pubkey)
#打印一下
print(crypto_email_text)

#私钥解密。获得明文
message = rsa.decrypt(crypto_email_text, privkey).decode()

print(message)


# =================================

# 私钥向公钥发送消息，采用签名方式
message = '这是机密'

# 私钥生成签名
crypto_email_text = rsa.sign(message.encode(), privkey, 'MD5')

print(crypto_email_text)

# 使用公钥解密签名和明文对比
rsa.verify(message.encode(), crypto_email_text, pubkey)
#失败则会出现异常，成功显示算法方式
print(rsa.verify(message.encode(), crypto_email_text, pubkey))


import hashlib

md = hashlib.md5()
password='123456'
md.update(password.encode())
new_pwd = md.hexdigest()
print(new_pwd)
