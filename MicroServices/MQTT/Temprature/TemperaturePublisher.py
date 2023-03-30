import requests
import json
import time
import os
import sys
import asyncio
# /MicroServices/REST/Micros
sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final')
from MicroServices.MQTT.MyMQTT import *

# test.mosquitto.org
# broker.hivemq.com
# iot.eclipse.org


class CatalogApi:
    def __init__(self):
        conf = json.loads(open('./Microservices/MQTT/config.json').read())
        headers = {'Content-Type': 'application/json'}
        fullPath = conf["baseUrl"]+str(conf["port"])+'/device?' + \
            'userId='+conf["userId"]+'&deviceId='+conf["deviceId"]
        response = requests.get(fullPath, headers=headers).json()
        self.broker = response["servicesDetails"]["serviceIp"] #'test.mosquitto.org'
        self.port = 1883
        self.topic = response["servicesDetails"]["topic"][0]#'IoT/grp4/temperature'
    
    def getBroker(self):
        return self.broker
    
    def getPort(self):
        return self.port
    
    def getTopic(self):
        return self.topic


class TemperaturePublisher:
    def __init__(self, clientID, broker, port, topic):
        self.statusToBool = {"ON": True, "OFF": False}
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, None)
        self.__message = {"client": clientID,
                          'n': 'switch', "status": None, "timestamp": ''}

    def start(self):
        self.mqttClient.start()

    def stop(self):
        self.mqttClient.stop()

    def publish(self, value):
        message = self.__message
        message["status"] = value  # elf.statusToBool[value]
        message["timestamp"] = str(time.time())
        self.mqttClient.myPublish(self.topic, message)
        print(f'Published {message} to {self.topic}')


if __name__ == "__main__":
    api = CatalogApi()
    broker = api.getBroker()
    port = api.getPort()
    topic = api.getTopic()
    ledMngr = TemperaturePublisher ('TemperatureManager', broker, port, topic)
    ledMngr.mqttClient.start()
    time.sleep(2)
    print('Temperature Manager started')
    done = False
    a = 0
    while not done:
            a += 1
            ledMngr.publish(f'Temp Detail ${a}')
            time.sleep(1)

    # broker = 'test.mosquitto.org'
    # port = 1883
    # topic = 'IoT/grp4/temperature'