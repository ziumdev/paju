snmpHost = '127.0.0.1'
snmpPort = 161


gasSensorA_Id = ''
gasSensorB_Id = ''
gasSensorC_Id = ''
gasSensorD_Id = ''
multimeter_A_Id = ''
multimeter_B_Id = ''
multimeter_C_Id = ''
multimeter_D_Id = ''

tagCO = {
    'ID' : '',
    'scale': 100,
    
}

# 아래부분은 수정 불필요
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

oidList = [flameSensorOidList, gasSensorOidList, multimeter_A_oidList, multimeter_B_oidList, multimeter_C_oidList, multimeter_D_oidList]

freqList = [25, 43, 61, 79]
voltageList = [26, 27, 29, 29, 30, 31,
               44, 45, 46, 47, 48, 49,
               62, 63, 64, 65, 66, 67,
               80, 81, 82, 83, 84, 85
               ]
currentList = [32, 33, 34,
               50, 51, 52,
               68, 69, 70,
               86, 87, 88
               ]
pfList = [35, 36, 37,
          53, 54, 55,
          71, 72, 73,
          89, 90, 91
          ]
pactList = [38, 56, 75, 92]  # 유효전력
preaList = [39, 57, 76, 93]  # 무효전력
pactAmountList = [40, 58, 77, 94]  # 유효전력량
preaAmountList = [41, 59, 78, 95]  # 무효전력량


intveral = 5

trapAgentAddress = '0.0.0.0'
snmpTrapPort = 9162

#SNMPv3/USM setup

# userInfo = {
#     'username': 'tester',
#     'authProtocol': 'authkey1',
#     'privProtocol': 'privkey1',
#     'OctetValue': '0x0102030405'
# }


