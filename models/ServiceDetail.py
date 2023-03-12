class ServiceDetail:
    def __init__(self, serviceType: str, serviceIp: str, topics= None): #List[str]:
        self.serviceType = serviceType
        self.serviceIp = serviceIp
        if topics is None:
            pass
        else:
            self.topic = topics
    
    def __repr__(self):
        if hasattr(self, 'topic'):
          return f"ServiceDetail -> {self.serviceType} :: {self.serviceIp} - {self.topic}"
        return f"ServiceDetail -> {self.serviceType} :: {self.serviceIp}"
    
    
if __name__ == "__main__":
    obj = ServiceDetail("REST", "192.127.1.1")
    print(obj.__repr__())

    obj2 = ServiceDetail("MQTT", "mqtt.eclipse.org", ["topic1", "topic2"])
    print(obj2.__repr__())