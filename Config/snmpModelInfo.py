oidDefault = "1.3.6.1.4.1.30960.2.1.5.1.1.9."
# 화재센서
fireSensorA = {
    'deviceId': 1,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'IS_FSS',
    'deviceDescription' : '화재센서_급양관',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '연기감지',
            'objectId': oidDefault + '1',
            'scale': 1,
            'unit': ''
        }
    ]
}
fireSensorB = {
    'deviceId': 2,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'IS_FSS',
    'deviceDescription' : '화재센서_탄약고',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '연기감지',
            'objectId': oidDefault + '2',
            'scale': 1,
            'unit': ''
        }
    ]
}
fireSensorC = {
    'deviceId': 3,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'IS_FSH',
    'deviceDescription': '화재센서_생활관',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '열감지',
            'objectId': oidDefault + '3',
            'scale': 1,
            'unit': ''
        }
    ]
}
fireSensorD = {
    'deviceId': 4,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'IS_FSH',
    'deviceDescription': '화재센서_유류고',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '열감지',
            'objectId': oidDefault + '4',
            'scale': 1,
            'unit': ''
        }
    ]
}

# Gas Sensor
gasSensorA = {
    'deviceId': 1,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'GAS-DUMMY',
    'deviceDescription': '가스센서_A',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '가연성가스',
            'objectId': oidDefault + '9',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 2,
            'dataDescription': '일산화탄소',
            'objectId': oidDefault + '10',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 3,
            'dataDescription': '산소',
            'objectId': oidDefault + '11',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 4,
            'dataDescription': '황화수소',
            'objectId': oidDefault + '12',
            'scale': 100,
            'unit': 'ppm'
        },
    ]
}
gasSensorB = {
    'deviceId': 2,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'GAS-DUMMY',
    'deviceDescription': '가스센서_B',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '가연성가스',
            'objectId': oidDefault + '13',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 2,
            'dataDescription': '일산화탄소',
            'objectId': oidDefault + '14',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 3,
            'dataDescription': '산소',
            'objectId': oidDefault + '15',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 4,
            'dataDescription': '황화수소',
            'objectId': oidDefault + '16',
            'scale': 100,
            'unit': 'ppm'
        },
    ]
}
gasSensorC = {
    'deviceId': 3,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'GAS-DUMMY',
    'deviceDescription': '가스센서_C',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '가연성가스',
            'objectId': oidDefault + '17',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 2,
            'dataDescription': '일산화탄소',
            'objectId': oidDefault + '18',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 3,
            'dataDescription': '산소',
            'objectId': oidDefault + '19',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 4,
            'dataDescription': '황화수소',
            'objectId': oidDefault + '20',
            'scale': 100,
            'unit': 'ppm'
        },
    ]
}
gasSensorD = {
    'deviceId': 4,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'GAS-DUMMY',
    'deviceDescription': '가스센서_D',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '가연성가스',
            'objectId': oidDefault + '21',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 2,
            'dataDescription': '일산화탄소',
            'objectId': oidDefault + '22',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 3,
            'dataDescription': '산소',
            'objectId': oidDefault + '23',
            'scale': 100,
            'unit': 'ppm'
        },
        {
            'dataId': 4,
            'dataDescription': '황화수소',
            'objectId': oidDefault + '24',
            'scale': 100,
            'unit': 'ppm'
        },
    ]
}

