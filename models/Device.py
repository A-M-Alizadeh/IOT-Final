# from ServiceDetail import ServiceDetail
import datetime
class Device:
    def __init__(self, deviceName: str, meatureType : list[str], availableServices: list[str], serVicesDetailes: list[any]): #List[ServiceDEtails]
        self.deviceName = deviceName
        self.meatureType = meatureType
        self.availableServices = availableServices
        self.serVicesDetailes = serVicesDetailes
        self.lastUpdate = datetime.datetime.now()

    def update(self, newDevice):
        self.deviceName = newDevice.deviceName
        self.meatureType = newDevice.meatureType
        self.availableServices = newDevice.availableServices
        self.serVicesDetailes = newDevice.serVicesDetailes
        self.lastUpdate = datetime.datetime.now()

    def __repr__(self):
        return f"Device -> {self.deviceName} :: {self.meatureType} - {self.availableServices} - {self.serVicesDetailes} - {self.lastUpdate}"
    
    # def save_to_db(self):
    #     pass
    
# if __name__ == "__main__":
#     obj = Device("device1", ["temp"], ["service1"], [ServiceDetail("REST", "192.127.1.1"), ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])])
#     print(obj.__repr__())
#     obj = Device("device2", ["temp","Humi"], ["service1"], [ServiceDetail("REST", "192.127.5.2:8080")])
#     print(obj.__repr__())