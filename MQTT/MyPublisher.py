from MyMQTT import *
import json
import time

class Publisher:
    def __init__(self,clientID, broker, port, topic):
        self.status = 'OFF'
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, self)

    def notify(self, topic, msg): #use senML
        if topic == 'led':
            self.status = json.loads(msg)
            print('led status: ', self.status) 

    def start(self):
        self.mqttClient.start()
        self.mqttClient.myPublish(self. topic, 'ON')