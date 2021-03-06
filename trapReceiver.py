# -*- coding: utf-8 -*-

from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from Config import mrsConfig, snmpConfig
import logging
import socket, json, datetime, struct

mrsHost = mrsConfig.ersHost
mrsPort = mrsConfig.ersPort

snmpEngine = engine.SnmpEngine()

trapAgentAddress = snmpConfig.trapAgentAddress
snmpTrapPort = snmpConfig.snmpTrapPort

logging.basicConfig(filename='received_traps.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)

logging.info("Agent is listening SNMP Trap on " + trapAgentAddress + " , Port : " + str(snmpTrapPort))
logging.info('--------------------------------------------------------------------------')

eventCnt = 0
global trapFlag

print("Agent is listening SNMP Trap on " + trapAgentAddress + " , Port : " + str(snmpTrapPort))

config.addTransport(
    snmpEngine,
    udp.domainName + (1,),
    udp.UdpTransport().openServerMode((trapAgentAddress, snmpTrapPort))
)

# config.addV3User(
#     snmpEngine, snmpConfig.userInfo['username'],
#     config.usmHMACMD5AuthProtocol, snmpConfig.userInfo['authProtocol'],
#     config.usmDESPrivProtocol,  snmpConfig.userInfo['privProtocol'],
#     securityEngineId=v2c.OctetString(value=snmpConfig.userInfo['OctetValue'])
# )

config.addV1System(snmpEngine, 'my-area', 'public')  # SNMP v3로 날릴 때는 이 부분을 주석처리하고, SNMP v2는 주석을 개방하고 v3 유저정보를 삭제함


def changeDict2Bytes(msg):
    encode_data = json.dumps(msg, indent=2).encode('utf-8')
    return encode_data

def sendMsg(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((mrsHost, mrsPort))
    sock.send(msg)
    sock.close()


# 시간에 0추가 함수 case1
def addZero(number):
    result = ''
    if 0 < number < 10:
        result += '0' + str(number)
        return result
    else:
        return str(number)


# 시간에 0추가 함수 case2
def addZeroMs(number):
    num = int(number / 1000)
    if str(num).__len__() < 3:
        result = str(num).zfill(3)
        return result
    else:
        return num


def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    global eventCnt
    trapFlag = False
    bodyJson = mrsConfig.bodyJson
    uSvcOutbId = mrsConfig.mrsClientCd + '-' + mrsConfig.mrsSiteCd + '-' + mrsConfig.headerTypeCd + 'TAG' + str(
        eventCnt).zfill(3)
    statEvetId = uSvcOutbId + 'E01'
    statEvetNm = ''
    dataKey = None
    dataValue = None
    statEvetGdCd = '0'
    statEvetOutbDtm = ''
    alarmPonit = '0'
    rate = 1
    for name, val in varBinds:
        if name.prettyPrint() == mrsConfig.trapOidList['alarmOccurs']:
            if val.prettyPrint() != '1':
                trapFlag = False
                # bodyJson = None
                break
            else:
                print("Received new Trap message")
                logging.info("Received new Trap message")
                trapFlag = True
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmNum']:
            pass
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmLevel']:
            statEvetGdCd = val.prettyPrint()
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmVal']:
            dataValue = val.prettyPrint()
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmChar']:
            pass
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmCpoint']:
            alarmPonit = val.prettyPrint()
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmAbove']:
            pass
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmTime']:
            statEvetOutbDtm = val.prettyPrint()
            pass
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmUnit']:
            dataKey = val.prettyPrint()
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmDesc']:
            byte_array = bytearray.fromhex(val.prettyPrint()[2:])
            statEvetNm = byte_array.decode()
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmValDesc']:
            pass
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmRate']:
            rate = val.prettyPrint()
            pass
        elif name.prettyPrint() == mrsConfig.trapOidList['alarmMeasureFormat']:
            pass
        statEvetItem = [{'key': dataKey, 'value': dataValue}]
        bodyJson["StatEvet"]["uSvcOutbId"] = uSvcOutbId
        bodyJson["StatEvet"]["statEvetId"] = statEvetId
        bodyJson["StatEvet"]["statEvetNm"] = statEvetNm
        bodyJson["StatEvet"]["statEvetGdCd"] = statEvetGdCd.zfill(2)
        bodyJson["StatEvet"]["procSt"] = 1
        bodyJson["StatEvet"]["outbPosCnt"] = 0
        bodyJson["StatEvet"]["outbPosNm"] = statEvetNm
        bodyJson["StatEvet"]["statEvetCntn"] = str(statEvetNm) + str(float(alarmPonit) / float(rate)) + str(
            dataKey) + '초과'
        bodyJson["StatEvet"]["statEvetOutbDtm"] = statEvetOutbDtm
        bodyJson["StatEvet"]["statEvetItemCnt"] = 1
        bodyJson["StatEvet"]["statEvetItem"] = statEvetItem
        bodyJson["StatEvet"]["cpxRelEvetOutbSeqnCnt"] = 0

    logging.info("==== End of Incoming Trap ====")
    if trapFlag:
        # print(bodyJson["StatEvet"]["statEvetNm"])
        # print(bodyJson)
        print(json.dumps(bodyJson, ensure_ascii=False))
        sendToErs(bodyJson)
        eventCnt += 1
        trapFlag = False


def sendToErs(jsonData):
    currentDateTimeString = datetime.datetime.today().strftime('%Y%m%d%H%M%S%f')[:-3]
    headerA = mrsConfig.mrsClientCd + '     ' + mrsConfig.mrsSiteCd + 'A1' + '      ' + mrsConfig.sendSystemCd + " "
    headerB = mrsConfig.headerTypeCd + mrsConfig.traceId + currentDateTimeString
    # jsonData = mrsConfig.bodyJson
    # jsonData['StatEvet']['outbPosNm'] = 'scold'
    # jsonData['StatEvet']['statEvetGdCd'] = '가스탐지기A'
    jsonData['StatEvet']['statEvetOutbDtm'] = currentDateTimeString

    bodyByte = json.dumps(jsonData, ensure_ascii=False).encode('utf-8')  # Json 값을 byte로 변경
    # bodyByte = marshal.dumps(bodyJson)
    bodyLength = struct.pack('<I', bodyByte.__len__())
    header = headerA.encode('utf-8').__add__(bodyLength).__add__(headerB.encode('utf-8'))
    msg = header + bodyByte
    sendMsg(msg.decode())


def run():
    ntfrcv.NotificationReceiver(snmpEngine, cbFun)
    snmpEngine.transportDispatcher.jobStarted(1)

    try:
        snmpEngine.transportDispatcher.runDispatcher()
    except Exception as e:
        snmpEngine.transportDispatcher.closeDispatcher()
        print(e)
        raise

