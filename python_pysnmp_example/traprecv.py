import requests
from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.carrier.asyncore.dgram import udp, udp6, unix
from pyasn1.codec.ber import decoder
from pysnmp.proto import api

#启一个接收snmptrap服务

# noinspection PyUnusedLocal
def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),
        )
        print('\n===============================Notification message from %s:%s: ' % (
            transportDomain, transportAddress
        )
              )
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                print('Enterprise: %s' % (pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()))
                print('Agent Address: %s' % (pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()))
                print('Generic Trap: %s' % (pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()))
                print('Specific Trap: %s' % (pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()))
                print('Uptime: %s' % (pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()))
                varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
            else:
                varBinds = pMod.apiPDU.getVarBinds(reqPDU)
            print('==Var-binds:')
            # trap = {}
            #输出trap的oid以及对应的内容
            for oid, val in varBinds:
                print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))
            #     if oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.1.0':
            #         trap['vmwAlertAliveServerName']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.2.0':
            #         trap['vmwAlertEntityName']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.3.0':
            #         trap['vmwAlertEntityType']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.4.0':
            #         trap['vmwAlertTimestamp']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.5.0':
            #         trap['vmwAlertCriticality']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.6.0':
            #         trap['vmwAlertRootCause']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.7.0':
            #         trap['vmwAlertURL']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.8.0':
            #         trap['vmwAlertID']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.9.0':
            #         trap['vmwAlertMessage']=hex_to_string(val.prettyPrint()[2:])
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.10.0':
            #         trap['vmwAlertType']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.11.0':
            #         trap['vmwAlertSubtype']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.12.0':
            #         trap['vmwAlertHealth']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.13.0':
            #         trap['vmwAlertRisk']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.14.0':
            #         trap['vmwAlertEfficiency']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.15.0':
            #         trap['vmwAlertMetricName']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.16.0':
            #         trap['vmwAlertResourceKind']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.17.0':
            #         trap['vmwAlertDefinitionName']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.18.0':
            #         trap['vmwareAlertDefinitionDesc']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.19.0':
            #         trap['vmwAlertImpact']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.4.1.6876.4.50.1.2.20.0':
            #         trap['vmwAlertNotificationRules']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.2.1.1.3.0':
            #         trap['sysUpTimeInstance']=val.prettyPrint()
            #     elif oid.prettyPrint()=='1.3.6.1.6.3.1.1.4.1.0':
            #         trap['snmpTrapOID.0']=val.prettyPrint()
            # print(trap)
            # url = 'http://192.168.3.89:8000/vmware/receive_vmware_alarm/'
            # resp = requests.post(url,json=trap)
            # print(resp)
    return wholeMsg


transportDispatcher = AsyncoreDispatcher()

transportDispatcher.registerRecvCbFun(cbFun)

#接收服务器地址
transportDispatcher.registerTransport(
    udp.domainName, udp.UdpSocketTransport().openServerMode(('20.26.38.236', 162))
)

## Local domain socket
# transportDispatcher.registerTransport(
#    unix.domainName, unix.UnixSocketTransport().openServerMode('/tmp/snmp-manager')
# )

transportDispatcher.jobStarted(1)

try:
    # Dispatcher will never finish as job#1 never reaches zero
    transportDispatcher.runDispatcher()
except:
    transportDispatcher.closeDispatcher()
    raise
