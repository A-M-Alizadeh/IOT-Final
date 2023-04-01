import uuid

class House:
    def __init__(self, usersIDs: list[str] = [], devicesIds : list[str] = []): #List[Device]):
        self.houseId = str(uuid.uuid1())
        self.usersIDs = usersIDs
        self.devicesIds = devicesIds

    def setUsers(self, users):
        self.usersIDs = users

    def setDevices(self, devices):
        self.devicesIds = devices
    
    def fullUpdate(self, newHouse):
        self.usersIDs = newHouse.usersIDs
        self.devicesIds = newHouse.devicesIds
        return self
    
    def updateDevices(self, devices):
        self.devicesIds = devices
        return self
    
    def updateUsers(self, users):
        self.usersIDs = users
        return self

    def getFull(self):
        return self
    
    def getId(self):
        return self.houseId
    
    def getUserIds(self):
        return self.usersIDs
    
    def getDevices(self):
        return self.devicesIds
#----------------------------------------------------
    def __repr__(self):
        return f"House({self.houseId}, {self.usersIDs}, {self.devicesIds})"
        





    
# if __name__ == "__main__":
#     h1 = House(["1"], ["12-32", "1234-3451"])
#     print(h1)
#     h1.updateUsers(["1","2"])
#     print(h1)
#     print("-------------------------------------------------")
#     h2 = House(["1"], ["12-333332", "1234"])
#     print(h2)
#     h2.updateDevices(["12-32", "1234-3453333333331"])
#     print(h2)
#     h2.fullUpdate(h1)
#     print(h2)




    # d1 = Device("device1", ["temp"], ["service1"], [ServiceDetail("REST", "192.127.1.1"),
    #                                                 ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])])
    
    # d2 = Device("device2", ["temp","Humi"], ["service1"], [ServiceDetail("REST", "192.127.5.2:8080")])
    # h1 = House([1], [d1,d2])
    # h2 = House([1,2], [d1,d2])
    # print(h1)