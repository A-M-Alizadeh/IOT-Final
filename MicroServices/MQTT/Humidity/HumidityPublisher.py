import requests
import json
import time
import os
import sys
import random
"""
    -------------------------------------------- Notice --------------------------------------------
    #path to parent folder
    # there is a difference between os.getcwd() in Mac Terminal and VSCode
    # VSCode returns the path to project root folder, while Mac Terminal returns the path to the current folder
"""
currentPath = os.getcwd()[:os.getcwd().find('/Final')+len('/Final')]+os.path.sep
sys.path.insert(1, currentPath)
from MicroServices.MQTT.MyMQTT import *

#--------------------------------------------REST API------------------------------------------------
class CatalogApi:
    def __init__(self):
        conf = json.loads(open(currentPath+'Microservices/MQTT/config.json').read())
        headers = {'Content-Type': 'application/json'}
        fullPath = conf["baseUrl"]+str(conf["rest_port"])+'/device?'+'&deviceId='+conf["humid_deviceId"] # + 'userId='+conf["userId"]
        response = requests.get(fullPath, headers=headers).json()
        self.broker = response["servicesDetails"]["serviceIp"] #'test.mosquitto.org'
        self.port = 1883
        self.topic = response["servicesDetails"]["topic"][0] #'IoT/grp4/temperature'
        self.clientId = response["deviceId"]+'-'+response["measureType"][0]
    
    def getBroker(self):
        return self.broker
    
    def getPort(self):
        return self.port
    
    def getTopic(self):
        return self.topic
    
    def getClientId(self):
        return self.clientId


#--------------------------------------------MQTT------------------------------------------------
class HumidityPublisher:
    def __init__(self, clientID, broker, port, topic):
        self.statusToBool = {"ON": True, "OFF": False}
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, None)
        self.__message = {"bn":clientID, "t": None,  "bu":"%RH", "n":"temp", "v":None}

    def start(self):
        self.mqttClient.start()

    def stop(self):
        self.mqttClient.stop()

    def randomValueGenerator(self):
        return round(random.uniform(20.0,40.0), 1)

    def publish(self):
        message = self.__message
        message["v"] = self.randomValueGenerator()
        message["t"] = str(time.time())
        self.mqttClient.myPublish(self.topic, message)
        print(f'Published {message} to {self.topic}')



#--------------------------------------------MAIN------------------------------------------------
if __name__ == "__main__":
    api = CatalogApi()
    broker = api.getBroker()
    port = api.getPort()
    topic = api.getTopic()
    clientId = api.getClientId()
    ledMngr = HumidityPublisher (clientId, broker, port, topic)
    ledMngr.mqttClient.start()
    time.sleep(2)
    print('Humidity Publisher started')
    while True:
            ledMngr.publish()
            time.sleep(10)