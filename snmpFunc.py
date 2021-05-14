from pysnmp.hlapi import *
from Config import mqttConfig, snmpConfig
import json, uuid, time


def sendData(topic, payload, qos):
    mqttConfig.mqClient.publish(topic=topic, payload=json.dumps(payload), qos=qos)


def getData(oids):
    # sample data
    data = {
        'to': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
        'fr': 'SiotTestAE',
        'rqi': str(uuid.uuid4()),
        'pc': {"m2m:cin": {"con": 0.0}},
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
                if int(oid.split(snmpConfig.oidDefault)[1]) <= 4:
                    # print(int(oid.split(snmpConfig.oidDefault)[1]))
                    for varBind in varBinds:  # SNMP response contents
                        # data[str(varBind).split('=')[0]] = str(varBind).split('=')[1]
                        data['pc']['m2m:cin']['con'] = str(varBind).split('=')[1]
                        sendData(mqttConfig.mqttTopic, str(data), 0)
                        print(json.dumps(data))
                        # print("success")
                elif 9 <= int(oid.split(snmpConfig.oidDefault)[1]) <= 24:
                    # print(int(oid.split(snmpConfig.oidDefault)[1]))
                    for varBind in varBinds:  # SNMP response contents
                        try:
                            data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                            unit = 'ppm'
                            data['to'] += unit
                            sendData(mqttConfig.mqttTopic, str(data), 0)
                            print(json.dumps(data))
                            data['to'] = data['to'][:-unit.__len__()]
                            # print("success")
                        except ValueError as e:
                            print(e)
                            pass
                elif 25 <= int(oid.split(snmpConfig.oidDefault)[1]) <= 96:
                    # print(int(oid.split(snmpConfig.oidDefault)[1]))
                    if int(oid.split(snmpConfig.oidDefault)[1]) in snmpConfig.freqList:
                        for varBind in varBinds:  # SNMP response contents
                            try:
                                data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                                unit = 'Hz'
                                data['to'] += unit
                                sendData(mqttConfig.mqttTopic, str(data), 0)
                                print(json.dumps(data))
                                data['to'] = data['to'][:-unit.__len__()]
                                # print("success")
                            except ValueError as e:
                                print(e)
                                pass
                    elif int(oid.split(snmpConfig.oidDefault)[1]) in snmpConfig.voltageList:
                        for varBind in varBinds:  # SNMP response contents
                            try:
                                data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                                unit = 'Vac'
                                data['to'] += unit
                                sendData(mqttConfig.mqttTopic, str(data), 0)
                                print(json.dumps(data))
                                data['to'] = data['to'][:-unit.__len__()]
                                # print("success")
                            except ValueError as e:
                                print(e)
                                pass
                    elif int(oid.split(snmpConfig.oidDefault)[1]) in snmpConfig.currentList:
                        for varBind in varBinds:  # SNMP response contents
                            try:
                                data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                                unit = 'A'
                                data['to'] += unit
                                sendData(mqttConfig.mqttTopic, str(data), 0)
                                print(json.dumps(data))
                                data['to'] = data['to'][:-unit.__len__()]
                                # print("success")
                            except ValueError as e:
                                pass
                    elif int(oid.split(snmpConfig.oidDefault)[1]) in snmpConfig.pfList:
                        for varBind in varBinds:  # SNMP response contents
                            try:
                                data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                                unit = 'PF'
                                data['to'] += unit
                                sendData(mqttConfig.mqttTopic, str(data), 0)
                                print(json.dumps(data))
                                data['to'] = data['to'][:-unit.__len__()]
                                # print("success")
                            except ValueError as e:
                                print(e)
                                pass
                    elif int(oid.split(snmpConfig.oidDefault)[1]) in snmpConfig.pactList:
                        for varBind in varBinds:  # SNMP response contents
                            try:
                                data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                                unit = 'kW'
                                data['to'] += unit
                                sendData(mqttConfig.mqttTopic, str(data), 0)
                                print(json.dumps(data))
                                data['to'] = data['to'][:-unit.__len__()]
                                # print("success")
                            except ValueError as e:
                                print(e)
                                pass
                    elif int(oid.split(snmpConfig.oidDefault)[1]) in snmpConfig.preaList:
                        for varBind in varBinds:  # SNMP response contents
                            try:
                                data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                                unit = 'KVar'
                                data['to'] += unit
                                sendData(mqttConfig.mqttTopic, str(data), 0)
                                print(json.dumps(data))
                                data['to'] = data['to'][:-unit.__len__()]
                                # print("success")
                            except ValueError as e:
                                print(e)
                                pass
                    elif int(oid.split(snmpConfig.oidDefault)[1]) in snmpConfig.pactAmountList:
                        for varBind in varBinds:  # SNMP response contents
                            try:
                                data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                                unit = 'kWh'
                                data['to'] += unit
                                sendData(mqttConfig.mqttTopic, str(data), 0)
                                print(json.dumps(data))
                                data['to'] = data['to'][:-unit.__len__()]
                                # print("success")
                            except ValueError as e:
                                print(e)
                                pass
                    elif int(oid.split(snmpConfig.oidDefault)[1]) in snmpConfig.preaAmountList:
                        for varBind in varBinds:  # SNMP response contents
                            try:
                                data['pc']['m2m:cin']['con'] = float(str(varBind).split('=')[1]) / 100
                                unit = 'kVarh'
                                data['to'] += unit
                                sendData(mqttConfig.mqttTopic, str(data), 0)
                                print(json.dumps(data))
                                data['to'] = data['to'][:-unit.__len__()]
                                # print("success")
                            except ValueError as e:
                                print(e)
                                pass
    return 0


def loop():
    while True:
        for list in snmpConfig.oidList:
            getData(list)
        time.sleep(snmpConfig.intveral)
