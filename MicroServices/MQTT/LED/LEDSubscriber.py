from MyMQTT import *
import json
import time

class LEDManager:
    def __init__(self,clientID, broker, port, topic):
        self.status = 'OFF'
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, self)

    def notify(self, topic, payload): #use senML
        self.status = json.loads(payload)["status"] 
        print( f'led status: ', self.status) 

    def start(self):
        self.mqttClient.start()
        self.mqttClient.mySubscribe(self. topic)
        

if __name__ == "__main__":
    led = LEDManager ('grp4_mqtt_iot_123456', 'test.mosquitto.org', 1883, 'IoT/grp4/led')
    led.start()
    while True:
        time.sleep(10)