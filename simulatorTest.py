# from Config import mrsConfig
# import datetime, struct, json, socket
# import numpy
# 
# # mrsHost = mrsConfig.mrsHost
# # mrsPort = mrsConfig.mrsPort
# 
# mrsHost = 'localhost'
# mrsPort = 9201
# 
# 
# def sendMsg(msg):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect((mrsHost, mrsPort))
#     sock.send(msg)
#     sock.close()
# 
# 
# # 시간에 0추가 함수 case1
# def addZero(number):
#     result = ''
#     if 0 < number < 10:
#         result += '0'+str(number)
#         return result
#     else:
#         return str(number)
# 
# 
# # 시간에 0추가 함수 case2
# def addZeroMs(number):
#     num = int(number / 1000)
#     if str(num).__len__() < 3:
#         result = str(num).zfill(3)
#         return result
#     else:
#         return num
# 
# 
# today = datetime.datetime.now().today()
# currentDateTimeString = datetime.datetime.today().strftime('%Y%m%d%H%M%S%f')[:-3]
# headerA = mrsConfig.mrsClientCd + '     ' + mrsConfig.mrsSiteCd+'A1' + '      ' + mrsConfig.sendSystemCd + " "
# headerB = mrsConfig.headerTypeCd + mrsConfig.traceId + currentDateTimeString
# 
# bodyJson = {
#   "StatEvet":{
#     "uSvcOutbId" : "GST-ZIUM-000TAG002",
#     "statEvetId" : "SMT-PA1-000TAG004E01",
#     "statEvetNm" : "영상장치",
#     "statEvetGdCd" : "99",    # trap의 경보발생레벨의 값에 0를 붙일것.
#     "procSt" : "1", # 1이 아닌 다른 메시지로..
#     "outbPosCnt" : 0,
#     "outbPosNm" : "취사장 옆 자재 창고",
#     "statEvetCntn" : "일산화탄소 가스 농도 초과",
#     "statEvetOutbDtm" : currentDateTimeString,
#     "statEvetItemCnt" : 1,
#     "statEvetItem" : [{"key": "DATA",  "value": "co"}],
#     "cpxRelEvetOutbSeqnCnt" : 0
#   }
# }
# 
# # bodyJson['StatEvet']['outbPosNm'] = 'scold'
# # bodyJson['StatEvet']['statEvetGdCd'] = '가스탐지기A'
# # bodyJson['StatEvet']['statEvetClrDtm'] = currentDateTimeString
# 
# # bodyByte = marshal.dumps(bodyJson)
# bodyByte = json.dumps(bodyJson).encode('utf-8')  # Json 값을 byte로 변경
# 
# bodyLength = struct.pack('<I', bodyByte.__len__())
# print(bodyByte.__len__())
# print(bodyLength)
# # print(type(headerA), type(headerB), type(bodyLength))
# header = headerA.encode('utf-8').__add__(bodyLength).__add__(headerB.encode('utf-8'))
# 
# print(header)
# print(bodyByte)
# sendMsg(header+bodyByte)
# # sendMsg(bodyByte)
# 
# # headerArr : [66, 80, 65, 32, 32, 32, 32, 32, 80, 65, 49, 65, 49, 32, 32, 32, 32, 32, 32, 83, 73, 77, 32, -48, 1, 0, 0, 48, 48, 49, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 50, 48, 50, 49, 48, 53, 50, 49, 49, 52, 50, 49, 49, 56, 53, 51, 51]
# # mine :      [66, 80, 65, 32, 32, 32, 32, 32, 32, 80, 65, 49, 65, 49, 32, 32, 32, 32, 32, 32, 83, 73, 77, 32, 28, 2, 0, 0, 48, 48, 49, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 50, 48, 50, 49, 48, 53, 50, 49, 49, 52, 51, 49, 53, 55, 54, 49]
# 
# # headerTypeCdByte : 65, 49
# # headerTypeCdByte : 65, 49
# # mine : 49, 65
# 
# # headerTyeCd : A1
# # bodyLenArr : -48, 1, 0, 0
# # bodyLen : 464
# 
# #GST-ZIUM-000TAG002

import uuid

print(uuid.uuid4())
