import json
import time
import sys
import os
"""
    -------------------------------------------- Notice --------------------------------------------
    #path to parent folder
    # there is a difference between os.getcwd() in Mac Terminal and VSCode
    # VSCode returns the path to project root folder, while Mac Terminal returns the path to the current folder
"""
currentPath = os.getcwd()[:os.getcwd().find('/Final')+len('/Final')]+os.path.sep
sys.path.insert(1, currentPath)
from MicroServices.MQTT.MyMQTT import *

class SensorsSubscriber:
    def __init__(self,clientID, broker, port, topic):
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, self)

    def notify(self, topic, payload): #use senML
        self.status = json.loads(payload)["status"] 
        print( f'sensor ${topic}: ${payload} recieved') 

    def start(self):
        self.mqttClient.start()
        self.mqttClient.mySubscribe(self. topic)
        
    def stop(self):
        self.mqttClient.stop()

    def saveTemperture(self, value):
        pass

    def saveHumidity(self, value):
        pass

if __name__ == "__main__":
    led = SensorsSubscriber ('grp4_mqtt_iot_123456', 'test.mosquitto.org', 1883, 'IoT/grp4/+')
    led.start()
    while True:
        time.sleep(1)