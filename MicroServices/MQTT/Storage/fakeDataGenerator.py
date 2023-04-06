import json
import random
import os
import sys
import pandas as pd


monthsIdealTemp = [
    {"1": {"min": 24, "max": 27}},
    {"2": {"min": 23, "max": 26}},
    {"3": {"min": 20, "max": 26}},
    {"4": {"min": 19, "max": 26}},
    {"5": {"min": 18, "max": 27}},
    {"6": {"min": 20, "max": 25}},
    {"7": {"min": 20, "max": 26}},
    {"8": {"min": 19, "max": 26}},
    {"9": {"min": 20, "max": 26}},
    {"10": {"min": 20, "max": 26}},
    {"11": {"min": 20, "max": 26}},
    {"12": {"min": 20, "max": 25}}
    ]

monthsIdealHumid = [
    {"1": {"min": 30, "max": 50}},
    {"2": {"min": 30, "max": 50}},
    {"3": {"min": 30, "max": 50}},
    {"4": {"min": 30, "max": 50}},
    {"5": {"min": 40, "max": 50}},
    {"6": {"min": 35, "max": 50}},
    {"7": {"min": 25, "max": 45}},
    {"8": {"min": 30, "max": 40}},
    {"9": {"min": 25, "max": 40}},
    {"10": {"min": 30, "max": 45}},
    {"11": {"min": 25, "max": 50}},
    {"12": {"min": 30, "max": 50}}
    ]

