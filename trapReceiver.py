from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.proto.api import v2c
from pysnmp.entity.rfc3413 import ntfrcv
from Config import mrsConfig, snmpConfig
import logging
import socket, json

mrsHost = mrsConfig.mrsHost
mrsPort = mrsConfig.mrsPort

snmpEngine = engine.SnmpEngine()

trapAgentAddress = snmpConfig.trapAgentAddress
snmpTrapPort = snmpConfig.snmpTrapPort

logging.basicConfig(filename='received_traps.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)

logging.info("Agent is listening SNMP Trap on "+trapAgentAddress+" , Port : " +str(snmpTrapPort))
logging.info('--------------------------------------------------------------------------')

print("Agent is listening SNMP Trap on "+trapAgentAddress+" , Port : " +str(snmpTrapPort))

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
config.addV1System(snmpEngine, 'my-area', 'public') # SNMP v3로 날릴 때는 이 부분을 주석처리하고, SNMP v2는 주석을 개방하고 v3 유저정보를 삭제함


def changeDict2Bytes(msg):
    encode_data = json.dumps(msg, indent=2).encode('utf-8')
    return encode_data


def sendMsg(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((mrsHost, mrsPort))
    sock.send(msg)
    sock.close()


def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    print("Received new Trap message")
    logging.info("Received new Trap message")
    for name, val in varBinds:
        logging.info('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
        logging.info("==== End of Incoming Trap ====")


def run():
    ntfrcv.NotificationReceiver(snmpEngine, cbFun)
    snmpEngine.transportDispatcher.jobStarted(1)

    try:
        snmpEngine.transportDispatcher.runDispatcher()
    except Exception as e:
        snmpEngine.transportDispatcher.closeDispatcher()
        print(e)
        raise