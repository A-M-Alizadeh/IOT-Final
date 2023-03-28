def insertUser(user):
    try:
        con = sqlite3.connect("DB/Iot-Final.db")
        cur = con.cursor()
        cur.execute("insert into User(userId, chatId, name, surname, username, houseIds)\
                        VALUES ('1', '1', 'John', 'Doe', 'johndoe', '1,2,3')")
        return True
    except:
        print("Error in insertUser")
        return False
