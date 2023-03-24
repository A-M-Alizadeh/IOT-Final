import datetime
import json
import sys

sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final')
from models.User import User
from models.House import House
from models.Device import Device
from models.ServiceDetail import ServiceDetail



class CatalogMaker:
    def __init__(self, projectOwner: str, projectName: str):
        self.projectOwner= projectOwner
        self.projectName= projectName
        self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.users = []
        self.houses = []
        self.devices = []
        self.services = []

    def __repr__(self):
        return f"CatalogMaker({self.projectOwner}, {self.projectName}, {self.lastUpdate}, {self.users}, {self.houses}, {self.devices}, {self.services})"
    
# --------------------------------------------   add methods
    def add_user(self, user: User):
        self.users.append(user)
    
    def add_house(self, house: House):
        self.houses.append(house)
    
    def add_device(self, device: Device):
        self.devices.append(device)
    
    def add_service(self, service: ServiceDetail):
        self.services.append(service)
# --------------------------------------------    get methods
    def getFull(self):
        return self

    def getDevices(self):
        return self.devices
    
    def getHouses(self):
        return self.houses
    
    def getUsers(self):
        return self.users
    
    def getServices(self):
        return self.services
# --------------------------------------------    find methods
    def findUser(self, userId):
        for user in self.users:
            if user.userId == userId:
                return user
        return None
    
    def findUserHouses(self, userId):
        user = self.findUser(userId)
        if user is not None:
            return user.getHouses()
        return None
    
    def findHouse(self, houseId):
        for house in self.houses:
            if house.houseId == houseId:
                return house
        return None
    
    def findHouseUsers(self, houseId):
        house = self.findHouse(houseId)
        if house is not None:
            return house.getUsers()
        return None
    
    def findHouseDevices(self, houseId):
        house = self.findHouse(houseId)
        if house is not None:
            return house.getDevices()
        return None
    
    def findDevice(self, deviceId):
        for device in self.devices:
            if device.deviceId == deviceId:
                return device
        return None
    
    def findDeviceServices(self, deviceId):
        device = self.findDevice(deviceId)
        if device is not None:
            return device.getServices()
        return None
    
    def findService(self, detailId):
        for service in self.services:
            if service.detailId == detailId:
                return service
        return None
# --------------------------------------------   update methods
    def updateUser(self, userId, user: User):
        usr = self.findUser(userId)
        if usr is not None:
            usr.fullUpdate(user)
            self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            return usr
        return False
    
    def updateHouse(self, houseId, house: House):
        hse = self.findHouse(houseId)
        if hse is not None:
            hse.fullUpdate(house)
            self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            return hse
        return False
    
    def updateDevice(self, deviceId, device: Device):
        dev = self.findDevice(deviceId)
        if dev is not None:
            dev.fullUpdate(device)
            self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            return dev
        return False
    
    def updateService(self, serviceId, service: ServiceDetail):
        srv = self.findService(serviceId)
        if srv is not None:
            srv.fullUpdate(service)
            self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            return srv
        return False
# --------------------------------------------   delete methods
#cascade delete !!!
    # def deleteUser(self, userId):
    #     usr = self.findUser(userId)
    #     if usr is not None:
    #         hsz = self.findUserHouses(userId)
    #         if hsz is not None:
    #             return False
    #         else:
    #             self.users.remove(usr)
    #             self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #             return True
    #     return False



#--------------------------------------------    save methods

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
    
    def saveJson(self):
        with open('./Catalog/data.json', 'w') as outfile:
            outfile.truncate()
            outfile.write(self.toJson())
            outfile.close() # .__dict__ or .Json()























# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # print("CatalogMaker")
    cm = CatalogMaker("Ali","HomeAutomation")

    s1 = ServiceDetail("REST", "192.127.1.1")
    s2 = ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])
    s3 = ServiceDetail("MQTT", "mqtt.mosquitto.org", ["iot/humidity", "iot/temperature"])

    d1 = Device("device1", ["temp"], ["service1"], [s1.getId(), s2.getId()])
    d2 = Device("device2", ["temp","Humi"], ["service1"], [s3.getId()])
    d3 = Device("device3", ["accell","speed"], ["service3"], [s3.getId()])

    u1 = User("Ali", "Alizadeh", "gray")
    u2 = User("Alex", "XYZ", "alex")
    u3 = User("John", "Doe", "john")

    h1 = House([u1.getId()], [d1.getId()])
    h2 = House([u2.getId(), u3.getId()], [d2.getId(),d3.getId()])

    u1.setHouses([h1.getId()])
    u2.setHouses([h2.getId()])
    u3.setHouses([h2.getId()])


    cm.add_user(u1)
    cm.add_user(u2)
    cm.add_user(u3)

    cm.add_house(h1)
    cm.add_house(h2)

    cm.add_device(d1)
    cm.add_device(d2)
    cm.add_device(d3)

    cm.add_service(s1)
    cm.add_service(s2)
    cm.add_service(s3)

    # print(u1.getId())
    # cm.updateUser(u1.getId(), User("Sara", "AliPoor", "Sr01", [h1.getId(), "baghbaghu"]))
    # print(u1.getId())

    # print(h1.getId())
    # cm.updateHouse(h1.getId(), House([u1.getId(), u2.getId()], [d1.getId(), d2.getId()]))
    # print(h1.getId())

    # print(d1.getId())
    # print(cm.updateDevice(d1.getId(), Device("device3", ["accell","light"], ["updatedService"], [s3.getId()])))
    # print(d1.getId())

    print(s1.getId())
    cm.updateService(s1.getId(), ServiceDetail("REST", "172.0.0.1"))
    print(s1.getId())



    # print(cm.findUser(u1.getId()))
    # print(cm.findHouse(h1.getId()))
    # print(cm.findHouseDevices(h2.getId()))
    # print(cm.findDevice(d1.getId()))
    # print(cm.findService(s1.getId()))

    # print(cm.findHouse(h1.getId()))

    cm.saveJson()
    print("\n--------------------------------\n")
    # gson = json.dumps(cm, default=lambda o: o.__dict__, indent=4)
    # print(gson)
    # print(cm.__dict__())
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

