from Device import Device
import uuid
# from typing import List

class House:
    def __init__(self, usersIDs: list[int], devicesList): #List[Device]):
        self.houseId = uuid.uuid1()
        self.usersIDs = usersIDs
        self.devicesList = devicesList
    
    def __repr__(self):
        return f"House -> {self.houseId} :: {self.usersIDs} - {self.devicesList}"
    
if __name__ == "__main__":
    d1 = Device("device1", ["temp"], ["service1"], ["details1"])
    d2 = Device("device2", ["temp","Humi"], ["service1"], ["details1"])
    obj = House([1,2,3], [d1,d2])
    print(obj.__repr__())