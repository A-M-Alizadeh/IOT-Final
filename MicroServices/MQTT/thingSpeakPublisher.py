import paho.mqtt.publish as publish
from time import sleep
import random
import requests

# while (True):
#     t = float(random.randrange(0, 100))
#     h = float(random.randrange(0, 100))
#     p = float(random.randrange(0, 100))
#     # payload = '{"field1":' + str(t) + ',"field2":' + str(h) + ',"field3":' + str(p) + '}'
#     payload = "field1=" + str(t) + "&field2=" + str(h) + "&field3=" + str(p)

#     print("Published: " + payload + " to ThingSpeak")
#     publish.single(
#         "channels/2099674/publish/A4K0Q4HTP2BZ3HLJ",
#         payload,
#         hostname="mqtt3.thingspeak.com",
#         port=1883,
#         tls=None,
#         transport="tcp")
#     print("Waiting...")
#     sleep(5)

while True:
    t = float(random.randrange(0, 100))
    h = float(random.randrange(0, 100))
    p = float(random.randrange(0, 100))
    readings = {"api_key": "A4K0Q4HTP2BZ3HLJ", "field1": t, "field2": h, "field3": p}
    url = "https://api.thingspeak.com/update.json"
    request_headers = {"Content-Type": "application/json"}
    resp = requests.post(url, readings, request_headers)
    sleep(5)
