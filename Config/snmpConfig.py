snmpHost = '127.0.0.1'
snmpPort = 161

oidDefault = "1.3.6.1.4.1.30960.2.1.5.1.1.9."

flameSensorList = []
gasSensorList = []
multimeter_A_sensorList = []
multimeter_B_sensorList = []
multimeter_C_sensorList = []
multimeter_D_sensorList = []


def makeOidList(listName, startNo, endNo):
    for i in range(startNo, endNo + 1):
        listName.append(oidDefault+str(i))
    return listName


flameSensorOidList = makeOidList(flameSensorList, 1, 4)
gasSensorOidList = makeOidList(gasSensorList, 9, 24)
multimeter_A_oidList = makeOidList(multimeter_A_sensorList, 25, 42)
multimeter_B_oidList = makeOidList(multimeter_B_sensorList, 43, 60)
multimeter_C_oidList = makeOidList(multimeter_C_sensorList, 61, 78)
multimeter_D_oidList = makeOidList(multimeter_D_sensorList, 79, 96)

intveral = 5

trapAgentAddress='127.0.0.1'
snmpTrapPort=50003

#SNMPv3/USM setup

userInfo = {
    'username': 'tester',
    'authProtocol': 'authkey1',
    'privProtocol': 'privkey1',
    'OctetValue': '0x0102030405'
}

oidList = [flameSensorOidList, gasSensorOidList, multimeter_A_oidList, multimeter_B_oidList, multimeter_C_oidList, multimeter_D_oidList]