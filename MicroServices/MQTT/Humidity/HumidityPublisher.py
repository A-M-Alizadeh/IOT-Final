import requests
import json
import time
import os
import sys

sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final')
from MicroServices.MQTT.MyMQTT import *

#--------------------------------------------REST API------------------------------------------------
class CatalogApi:
    def __init__(self):
        conf = json.loads(open('./Microservices/MQTT/config.json').read())
        headers = {'Content-Type': 'application/json'}
        fullPath = conf["baseUrl"]+str(conf["rest_port"])+'/device?'+'&deviceId='+conf["humid_deviceId"] # + 'userId='+conf["userId"]
        response = requests.get(fullPath, headers=headers).json()
        self.broker = response["servicesDetails"]["serviceIp"] #'test.mosquitto.org'
        self.port = 1883
        self.topic = response["servicesDetails"]["topic"][0] #'IoT/grp4/temperature'
    
    def getBroker(self):
        return self.broker
    
    def getPort(self):
        return self.port
    
    def getTopic(self):
        return self.topic


#--------------------------------------------MQTT------------------------------------------------
class HumidityPublisher:
    def __init__(self, clientID, broker, port, topic):
        self.statusToBool = {"ON": True, "OFF": False}
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, None)
        self.__message = {"client": clientID,'n': 'switch', "status": None, "timestamp": ''}

    def start(self):
        self.mqttClient.start()

    def stop(self):
        self.mqttClient.stop()

    def publish(self, value):
        message = self.__message
        message["status"] = value  # self.statusToBool[value]
        message["timestamp"] = str(time.time())
        self.mqttClient.myPublish(self.topic, message)
        print(f'Published {message} to {self.topic}')



#--------------------------------------------MAIN------------------------------------------------
if __name__ == "__main__":
    api = CatalogApi()
    broker = api.getBroker()
    port = api.getPort()
    topic = api.getTopic()
    ledMngr = HumidityPublisher ('HumidityManager', broker, port, topic)
    ledMngr.mqttClient.start()
    time.sleep(2)
    print('Humidity Manager started')
    done = False
    a = 0
    while not done:
            a += 1
            ledMngr.publish(f'Temp Detail ${a}')
            time.sleep(1)