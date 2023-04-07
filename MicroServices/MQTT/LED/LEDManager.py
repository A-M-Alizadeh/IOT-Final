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


class LEDManager:
    def __init__(self,clientID, broker, port, topic):
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
        message["direct"] = True
        self.mqttClient.myPublish(self.topic, message)
        print(f'Published =>  {message} to {self.topic}')

if __name__ == "__main__":
    conf = json.load(open(currentPath+'MicroServices/MQTT/config.json'))
    broker = conf['broker']
    port = conf['broker_port']
    topic = conf['topic']
    ledMngr = LEDManager ('LEDManager', broker, port, 'IoT/grp4/command/led')
    ledMngr.mqttClient.start()
    time.sleep(2)
    print('Welcome to the LED Manager to switch LED ON/OFF')
    done = False
    print('\nType "ON" to switch the LED ON \n and "OFF" to switch the LED OFF \n and "exit" to exit the program :')
    while not done:
        command = input('Enter your command: ')
        if command == 'ON' or command == 'OFF':
            ledMngr.publish(command)
        elif command == 'exit':
            done = True
        else:
            print('Wrong command, try again')