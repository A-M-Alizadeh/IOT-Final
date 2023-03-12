from models.User import User
from models.House import House
from models.Device import Device
from models.ServiceDetail import ServiceDetail


class CatalogMaker:
    def __init__(self):
        self.users = []
        self.houses = []
        self.devices = []
        self.services = []

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
            if user.userId == userId:
                return user
        return None
    
    def findHouse(self, houseId):
        for house in self.houses:
            if house.houseId == houseId:
                return house
        return None
    
    def findDevice(self, deviceId):
        for device in self.devices:
            if device.deviceId == deviceId:
                return device
        return None
    
    def findService(self, serviceId):
        for service in self.services:
            if service.serviceId == serviceId:
                return service
        return None