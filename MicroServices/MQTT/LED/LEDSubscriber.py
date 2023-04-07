import json
import time
import sys
import os
from datetime import datetime

"""
    -------------------------------------------- Notice --------------------------------------------
    #path to parent folder
    # there is a difference between os.getcwd() in Mac Terminal and VSCode
    # VSCode returns the path to project root folder, while Mac Terminal returns the path to the current folder
"""
currentPath = os.getcwd()[:os.getcwd().find('/Final')+len('/Final')]+os.path.sep
sys.path.insert(1, currentPath)
from MicroServices.MQTT.MyMQTT import *

from ML.fakeDataGenerator import monthsIdealTemp, monthsIdealHumid


class LEDSubscriber:
    def __init__(self,clientID, broker, port, topic):
        self.status = 'OFF'
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, self)

    def notify(self, topic, payload):
        self.status = json.loads(payload)["status"] 
        print( f'led status: ', self.status)
        if json.loads(payload)["direct"] == True:
            self.manualDecision(self.status)
        else:
            self.automaticDecision(payload)
        

    def start(self):
        self.mqttClient.start()
        self.mqttClient.mySubscribe(self. topic)
        
    def stop(self):
        self.mqttClient.stop()

    def manualDecision(self, decision):
        h_data = json.load(open(currentPath+'MicroServices/MQTT/Storage/Humid.json'))["readings"]
        t_data = json.load(open(currentPath+'MicroServices/MQTT/Storage/Temp.json'))["readings"]
        d_data = json.load(open(currentPath+'MicroServices/MQTT/Storage/UserDecisions.json'))
        month = datetime.fromtimestamp(float(t_data[0]["t"])).month
        
        item = [{
            "minTemp":monthsIdealTemp[month-1][str(month)]["min"],
            "maxTemp":monthsIdealTemp[month-1][str(month)]["max"],
            "minHumid":monthsIdealHumid[month-1][str(month)]["min"],
            "maxHumid":monthsIdealHumid[month-1][str(month)]["max"],
            "currentTemp":t_data[0]["v"],
            "currentHumid":h_data[0]["v"],
            "currentMonth":month,
            "userDecision":decision
            }]
        d_data.extend(item)  
        with open(currentPath+'MicroServices/MQTT/Storage/UserDecisions.json', "w") as f:
          json.dump(d_data, f, indent=4)
        print('manual decision saved', item)

    def automaticDecision(self, payload):
        print('automatic decision', payload)
        

if __name__ == "__main__":
    led = LEDSubscriber ('grp4_mqtt_iot_led_sub', 'test.mosquitto.org', 1883, 'IoT/grp4/command/led')
    led.start()
    while True:
        time.sleep(1)