# 멀티미터
multimeterA = {
    'deviceId': 1,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'MM-DUMMY',
    'deviceDescription': '멀티미터_A',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '주파수',
            'objectId': oidDefault + '25',
            'scale': 100,
            'unit': 'Hz'
        },
        {
            'dataId': 2,
            'dataDescription': '전압(RS)',
            'objectId': oidDefault + '26',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 3,
            'dataDescription': '전압(ST)',
            'objectId': oidDefault + '27',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 4,
            'dataDescription': '전압(TR)',
            'objectId': oidDefault + '28',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 5,
            'dataDescription': '전압(R)',
            'objectId': oidDefault + '29',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 6,
            'dataDescription': '전압(S)',
            'objectId': oidDefault + '30',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 7,
            'dataDescription': '전압(T)',
            'objectId': oidDefault + '31',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 8,
            'dataDescription': '전류(R)',
            'objectId': oidDefault + '32',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 9,
            'dataDescription': '전류(S)',
            'objectId': oidDefault + '33',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 10,
            'dataDescription': '전류(T)',
            'objectId': oidDefault + '34',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 11,
            'dataDescription': '역률(R)',
            'objectId': oidDefault + '35',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 12,
            'dataDescription': '역률(S)',
            'objectId': oidDefault + '36',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 13,
            'dataDescription': '역률(T)',
            'objectId': oidDefault + '37',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 14,
            'dataDescription': '유효전력',
            'objectId': oidDefault + '38',
            'scale': 100,
            'unit': 'kW'
        },
        {
            'dataId': 15,
            'dataDescription': '무효전력',
            'objectId': oidDefault + '39',
            'scale': 100,
            'unit': 'kVar'
        },
        {
            'dataId': 16,
            'dataDescription': '유효전력량',
            'objectId': oidDefault + '40',
            'scale': 100,
            'unit': 'kWh'
        },
        {
            'dataId': 17,
            'dataDescription': '무효전력량',
            'objectId': oidDefault + '41',
            'scale': 100,
            'unit': 'kVarh'
        },
        {
            'dataId': 18,
            'dataDescription': '경보',
            'objectId': oidDefault + '42',
            'scale': 1,
            'unit': ''
        },
    ]
}
multimeterB = {
    'deviceId': 2,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'MM-DUMMY',
    'deviceDescription': '멀티미터_B',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '주파수',
            'objectId': oidDefault + '43',
            'scale': 100,
            'unit': 'Hz'
        },
        {
            'dataId': 2,
            'dataDescription': '전압(RS)',
            'objectId': oidDefault + '44',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 3,
            'dataDescription': '전압(ST)',
            'objectId': oidDefault + '45',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 4,
            'dataDescription': '전압(TR)',
            'objectId': oidDefault + '46',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 5,
            'dataDescription': '전압(R)',
            'objectId': oidDefault + '47',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 6,
            'dataDescription': '전압(S)',
            'objectId': oidDefault + '48',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 7,
            'dataDescription': '전압(T)',
            'objectId': oidDefault + '49',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 8,
            'dataDescription': '전류(R)',
            'objectId': oidDefault + '50',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 9,
            'dataDescription': '전류(S)',
            'objectId': oidDefault + '51',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 10,
            'dataDescription': '전류(T)',
            'objectId': oidDefault + '52',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 11,
            'dataDescription': '역률(R)',
            'objectId': oidDefault + '53',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 12,
            'dataDescription': '역률(S)',
            'objectId': oidDefault + '54',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 13,
            'dataDescription': '역률(T)',
            'objectId': oidDefault + '55',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 14,
            'dataDescription': '유효전력',
            'objectId': oidDefault + '56',
            'scale': 100,
            'unit': 'kW'
        },
        {
            'dataId': 15,
            'dataDescription': '무효전력',
            'objectId': oidDefault + '57',
            'scale': 100,
            'unit': 'kVar'
        },
        {
            'dataId': 16,
            'dataDescription': '유효전력량',
            'objectId': oidDefault + '58',
            'scale': 100,
            'unit': 'kWh'
        },
        {
            'dataId': 17,
            'dataDescription': '무효전력량',
            'objectId': oidDefault + '59',
            'scale': 100,
            'unit': 'kVarh'
        },
        {
            'dataId': 18,
            'dataDescription': '경보',
            'objectId': oidDefault + '60',
            'scale': 1,
            'unit': ''
        },
    ]
}
multimeterC = {
    'deviceId': 3,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'MM-DUMMY',
    'deviceDescription': '멀티미터_C',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '주파수',
            'objectId': oidDefault + '61',
            'scale': 100,
            'unit': 'Hz'
        },
        {
            'dataId': 2,
            'dataDescription': '전압(RS)',
            'objectId': oidDefault + '62',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 3,
            'dataDescription': '전압(ST)',
            'objectId': oidDefault + '63',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 4,
            'dataDescription': '전압(TR)',
            'objectId': oidDefault + '64',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 5,
            'dataDescription': '전압(R)',
            'objectId': oidDefault + '65',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 6,
            'dataDescription': '전압(S)',
            'objectId': oidDefault + '66',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 7,
            'dataDescription': '전압(T)',
            'objectId': oidDefault + '67',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 8,
            'dataDescription': '전류(R)',
            'objectId': oidDefault + '68',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 9,
            'dataDescription': '전류(S)',
            'objectId': oidDefault + '69',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 10,
            'dataDescription': '전류(T)',
            'objectId': oidDefault + '70',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 11,
            'dataDescription': '역률(R)',
            'objectId': oidDefault + '71',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 12,
            'dataDescription': '역률(S)',
            'objectId': oidDefault + '72',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 13,
            'dataDescription': '역률(T)',
            'objectId': oidDefault + '73',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 14,
            'dataDescription': '유효전력',
            'objectId': oidDefault + '74',
            'scale': 100,
            'unit': 'kW'
        },
        {
            'dataId': 15,
            'dataDescription': '무효전력',
            'objectId': oidDefault + '75',
            'scale': 100,
            'unit': 'kVar'
        },
        {
            'dataId': 16,
            'dataDescription': '유효전력량',
            'objectId': oidDefault + '76',
            'scale': 100,
            'unit': 'kWh'
        },
        {
            'dataId': 17,
            'dataDescription': '무효전력량',
            'objectId': oidDefault + '77',
            'scale': 100,
            'unit': 'kVarh'
        },
        {
            'dataId': 18,
            'dataDescription': '경보',
            'objectId': oidDefault + '78',
            'scale': 1,
            'unit': ''
        },
    ]
}
multimeterD = {
    'deviceId': 4,
    'deviceEndPointURI': '/iotCore/AEe2c8236c-7d26-48d2-9cc7-29e79129c811/',
    'modelName': 'MM-DUMMY',
    'deviceDescription': '멀티미터_D',
    'dataObject': [
        {
            'dataId': 1,
            'dataDescription': '주파수',
            'objectId': oidDefault + '79',
            'scale': 100,
            'unit': 'Hz'
        },
        {
            'dataId': 2,
            'dataDescription': '전압(RS)',
            'objectId': oidDefault + '80',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 3,
            'dataDescription': '전압(ST)',
            'objectId': oidDefault + '81',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 4,
            'dataDescription': '전압(TR)',
            'objectId': oidDefault + '82',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 5,
            'dataDescription': '전압(R)',
            'objectId': oidDefault + '83',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 6,
            'dataDescription': '전압(S)',
            'objectId': oidDefault + '84',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 7,
            'dataDescription': '전압(T)',
            'objectId': oidDefault + '85',
            'scale': 100,
            'unit': 'Vac'
        },
        {
            'dataId': 8,
            'dataDescription': '전류(R)',
            'objectId': oidDefault + '86',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 9,
            'dataDescription': '전류(S)',
            'objectId': oidDefault + '87',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 10,
            'dataDescription': '전류(T)',
            'objectId': oidDefault + '88',
            'scale': 100,
            'unit': 'A'
        },
        {
            'dataId': 11,
            'dataDescription': '역률(R)',
            'objectId': oidDefault + '89',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 12,
            'dataDescription': '역률(S)',
            'objectId': oidDefault + '90',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 13,
            'dataDescription': '역률(T)',
            'objectId': oidDefault + '91',
            'scale': 100,
            'unit': 'PF'
        },
        {
            'dataId': 14,
            'dataDescription': '유효전력',
            'objectId': oidDefault + '92',
            'scale': 100,
            'unit': 'kW'
        },
        {
            'dataId': 15,
            'dataDescription': '무효전력',
            'objectId': oidDefault + '93',
            'scale': 100,
            'unit': 'kVar'
        },
        {
            'dataId': 16,
            'dataDescription': '유효전력량',
            'objectId': oidDefault + '94',
            'scale': 100,
            'unit': 'kWh'
        },
        {
            'dataId': 17,
            'dataDescription': '무효전력량',
            'objectId': oidDefault + '95',
            'scale': 100,
            'unit': 'kVarh'
        },
        {
            'dataId': 18,
            'dataDescription': '경보',
            'objectId': oidDefault + '96',
            'scale': 1,
            'unit': ''
        },
    ]
}

sensorList = [
    fireSensorA, fireSensorB, fireSensorC, fireSensorD,
    gasSensorA, gasSensorB, gasSensorC, gasSensorD,
    multimeterA, multimeterB, multimeterC, multimeterD
]
