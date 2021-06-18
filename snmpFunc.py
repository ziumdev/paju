from pysnmp.hlapi import *
from Config import mqttConfig, snmpConfig
import json, uuid, time
import modelInfo


def getSensorData(sensorList):
    data = {
        'to': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
        'fr': 'SiotTestAE',
        'rqi': str(uuid.uuid4()),
        'pc': {'m2m:cin': {'con': 0.0}},
        'op': 1,
        'ty': 4,
        'sec': 0
    }
    for sensor in sensorList:
        for dataObject in sensor['dataObject']:
            iterator = getCmd(SnmpEngine(), CommunityData('public'), UdpTransportTarget((snmpConfig.snmpHost, snmpConfig.snmpPort)), ContextData(),
                              ObjectType(ObjectIdentity(dataObject['objectId'])))
            errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
            if errorIndication:  # SNMP engine errors
                print(errorIndication)
            else:
                if errorStatus:  # SNMP agent errors
                    print(
                        '%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex) - 1] if errorIndex else '?'))
                else:
                    for varBind in varBinds:
                        try:
                            data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / dataObject['scale']
                            unit = dataObject['unit']
                            data['to'] += unit
                            sendData(mqttConfig.mqttTopic, json.loads(data), 0)
                            print(json.dumps(data))
                            data['to'] = data['to'][:-unit.__len__()]
                            print("success")
                        except ValueError as e:
                            print(e)
                            pass


def sendData(topic, payload, qos):
    mqttConfig.mqClient.publish(topic=topic, payload=str(payload), qos=qos)


def loop():
    while True:
        getSensorData(modelInfo.sensorList)
        # for list in snmpConfig.oidList:
        #     getData(list)
        time.sleep(snmpConfig.intveral)
