import json
import time
import sys
import os
import requests
import joblib
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
# from MicroServices.MQTT.LED.LEDManager import *

# ml_model = joblib.load(currentPath+'ML/condition_recommender.joblib')
# ledMngr = LEDManager ('LEDManager', 'test.mosquitto.org', 1883, 'IoT/grp4/command/led')
# ledMngr.mqttClient.start()
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
        print( f'sensor ${topic}: ${payload} recieved')
        print('--------------------------------------------', json.loads(payload)["v"])
        if topic == 'IoT/grp4/temperature':
            self.saveTemperture(payload)
        elif topic == 'IoT/grp4/humidity':
            self.saveHumidity(payload)
        # elif topic == 'IoT/grp4/command/led':
            #recommendation system
            #feed data is this structure: [min_temp, max_temp, min_humid, max_humid, min_light, max_light, min_co2, max_co2]
            # prediction = ml_model.predict([[20,26,25,50,-0.8,42.0,11]])     
            # ledMngr.publish('Predicted value: '+str(prediction))



    def start(self):
        self.mqttClient.start()
        self.mqttClient.mySubscribe(self. topic)
        
    def stop(self):
        self.mqttClient.stop()

    def saveTemperture(self, value):
        self.saver(currentPath+'MicroServices/MQTT/Storage/Temp.json', value)

    def saveHumidity(self, value):
        self.saver(currentPath+'MicroServices/MQTT/Storage/Humid.json', value)
    
    def saver(self, address, value):
        with open(address, 'r') as f:
            data = json.load(f)
            f.close()
        with open(address, 'w') as f:
            f.truncate()
            data['readings'].insert(0, json.loads(value))
            
            f.write(json.dumps(data, indent=4))
            f.close()


#--------------------------------------------MAIN------------------------------------------------
if __name__ == "__main__":
    cm = CatalogApi()

    led = SensorsSubscriber ('grp4_mqtt_iot_123456', cm.getBroker(), 1883, cm.getTopic())
    led.start()
    while True:
        time.sleep(1)