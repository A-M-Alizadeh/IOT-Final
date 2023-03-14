# from Device import Device
# from ServiceDetail import ServiceDetail
import uuid
# from typing import List

class House:
    def __init__(self, usersIDs: list[int], devicesList = []): #List[Device]):
        self.houseId = uuid.uuid1()
        self.usersIDs = usersIDs
        self.devicesList = devicesList

    def getFull(self):
        return self
    
    def __str__(self):
        return f"House -> {self.houseId} :: {self.usersIDs} - {self.devicesList}"

    def update(self, newHouse):
        self.usersIDs = newHouse.usersIDs
        self.devicesList = newHouse.devicesList

    def getId(self):
        return str(self.houseId)
    
    def getUserIds(self):
        return self.usersIDs
    
    def getDevices(self):
        return self.devicesList
        
    
    # def __repr__(self):
    #     return f"House -> {self.houseId} :: {self.usersIDs} - {self.devicesList}"
    
# if __name__ == "__main__":
#     d1 = Device("device1", ["temp"], ["service1"], [ServiceDetail("REST", "192.127.1.1"),
#                                                     ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])])
    
#     d2 = Device("device2", ["temp","Humi"], ["service1"], [ServiceDetail("REST", "192.127.5.2:8080")])
#     h1 = House([1], [d1,d2])
#     h2 = House([1,2], [d1,d2])
#     print(h1.__repr__())