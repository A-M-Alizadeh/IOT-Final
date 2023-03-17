import uuid
import json
# from House import House
# from Device import Device
# from ServiceDetail import ServiceDetail
# from typing import List

class User:
    def __init__(self, name: str, surename: str, username: str, houses = []):
        self.userId = str(uuid.uuid1())
        self.chatId = str(uuid.uuid1())
        self.name = name
        self.surename = surename
        self.username = username
        self.houses = houses
    
    def getFull(self):
        return self
    
    # def __str__(self):
    #     return f"User -> {self.userId} :: {self.chatId} - {self.name} - {self.surename} - {self.username} - {self.houses}"
    # def __json__(self):
    #     return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    # def __repr__(self):
    #     return f"User -> {self.userId} :: {self.chatId} - {self.name} - {self.surename} - {self.username} - {self.houses}"
    
    def update(self, newHouse):
        self.name = newHouse.name
        self.surename = newHouse.surename
        self.username = newHouse.username
        self.houses = newHouse.houses

    def getId(self):
        return str(self.userId)
    
    def setHouses(self, houses): #: List[House]
        self.houses = houses

    def userUpdate(self,user):
        if isinstance(user, User) :
            self.name = user.name
            self.surename = user.surename
            self.username = user.username

    def getAttr(self, attr: str):
        return self[attr]
    
    def getHouses(self):
        return self.houses
    


# if __name__ == '__main__':
#     d1 = Device("device1", ["temp"], ["service1"], [ServiceDetail("REST", "192.127.1.1"),
#                                                     ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])])
#     d2 = Device("device2", ["temp","Humi"], ["service1"], [ServiceDetail("REST", "192.127.5.2:8080")])
#     h1 = House([1], [d1,d2])
#     h2 = House([1,2], [d1,d2])

#     u1 = User("Ali", "Alizadeh", "gray", [h1,h2])
#     print(u1.__repr__())

#     print("\n--------------------------------\n")

#     print(u1.getHouses())