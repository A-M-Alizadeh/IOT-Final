import requests
import json
import time
import os
import sys
import random
import requests
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
class TemperaturePublisher:
    def __init__(self, clientID, broker, port, topic):
        self.statusToBool = {"ON": True, "OFF": False}
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, None)
        self.__message = {"bn":clientID, "t": None,  "u":"Cel", "n":"temp", "v":None}

    def start(self):
        self.mqttClient.start()

    def stop(self):
        self.mqttClient.stop()

    def randomValueGenerator(self):
        return round(random.uniform(20.0,48.0), 1)

    def publish(self):
        message = self.__message
        message["v"] = self.randomValueGenerator()
        message["t"] = str(time.time())
        self.mqttClient.myPublish(self.topic, message)
        print(f'Published {message} to {self.topic}')
        #--------------------------------------------REST API------------------------------------------------
        # readings = {"api_key": "A4K0Q4HTP2BZ3HLJ", "field1": str(message["v"]), "field2": None}
        # url = "https://api.thingspeak.com/update.json"
        # request_headers = {"Content-Type": "application/json"}
        # resp = requests.post(url, readings, request_headers)
        # print(f'Published {message} to ThingSpeak')
        # print("Waiting...", json.loads(resp.text))



#--------------------------------------------MAIN------------------------------------------------
if __name__ == "__main__":
    api = CatalogApi()
    broker = api.getBroker()
    port = api.getPort()
    topic = api.getTopic()
    clientId = api.getClientId()
    tempPub = TemperaturePublisher (clientId, broker, port, topic)
    tempPub.mqttClient.start()
    time.sleep(2)
    print('Temperature Publisher started')
    while True:
            tempPub.publish()
            time.sleep(10)