import requests
import json
import time
import os
import sys
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
        fullPath = conf["baseUrl"]+str(conf["rest_port"])+'/device?' + 'userId='+conf["userId"]+'&deviceId='+conf["temp_deviceId"]
        response = requests.get(fullPath, headers=headers).json()
        self.broker = response["servicesDetails"]["serviceIp"]
        self.port = 1883
        self.topic = response["servicesDetails"]["topic"][0]
    
    def getBroker(self):
        return self.broker
    
    def getPort(self):
        return self.port
    
    def getTopic(self):
        return self.topic


#--------------------------------------------MQTT------------------------------------------------
class TemperaturePublisher:
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
    ledMngr = TemperaturePublisher ('TemperaturePublisher', broker, port, topic)
    ledMngr.mqttClient.start()
    time.sleep(2)
    print('Temperature Publisher started')
    done = False
    a = 0
    while not done:
            a += 1
            ledMngr.publish(f'Temp Detail ${a}')
            time.sleep(1)