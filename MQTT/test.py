import paho.mqtt.client as mqtt
import time

broker = "test.mosquitto.org"

client = mqtt.Client("Ali2023")  
print("Connecting to broker ",broker)
client.connect(broker)

time.sleep(4)
client.disconnect()