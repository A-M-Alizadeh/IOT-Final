from models.User import User

if __name__ == '__main__':
    obj = User("Kos", "Kesh", "KosKeshe kochak")
    print(obj.__repr__())