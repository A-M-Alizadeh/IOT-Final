import json
import time
import sys
import os
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
        fullPath = conf["baseUrl"]+str(conf["rest_port"])+'/device?'+'&deviceId='+conf["humid_deviceId"] # + 'userId='+conf["userId"]
        response = requests.get(fullPath, headers=headers).json()
        self.broker = response["servicesDetails"]["serviceIp"]
        self.port = 1883
        self.topic = response["servicesDetails"]["topic"][0]
    
    def getBroker(self):
        return self.broker
    
    def getPort(self):
        return self.port
    
    def getTopic(self):
        return self.topic[0: self.topic.rindex('/')+1] + '+'


#--------------------------------------------MQTT------------------------------------------------
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


#--------------------------------------------MAIN------------------------------------------------
if __name__ == "__main__":
    cm = CatalogApi()


    led = SensorsSubscriber ('grp4_mqtt_iot_123456', cm.getBroker(), 1883, cm.getTopic())
    led.start()
    while True:
        time.sleep(1)