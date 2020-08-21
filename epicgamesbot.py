from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

drivers = [webdriver.Chrome(PATH), webdriver.Chrome(PATH)]
elements = [0, 0]

SITE = "https://www.epicgames.com/store/en-US/free-games"
CLASS_NAME = "css-1r3zsoc-StatusBar__root"

for i in range(len(drivers)):
    drivers[i].get(SITE)
    elements[i] = drivers[i].find_elements_by_class_name(CLASS_NAME)
    elements[i][i].click()