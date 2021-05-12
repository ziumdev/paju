from pysnmp.hlapi import *
from Config import mqttConfig, snmpConfig
import json, uuid, time


def sendData(topic, payload, qos):
    mqttConfig.mqClient.publish(topic=topic, payload=json.dumps(payload), qos=qos)


def getData(oids):
    # sample data
    data = {
        'to': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/vm',
        'fr': 'SiotTestAE',
        'rqi': str(uuid.uuid4()),
        'pc': {"m2m:cin": {"con": 0}},
        'op': 1,
        'ty': 4,
        'sec': 0
    }

    for oid in oids:
        iterator = getCmd(SnmpEngine(), CommunityData('test'), UdpTransportTarget((snmpConfig.snmpHost, snmpConfig.snmpPort)), ContextData(),
                          ObjectType(ObjectIdentity(oid)))
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:  # SNMP engine errors
            print(errorIndication)
        else:
            if errorStatus:  # SNMP agent errors
                print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
            else:
                for varBind in varBinds:  # SNMP response contents
                    # data[str(varBind).split('=')[0]] = str(varBind).split('=')[1]
                    data['pc']['m2m:cin']['con'] = str(varBind).split('=')[1]
                    sendData(mqttConfig.mqttTopic, str(data), 0)
                    print(json.dumps(data))
                    # print("success")
    return 0


def loop():
    while True:
        getData(snmpConfig.oidList)
        time.sleep(snmpConfig.intveral)
