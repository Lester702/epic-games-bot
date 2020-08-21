from Bot import GetGames
import time

returnValue = str

while True:
    Time = time.ctime.split()[0]

    if Time[0] == "Thu" and int(Time[3].split(":")[0]) >= 8:
        returnValue = GetGames("PUT EMAIL HERE", "PUT PASSWORD HERE")
        if returnValue == "Success":
            time.sleep(604800) #One week
        elif returnValue == "Already Purchased":
            time.sleep(3600) # 1 hour, Feel free to change this
        else:
            quit()