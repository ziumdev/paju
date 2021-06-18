from pysnmp.hlapi import *
from Config import mqttConfig, snmpConfig, snmpModelInfo
import json, uuid, time


def getSensorData(sensorList):
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
                            sensorData = snmpConfig.data
                            sensorData['rqi'] = str(uuid.uuid4())
                            sensorData['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / dataObject['scale']
                            unit = dataObject['unit']
                            sensorData['to'] += unit
                            sendData(mqttConfig.mqttTopic, json.loads(sensorData), 0)
                            print(json.dumps(sensorData))
                            print("success")
                        except ValueError as e:
                            print(e)
                            pass


def sendData(topic, payload, qos):
    mqttConfig.mqClient.publish(topic=topic, payload=str(payload), qos=qos)


def loop():
    while True:
        getSensorData(snmpModelInfo.sensorList)
        time.sleep(snmpConfig.intveral)
