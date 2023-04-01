import json
import uuid


class CatalogManager:

    # ----------------- Constructor -----------------#
    def __init__(self, catalogPath: str):
        self.catalogPath = catalogPath
        with open(self.catalogPath, "r") as outfile:
            self.catalog = json.load(open(catalogPath))
            outfile.close()

    # ----------------- Getters -----------------#

    def getUsers(self):
        return self.catalog["usersList"]

    def getHouses(self):
        return self.catalog["houses"]

    def getCatalog(self):
        return self.catalog
    
    def getAllDevices(self):
        tempDevices = []
        for house in self.catalog["houses"]:
            for device in house["devicesList"]:
                tempDevices.append(device)
        return tempDevices


    # ----------------- Setters -----------------#

    def createUser(self, newUser):
        newUser["userId"] = str(uuid.uuid1())
        newUser["chatId"] = str(uuid.uuid1())
        self.catalog["usersList"].append(newUser)
        self.saveJson()
        return newUser["userId"]

    def createHouse(self, newHouse):
        newHouse["houseId"] = str(uuid.uuid1())
        if "userId" not in newHouse:
            newHouse["userId"] = ""
        else:
            self.setUserHouse(newHouse["userId"], newHouse["houseId"])
        self.catalog["houses"].append(newHouse)
        self.saveJson()
        return newHouse["houseId"]

    def setUserHouse(self, userId, houseId):
        user = self.findUser(userId)
        if user is not None:
            user["houseId"] = houseId
            return True
        return False

    def updateHouseUser(self, userId, houseId):
        user = self.findUser(userId)
        if user is not None:
            user["houseId"] = houseId
            return True
        return False

    def createOrUpdateDevice(self, newDevice, userId, houseId):
        isNew = True
        user = self.findUser(userId)
        if user is not None:
            house = self.findHouse(houseId)
            if house is not None:
                house["userId"] = userId
                for dev in house["devicesList"]:
                    if dev["deviceId"] == newDevice["deviceId"]:
                        house["devicesList"][house["devicesList"].index(
                            dev)] = newDevice
                        isNew = False
                if isNew:
                    newDevice["deviceId"] = str(uuid.uuid1())
                    house["devicesList"].append(newDevice)
                self.saveJson()
                return newDevice["deviceId"]
            return False
        return False

    # ----------------- Finders -----------------#

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

    def findHouseByUser(self, userId: str):
        houses = []
        for house in self.getHouses():
            if house["userId"] == userId:
                houses.append(house)
        return houses

    def findUserByHouse(self, houseId: str):
        users = []
        for user in self.getUsers():
            if houseId in user["houseId"]:
                users.append(user)
        return users

    def findDevice(self, deviceId: str):
        for house in self.catalog["houses"]:
            for device in house["devicesList"]:
                print('--------->',device)
                if device["deviceId"] == deviceId:
                    return device
        return None

    def findDeviceByUser(self, userId: str):
        tempDevices = []
        for house in self.catalog["houses"]:
            if house["userId"] == userId:
                for device in house["devicesList"]:
                    tempDevices.append(device)
        return tempDevices

    def findDeviceByHouse(self, houseId: str):
        tempDevices = []
        for house in self.catalog["houses"]:
            if house["houseId"] == houseId:
                for device in house["devicesList"]:
                    tempDevices.append(device)
        return tempDevices

    def findDeviceByMeasureType(self, measureType: str):
        tempDevices = []
        for house in self.catalog["houses"]:
            for device in house["devicesList"]:
                for measure in device["measureType"]:
                    if measure == measureType:
                        tempDevices.append(device)
                        continue
        return tempDevices

    # ----------------- updater -----------------#

    def updateUser(self, userId,  newUser):
        user = self.findUser(userId)
        if newUser["houseId"] == "":
            newUser["houseId"] = user["houseId"]
        newUser["userId"] = user["userId"]
        newUser["chatId"] = user["chatId"]
        if user is not None:
            self.catalog["usersList"][self.catalog["usersList"].index(
                user)] = newUser
            self.saveJson()
            return user["userId"]
        return False

    def updateHouse(self, houseId,  newHouse):
        house = self.findHouse(houseId)
        newHouse["houseId"] = house["houseId"]
        if house is not None:
            print(house)
            print("------------------")
            print(newHouse)
            print("updating house ...")
            self.catalog["houses"][self.catalog["houses"].index(
                house)] = newHouse
            self.saveJson()
            return house["houseId"]
        return False

    # ----------------- Remover -----------------#

    def removeUser(self, userId):
        user = self.findUser(userId)
        print('-----> ', userId, user)
        if user is not None:
            self.catalog["usersList"].remove(user)
            houses = self.findHouseByUser(userId)
            if houses is not None:
                for house in houses:
                    print("removing house ...")
                    house["userId"] = ""
                    self.updateHouse(house["houseId"], house)
            self.saveJson()
            return True
        return False

    def removeHouse(self, houseId):
        house = self.findHouse(houseId)
        if house is not None:
            self.catalog["houses"].remove(house)
            users = self.findUserByHouse(houseId)
            if users is not None:
                for user in users:
                    user["houseId"] = ""
                    self.updateUser(user["userId"], user)
            self.saveJson()
            return True
        return False

    def removeDevice(self, deviceId, houseId):
        house = self.findHouse(houseId)
        if house is not None:
            for device in house["devicesList"]:
                if device["deviceId"] == deviceId:
                    house["devicesList"].remove(device)
                    self.saveJson()
                    return True
        return False
    # ----------------- Saver -----------------#

    def saveJson(self):
        with open(self.catalogPath, "w") as outfile:
            outfile.truncate()
            outfile.write(json.dumps(self.catalog, indent=4))
            outfile.close()


