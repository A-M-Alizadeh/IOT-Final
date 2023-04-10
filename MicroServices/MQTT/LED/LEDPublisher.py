import json
import time
import sys
import os
import joblib
from datetime import datetime
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
from ML.fakeDataGenerator import monthsIdealTemp, monthsIdealHumid

ml_model = joblib.load(currentPath+'ML/condition_recommender.joblib')

class LEDPublisher:
    def __init__(self,clientID, broker, port, topic):
        self.statusToBool = {"ON": True, "OFF": False}
        self.topic = topic
        self.mqttClient = MyMQTT(clientID, broker, port, None)
        self.__message = {"client": clientID,'n': 'switch', "status": None, "timestamp": ''}

    def start(self):
        self.mqttClient.start()

    def stop(self):
        self.mqttClient.stop()

    def publish(self):
        h_data = json.load(open(currentPath+'MicroServices/MQTT/Storage/Humid.json'))["readings"]
        t_data = json.load(open(currentPath+'MicroServices/MQTT/Storage/Temp.json'))["readings"]
        month = datetime.fromtimestamp(float(t_data[0]["t"])).month
        
        prediction = ml_model.predict([[
            monthsIdealTemp[month-1][str(month)]["min"],
            monthsIdealTemp[month-1][str(month)]["max"],
            monthsIdealHumid[month-1][str(month)]["min"],
            monthsIdealHumid[month-1][str(month)]["max"],
            t_data[0]["v"],
            h_data[0]["v"],
            month
            ]])
            
        message = self.__message
        message["status"] = int(prediction[0][2])
        message["idealTemp"] = int(prediction[0][0])
        message["idealHumid"] = int(prediction[0][1])
        message["timestamp"] = str(time.time())
        message["direct"] = False
        self.mqttClient.myPublish(self.topic, message)
        print(f'Published =>  {message} to {self.topic}')
        #--------------------------------------------REST API------------------------------------------------
        readings = {"api_key": "A4K0Q4HTP2BZ3HLJ", "field1": str(t_data[0]["v"]), "field2": str(h_data[0]["v"])}
        url = "https://api.thingspeak.com/update.json"
        request_headers = {"Content-Type": "application/json"}
        resp = requests.post(url, readings, request_headers)
        print(f'----------------- Published {readings} to ThingSpeak')

if __name__ == "__main__":
    conf = json.load(open(currentPath+'MicroServices/MQTT/config.json'))
    broker = conf['broker']
    port = conf['broker_port']
    topic = conf['topic']
    ledMngr = LEDPublisher ('LEDPublisher', broker, port, 'IoT/grp4/command/led')
    ledMngr.mqttClient.start()
    while True:
            ledMngr.publish()
            time.sleep(30)