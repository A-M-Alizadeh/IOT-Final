import uuid
from House import House
# from typing import List

class User:
    def __init__(self, name: str, surename: str, username: str):
        self.userId = uuid.uuid1()
        self.chatId = uuid.uuid1()
        self.name = name
        self.surename = surename
        self.username = username
        self.houses = []
    
    def setHouses(self, houses): #: List[House]
        self.houses = houses

    def __repr__(self):
        return f"User -> {self.userId} :: {self.username} - {self.name} {self.surename}"
    
    def userUpdate(self,user):
        if isinstance(user, User) :
            self.name = user.name
            self.surename = user.surename
            self.username = user.username
    def getAttr(self, attr: str):
        return self[attr]
        

    def save_to_db(self):
        print("saving User: {self.}")
        # db.session.add(self)
        # db.session.commit()