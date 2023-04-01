import uuid

class ServiceDetail:
    def __init__(self, serviceType: str, serviceIp: str, topics= None): #List[str]:
        self.detailId = str(uuid.uuid1())
        self.serviceType = serviceType
        self.serviceIp = serviceIp
        if topics is None:
            pass
        else:
            self.topics = topics
        
    def fullUpdate(self, newServiceDetail):
        self.serviceType = newServiceDetail.serviceType
        self.serviceIp = newServiceDetail.serviceIp
        if hasattr(newServiceDetail, 'topics'):
            self.topics = newServiceDetail.topics
        return self
    
    def getFull(self):
        return self
    
    def getId(self):
        return self.detailId
#----------------------------------------------------
    def __repr__(self):
        if hasattr(self, 'topics'):
            return f"ServiceDetail({self.detailId}, {self.serviceType}, {self.serviceIp}, {self.topics})"
        else:
            return f"ServiceDetail({self.detailId}, {self.serviceType}, {self.serviceIp})"


    



    
    
# if __name__ == "__main__":
#     obj = ServiceDetail("REST", "192.127.1.1")
#     print(obj)
#     obj.update(ServiceDetail("MQRR", "mqtt.eclipse.com", ["topic1", "TEMP"]))
#     print(obj)
#     obj2 = ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])
#     print(obj2)