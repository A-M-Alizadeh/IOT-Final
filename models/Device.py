# import ServiceDetail
import datetime
import uuid
class Device:
    def __init__(self, deviceName: str, meatureType : list[str], availableServices: list[str], servicesDetailes: list[str]): #List[ServiceDEtails]
        self.deviceId = str(uuid.uuid1())
        self.deviceName = deviceName
        self.meatureType = meatureType
        self.availableServices = availableServices
        self.servicesDetailes = servicesDetailes
        self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def fullUpdate(self, newDevice):
        self.deviceName = newDevice.deviceName
        self.meatureType = newDevice.meatureType
        self.availableServices = newDevice.availableServices
        self.servicesDetailes = newDevice.servicesDetailes
        self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return self
    
    def updateServicesDetails(self, newServicesDetails):
        self.servicesDetailes = newServicesDetails
        self.lastUpdate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return self

    def getFull(self):
        return self
    
    def getId(self):
        return self.deviceId
#-----------------------------------------------------------------------------
    def __repr__(self):
        return f"Device({self.deviceId}, {self.deviceName}, {self.meatureType}, {self.availableServices}, {self.servicesDetailes})"





# if __name__ == "__main__":
#     obj = Device("device1", ["temp"], ["service1"], ["123-123", "65646-12331"])
#     print(obj)
#     obj = Device("device2", ["temp","Humi"], ["service1"], ["123-777", "65646-44444"])
#     print(obj)