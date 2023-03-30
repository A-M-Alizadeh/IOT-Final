import json
import time
import os
import sys
sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final') #/MicroServices/REST/Micros
from MicroServices.MQTT.MyMQTT import *

#test.mosquitto.org
#broker.hivemq.com
#iot.eclipse.org


class HumidityPublisher:
    print(os.getcwd())
    def __init__(self,clientID, broker, port, topic):
        print(os.getcwd())
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
        message["status"] = value #elf.statusToBool[value]
        message["timestamp"] = str(time.time())
        self.mqttClient.myPublish(self.topic, message)
        print(f'Published {message} to {self.topic}')

if __name__ == "__main__":
    broker = 'test.mosquitto.org'
    port = 1883
    topic = 'IoT/grp4/humidity'
    ledMngr = HumidityPublisher ('HumidityManager', broker, port, topic)
    ledMngr.mqttClient.start()
    time.sleep(2)
    print('Humidity Manager started')
    done = False
    a = 0
    while not done:
            a += 1
            ledMngr.publish(f'Humid Detail -> ${a}')
            time.sleep(1)