#Make sure selenium is downloaded, the video in README shows how to do that.
from selenium import webdriver

#Login Info
EMAIL = ""
PASSWORD = ""

#Make sure you have the chrome driver installed. The video in README shows how to do that.
PATH = "C:\Program Files (x86)\chromedriver.exe"

drivers = [webdriver.Chrome(PATH), webdriver.Chrome(PATH)]
elements = [0, 0]

for i in range(len(drivers)):
    #Go to the game's product page
    drivers[i].get("https://www.epicgames.com/store/en-US/free-games")
    elements[i] = drivers[i].find_elements_by_class_name("css-1r3zsoc-StatusBar__root")
    elements[i][i].click()

    #Deal with any "Content is for Mature Audiences" pop-ups.
    try:
        matureWarning = drivers[i].find_element_by_class_name("WarningTemplate-wrapper_4600e045 launcher-nav-left")
    except Exception:
        drivers[i].find_element_by_class_name("css-jm4dil-Button-styles__main").click()

    #Check if game has already been bought
    try:
        drivers[i].find_element_by_class_name("css-zc5dwj-Button-styles__main").click()
    except:
        break

    #Log in to Epic Games
    drivers[i].find_element_by_id("login-with-epic").click()
    drivers[i].find_element_by_id("email").send_keys(EMAIL)
    drivers[i].find_element_by_id("password").send_keys(PASSWORD)
    drivers[i].find_element_by_id("login").click()
    
    #Check if login worked, and purchase game.
    try:
        drivers[i].find_element_by_class_name("btn btn-primary").click()
    except:
        print("Login Failed")
        break