def generateDatainRange():
    randMonth = random.randint(1, 12)
    randTemp = round(random.uniform(float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"]), float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"])),1)
    randHumid = round(random.uniform(float(monthsIdealHumid[randMonth-1][str(randMonth)]["min"]), float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"])),1)
    userRandChoice = randomWithProbability()
    return {
        "minTemp": monthsIdealTemp[randMonth-1][str(randMonth)]["min"],
        "maxTemp": monthsIdealTemp[randMonth-1][str(randMonth)]["max"],
        "minHumid": monthsIdealHumid[randMonth-1][str(randMonth)]["min"],
        "maxHumid": monthsIdealHumid[randMonth-1][str(randMonth)]["max"],
        "currentTemp": randTemp,
        "currentHumid": randHumid,
        "currentMonth": randMonth,
        "goalTemp": 0,
        "goalHumid": 0,
        "userDecision": userRandChoice
        }  

def generateDataOutofRange1():
    randMonth = random.randint(1, 12)
    #check for the months to see it should be colder or hotter
    if randMonth in range(4,9):
        rnd = randomWithProbability()
        if rnd == 0:
          randTemp = round(random.uniform(
            float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"]),
            float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"])+27)
            ,1)
          randHumid = round(random.uniform(
            float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"]-5),
            float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"])+30)
            ,1)
        else:
          randTemp = round(random.uniform(
            float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"]-3),
            float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"])+27)
            ,1)
          randHumid = round(random.uniform(
            float(monthsIdealHumid[randMonth-1][str(randMonth)]["min"]-10),
            float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"]+20))
            ,1)

    else:
        rnd = randomWithProbability()
        if rnd == 0:
          randTemp = round(random.uniform(
              float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"])-35,
              float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"])-3)
              ,1)
          randHumid = round(random.uniform(
              float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"]),
              float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"])+10)
              ,1)
        else:
          randTemp = round(random.uniform(
              float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"])-35,
              float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"])-3)
              ,1)
          randHumid = round(random.uniform(
              float(monthsIdealHumid[randMonth-1][str(randMonth)]["min"])-10,
              float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"])+20)
              ,1)
    idealTempAvg = (monthsIdealTemp[randMonth-1][str(randMonth)]["min"] + monthsIdealTemp[randMonth-1][str(randMonth)]["max"])/2
    idealHumidAvg = (monthsIdealHumid[randMonth-1][str(randMonth)]["min"] + monthsIdealHumid[randMonth-1][str(randMonth)]["max"])/2
    return {
        "minTemp": monthsIdealTemp[randMonth-1][str(randMonth)]["min"],
        "maxTemp": monthsIdealTemp[randMonth-1][str(randMonth)]["max"],
        "minHumid": monthsIdealHumid[randMonth-1][str(randMonth)]["min"],
        "maxHumid": monthsIdealHumid[randMonth-1][str(randMonth)]["max"],
        "currentTemp": randTemp,
        "currentHumid": randHumid,
        "currentMonth": randMonth,
        "goalTemp": int(idealTempAvg),
        "goalHumid": int(idealHumidAvg),
        "userDecision": 1
        }

def generateDataOutofRange2():
    randMonth = random.randint(1, 12)
    if randMonth in range(4,9):
        rnd = random.randint(0,1)
        if rnd == 0:
          randTemp = round(random.uniform(
            float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"]-10),
            float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"])+10)
            ,1)
          randHumid = round(random.uniform(
            float(monthsIdealHumid[randMonth-1][str(randMonth)]["min"]-30),
            float(monthsIdealHumid[randMonth-1][str(randMonth)]["min"]))
            ,1)
        else:
          randTemp = round(random.uniform(
            float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"]-10),
            float(monthsIdealTemp[randMonth-1][str(randMonth)]["max"])+10)
            ,1)
          randHumid = round(random.uniform(
            float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"]),
            float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"]+20))
            ,1)

    else:
        rnd = random.randint(0,1)
        if rnd == 0:
          randTemp = round(random.uniform(
              float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"])-15,
              float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"])+5)
              ,1)
          randHumid = round(random.uniform(
              float(monthsIdealHumid[randMonth-1][str(randMonth)]["min"]-10),
              float(monthsIdealHumid[randMonth-1][str(randMonth)]["min"])+5)
              ,1)
        else:
          randTemp = round(random.uniform(
              float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"])-15,
              float(monthsIdealTemp[randMonth-1][str(randMonth)]["min"])+5)
              ,1)
          randHumid = round(random.uniform(
              float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"])-5,
              float(monthsIdealHumid[randMonth-1][str(randMonth)]["max"])+10)
              ,1)
    idealTempAvg = (monthsIdealTemp[randMonth-1][str(randMonth)]["min"] + monthsIdealTemp[randMonth-1][str(randMonth)]["max"])/2
    idealHumidAvg = (monthsIdealHumid[randMonth-1][str(randMonth)]["min"] + monthsIdealHumid[randMonth-1][str(randMonth)]["max"])/2
    return {
        "minTemp": monthsIdealTemp[randMonth-1][str(randMonth)]["min"],
        "maxTemp": monthsIdealTemp[randMonth-1][str(randMonth)]["max"],
        "minHumid": monthsIdealHumid[randMonth-1][str(randMonth)]["min"],
        "maxHumid": monthsIdealHumid[randMonth-1][str(randMonth)]["max"],
        "currentTemp": randTemp,
        "currentHumid": randHumid,
        "currentMonth": randMonth,
        "goalTemp": int(idealTempAvg),
        "goalHumid": int(idealHumidAvg),
        "userDecision": 1
        }

def randomWithProbability():
    # 0 - turn off
    # 1 - turn on and go to desired temp and humid which is the average of the ideal temp and humid
    mylist = [0,0,1,0,1,0,0,0,1,0]
    return random.choice(mylist)






if __name__ == "__main__":
  for i in range(1):
       print(generateDatainRange())
       print(generateDataOutofRange1())
       print(generateDataOutofRange2())


  # tem = [] 
  # for i in range(3000):
  #   tem.append(generateDatainRange())
  #   tem.append(generateDataOutofRange1())
  #   tem.append(generateDataOutofRange2())
  #   pd.DataFrame(tem).to_csv(os.getcwd()+"/Microservices/MQTT/Storage/MLData.csv", index = None)
     


    # tempData = []
    # for item in range(4000):
    #     tempData.append(generateDatainRange())
    #     tempData.append(generateDataOutofRange1())
    #     tempData.append(generateDataOutofRange2())

    # with open(os.getcwd()+"/Microservices/MQTT/Storage/AnalyticsData.json", "r") as f:
    #     data = json.load(f)
    #     data.extend(tempData)
        
    # with open(os.getcwd()+"/Microservices/MQTT/Storage/AnalyticsData.json", "w") as f:
    #     json.dump(data, f, indent=4)

    # df = pd.read_json(os.getcwd()+"/Microservices/MQTT/Storage/AnalyticsData.json")
    # df.to_csv (os.getcwd()+"/Microservices/MQTT/Storage/MLData.csv", index = None)
