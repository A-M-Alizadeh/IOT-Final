class Device:
    def __init__(self, deviceName: str, meatureType : list[str], availableServices: list[str], serVicesDetailes: list[any]): #List[ServiceDEtails]
        self.deviceName = deviceName
        self.meatureType = meatureType
        self.availableServices = availableServices
        self.serVicesDetailes = serVicesDetailes

    def __repr__(self):
        return f"Device -> {self.deviceName} :: {self.meatureType} - {self.availableServices} - {self.serVicesDetailes}"
    def save_to_db(self):
        pass
    
if __name__ == "__main__":
    obj = Device("device1", ["temp"], ["service1"], ["details1"])
    print(obj.__repr__())
    obj = Device("device2", ["temp","Humi"], ["service1"], ["details1"])
    print(obj.__repr__())