# --------------------------------------- Main #---------------------------------------

# if __name__ == "__main__":
#     try:
#         cr = CatalogManager("./Catalog/Catalogue.json")
#     except:
#         print("Error while loading the json file")
#         exit(1)

#     cr.removeHouse("12")
#     cr.saveJson()

    # newUserID = cr.createUser({"username": "ABS", "houseId": ""})
    # newhouseID = cr.createHouse({"houseName": "Casabelanca", "devicesList": []})
    # cr.setUserHouse(newUserID, newhouseID)
    # cr.createOrUpdateDevice({
    #     "deviceId": 1, "deviceName": "Newww Device" ,
    #     "measureType": ["Temperature", "Humidity", "NEWWW Measure"],
    #     "availableServices":["MQTT"],
    #     "servicesDetails": {
    #         "serviceType":"MQTT",
    #         "serviceIp":"mqtt.mosquitto.org",
    #         "topic":["mySmartThing/temp/1","mySmartThing/humid/1"]
    #     }
    # }, "1263cf68-cccd-11ed-983c-ae52d2a871b1", "057f9fe4-ccd1-11ed-96ce-ae52d2a871b1")

    # newUserID = cr.createUser({"username": "Eva", "houseId": [200]})
    # newhouseID = cr.createHouse({"houseName": "Casa Eva", "devicesList": []})
    # cr.setUserHouse(newUserID, newhouseID)
    # cr.createOrUpdateDevice({
    #     "deviceName": "AirConditioner" ,
    #     "measureType": [],
    #     "availableServices":["REST"],
    #     "servicesDetails": {
    #         "serviceType":"REST",
    #         "serviceIp":"http://localhost:8080",
    #     }
    # }, newUserID, newhouseID)

    # cr.updateUser("bd12dc64-ccc9-11ed-8c45-ae52d2a871b1", {"username": "Alex", "houseId": ["2016"]})

    # cr.createUser({"username": "sara", "houseId": []})
    # print(cr.getHouses())
    # cr.updateHouse(1, {})
    # print(cr.getHouses())
    # cr.saveJson()

    # print(cr.getCatalog())
    # print(cr.getUsers())
    # print(cr.getHouses())
    # print(cr.findUser("25bd6f52-ccc7-11ed-b6a6-ae52d2a871b1"))
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
    # cr.saveJson()
