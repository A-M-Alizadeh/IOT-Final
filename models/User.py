import uuid

class User:
    def __init__(self, name: str, surename: str, username: str, housesIds: list[str] = []):
        self.userId = str(uuid.uuid1())
        self.chatId = str(uuid.uuid1())
        self.name = name
        self.surename = surename
        self.username = username
        self.housesIds = housesIds
    
    def fullUpdate(self, updatedUser):
        self.name = updatedUser.name
        self.surename = updatedUser.surename
        self.username = updatedUser.username
        self.housesIds = updatedUser.housesIds
        return self

    def userUpdate(self,user):
        if isinstance(user, User) :
            self.name = user.name
            self.surename = user.surename
            self.username = user.username
            return self

    def setHouses(self, housesIds: list[int]): #: List[House]
        self.housesIds = housesIds

    def getFull(self):
        return self
    
    def getId(self):
        return self.userId

    def getAttr(self, attr: str):
        return self[attr]
    
    def getHouses(self):
        return self.housesIds
    
#----------------------------------------------------
    def __repr__(self):
        return f"User({self.name}, {self.surename}, {self.username}, {self.housesIds})"

    







# if __name__ == '__main__':
#     u1 = User("Ali", "Alizadeh", "gray", ["234-433","123"])
#     print(u1)
#     u1.fullUpdate(User("Aziz", "Alizadeh", "gray", ["111","233-1221"]))
#     print(u1)
#     print(u1.getHouses())
#     print(u1.getId())






    # d1 = Device("device1", ["temp"], ["service1"], [ServiceDetail("REST", "192.127.1.1"),
    #                                                 ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])])
    # d2 = Device("device2", ["temp","Humi"], ["service1"], [ServiceDetail("REST", "192.127.5.2:8080")])
    # h1 = House([1], [d1,d2])
    # h2 = House([1,2], [d1,d2])