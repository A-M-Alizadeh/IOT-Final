#!/bin/sh
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/REST/ && python server.py"
end tell'
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/REST/Micros/Users && python UserService.py"
end tell'
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/REST/Micros/House && python HouseService.py"
end tell'
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/REST/Micros/Devices && python DeviceService.py"
end tell'

sleep 10

osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/MQTT/ && python Subscriber.py"
end tell'
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/MQTT/Humidity/ && python HumidityPublisher.py"
end tell'
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/MQTT/Temprature/ && python TemperaturePublisher.py"
end tell'
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/MQTT/LED/ && python LEDSubscriber.py"
end tell'
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/MQTT/LED/ && python LEDPublisher.py"
end tell'
osascript -e 'tell app "Terminal"
    do script "cd /Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/MQTT/LED/ && python LEDManager.py"
end tell'

