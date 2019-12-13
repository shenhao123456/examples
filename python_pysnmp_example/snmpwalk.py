#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : snmpwalk.py
@Author: sh
@Date  : 2019/3/27
@Desc  :
"""
from pysnmp.hlapi import *

#通过snmp获取服务器的相关参数，传入对应的oid,返回内容

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public', mpModel=1),
           UdpTransportTarget(('192.168.3.82', 161)),
           ContextData(),
           # ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0)),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))  #oid
           )
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for oid, val in varBinds:
        #输出返回的内容
        print(oid.prettyPrint()+'='+val.prettyPrint())

