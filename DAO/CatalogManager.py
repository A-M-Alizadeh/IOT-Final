import json

class CatalogManager:
    
    #----------------- Constructor -----------------#
    def __init__(self, catalogPath: str):
        self.catalog = json.load(open(catalogPath))

    #----------------- Getters -----------------#

    def getUsers(self):
        return self.catalog["usersList"]
    
    def getHouses(self):
        return self.catalog["houses"]
    
    def getCatalog(self):
      return self.catalog
    
    #----------------- Finders -----------------#
    
    def findUser(self, userId: str):
        for user in self.catalog["usersList"]:
            if user["userId"] == userId:
                return user
        return None
    
    def findHouse(self, houseId: str):
        for house in self.catalog["houses"]:
            if house["houseId"] == houseId:
                return house
        return None
    
    def findHouseDevices(self, houseId: int):
        house = self.findHouse(houseId)
        if house is not None:
            return house["devicesList"]
        return None
    
    def findDevice(self, deviceId: int):
        for house in self.catalog["houses"]:
            for device in house["devicesList"]:
                if device["deviceId"] == deviceId:
                    return device
        return None
    
    def findDevice(self, deviceId: int):
        for house in self.catalog["houses"]:
            for device in house["devicesList"]:
                if device["deviceId"] == deviceId:
                    return device
        return None
    
    def findDeviceByMeasureType(self, measureType: str):
        tempDevices = []
        for house in self.catalog["houses"]:
            for device in house["devicesList"]:
                for measure in device["measureType"]:
                  if measure == measureType:
                    tempDevices.append(device)
                    continue
        return tempDevices
    
    #----------------- Setter -----------------#

    def createOrUpdateDevice(self, newDevice, userId, houseId):
        user = self.findUser(userId)
        if user is not None:
            house = self.findHouse(houseId)
            if house is not None:
                for dev in house["devicesList"]:
                    if dev["deviceId"] == newDevice["deviceId"]:
                        house["devicesList"][house["devicesList"].index(dev)] = newDevice
                        return True
                house["devicesList"].append(newDevice)
                return True
        return False
    
    #----------------- Saver -----------------#

    def saveJson(self):
        with open("date.json", "w") as outfile:
            json.dump(self.catalog, outfile)

# if __name__ == "__main__":
#     cr = CatalogManager("./DAO/Catalogue.json")
    # print(cr.getCatalog())
    # print(cr.getUsers())
    # print(cr.getHouses())
    # print(cr.findUser("Foo Bar"))
    # print(cr.findHouse(1))
    # print(cr.findHouseDevices(1))
    # print(cr.findDevice(1))
    # print(cr.findDeviceByMeasureType("Temperature"))

    # cr.createOrUpdateDevice({
    #     "deviceId": 1, "deviceName": "Newww Device" , 
    #     "measureType": ["Temperature", "Humidity", "NEWWW Measure"], 
    #     "availableServices":["MQTT"],
    #     "ervicesDetails": {
    #       "serviceType":"MQTT",
    #       "serviceIp":"mqtt.eclipse.org",
    #       "topic":["mySmartThing/temp/1","mySmartThing/humid/1"]
    #     }}, "Foo Bar", 1)
    # cr.createOrUpdateDevice({
    #     "deviceId": 10, "deviceName": "Newww Device" , 
    #     "measureType": ["Temperature", "Humidity", "NEWWW Measure"], 
    #     "availableServices":["MQTT"],
    #     "ervicesDetails": {
    #       "serviceType":"MQTT",
    #       "serviceIp":"mqtt.eclipse.org",
    #       "topic":["mySmartThing/temp/1","mySmartThing/humid/1"]
    #     }}, "Foo Bar", 1)

    # print("-------",cr.findHouse(1))


