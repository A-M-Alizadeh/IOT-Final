from ..models.User import User
from ..models.House import House
from ..models.Device import Device
from ..models.ServiceDetail import ServiceDetail
import datetime
import json


class CatalogManager:
    def __init__(self, projectOwner: str, projectName: str):
        self.projectOwner= projectOwner
        self.projectName= projectName
        self.lastUpdate = datetime.datetime.now()
        self.users = []
        self.houses = []
        self.devices = []
        self.services = []

    def get(self): #create an object and return it
        return self

    def getFull(self):
        return self

    def __str__(self):
        return f"CatalogManager -> {self.projectOwner} :: {self.projectName} - {self.lastUpdate} - {self.users} - {self.houses} - {self.devices} - {self.services}"

    def add_user(self, user: User):
        self.users.append(user)
    
    def add_house(self, house: House):
        self.houses.append(house)
    
    def add_device(self, device: Device):
        self.devices.append(device)
    
    def add_service(self, service: ServiceDetail):
        self.services.append(service)
    
    def getDevices(self):
        return self.devices
    
    def getHouses(self):
        return self.houses
    
    def getUsers(self):
        return self.users
    
    def getServices(self):
        return self.services
    
    def findUser(self, userId):
        for user in self.users:
            if str(user.userId) == userId:
                return user
        return None
    
    def findHouse(self, houseId):
        for house in self.houses:
            if str(house.houseId) == houseId:
                return house
        return None
    
    def findHouseDevices(self, houseId):
        house = self.findHouse(houseId)
        if house is not None:
            return house.getDevices()
        return None
    
    def saveJson(self):
        with open('data.json', 'w') as outfile:
            json.dump(self.getFull(), outfile)
    

if __name__ == "__main__":
    # print("CatalogManager")
    cm = CatalogManager("Ali","HomeAutomation")

    d1 = Device("device1", ["temp"], ["service1"], [ServiceDetail("REST", "192.127.1.1"),
                                                    ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])])
    d2 = Device("device2", ["temp","Humi"], ["service1"], [ServiceDetail("REST", "192.127.5.2:8080")])

    h1 = House([1], [d1,d2])
    h2 = House([1,2], [d1,d2])

    u1 = User("Ali", "Alizadeh", "gray", [{"HouseId": h1.getId()},{"HouseId": h2.getId()}])

    cm.add_user(u1)
    cm.add_house(h1)
    cm.add_house(h2)
    cm.add_device(d1)
    cm.add_device(d2)

    cm.saveJson()
    print("\n--------------------------------\n")
    # print(cm.getFull())
    # print(cm.getDevices())
    print("\n--------------------------------\n")
    # print(cm.getHouses())
    print("\n--------------------------------\n")
    # print(cm.getUsers())
    print("\n--------------------------------\n")
    # for usr in cm.getUsers():
    #     print(usr.getFull())
    # print(cm.findUser(input("user ID ?")))
    # print(cm.findHouseDevices(input("house ID ?")))

