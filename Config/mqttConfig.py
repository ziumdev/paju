import paho.mqtt.client as mqtt

brkIp = '127.0.0.1'
brkPort = 1883
brkKeepalive = 60

mqttTopic = '/oneM2M/req/SiotTestAE/iotCore'

mqClient=mqtt.Client()
mqClient.max_inflight_messages_set(inflight=20)
mqClient.message_retry_set(retry=5)
try:
    mqClient.connect(host=brkIp, port=brkPort, keepalive=brkKeepalive, bind_address="")
    # mqClient.reconnect()
except ConnectionError as e:
    print(e)
    print("cannot connect with MQTT server")