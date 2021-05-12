snmpHost = '127.0.0.1'
snmpPort = 161
oidList = ["1.3.6.1.4.1.30960.2.1.5.1.1.9.1", "1.3.6.1.4.1.30960.2.1.5.1.1.9.2", "1.3.6.1.4.1.30960.2.1.5.1.1.9.3",
           "1.3.6.1.4.1.30960.2.1.5.1.1.9.4", "1.3.6.1.4.1.30960.2.1.5.1.1.9.5", "1.3.6.1.4.1.30960.2.1.5.1.1.9.6"]

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