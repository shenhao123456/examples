#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : sendtrap.py
@Author: sh
@Date  : 2019/1/24
@Desc  :
"""
from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.carrier.asyncore.dgram import udp, udp6
from pyasn1.codec.ber import encoder
from pysnmp.proto import api


#发送snmptrap
# Protocol version to use
# pMod = api.protoModules[api.protoVersion1]
#版本 2c
pMod = api.protoModules[api.protoVersion2c]

# Build PDU
trapPDU = pMod.TrapPDU()
pMod.apiTrapPDU.setDefaults(trapPDU)


# Traps have quite different semantics across proto versions
if pMod == api.protoModules[api.protoVersion1]:
    pMod.apiTrapPDU.setEnterprise(trapPDU, (1, 3, 6, 1, 1, 2, 3, 4, 1))
    pMod.apiTrapPDU.setGenericTrap(trapPDU, 'coldStart')
    # pMod.apiTrapPDU.setSpecificTrap(trapPDU, 'news')
else:
    #发送内容
    var = []
    oid1 = (1, 3, 6, 1, 4, 1, 2014516, 1, 1, 1, 2, 0)
    val1 = pMod.Integer(1)

    oid2 = (1, 3, 6, 1, 4, 1, 2014516, 1, 1, 1, 3, 0)
    val2 = pMod.OctetString('11111111111')
    var.append((oid1, val1))
    var.append((oid2, val2))

    pMod.apiTrapPDU.setVarBinds(trapPDU,var)
# Build message
trapMsg = pMod.Message()
pMod.apiMessage.setDefaults(trapMsg)
pMod.apiMessage.setCommunity(trapMsg, 'public')
pMod.apiMessage.setPDU(trapMsg, trapPDU)

transportDispatcher = AsyncoreDispatcher()

# UDP/IPv4
transportDispatcher.registerTransport(
    udp.domainName, udp.UdpSocketTransport().openClientMode()
)
#发送服务器地址
transportDispatcher.sendMessage(
    encoder.encode(trapMsg), udp.domainName, ('192.168.3.185', 162)
)

# # UDP/IPv6
# transportDispatcher.registerTransport(
#     udp6.domainName, udp6.Udp6SocketTransport().openClientMode()
# )
# transportDispatcher.sendMessage(
#     encoder.encode(trapMsg), udp6.domainName, ('::1', 162)
# )

# Dispatcher will finish as all scheduled messages are sent
transportDispatcher.runDispatcher()

transportDispatcher.closeDispatcher()
