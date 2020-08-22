#Make sure selenium is downloaded, the video in README shows how to do that.
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def GetGames(EMAIL, PASSWORD, PATH):
    drivers = [webdriver.Chrome(PATH), webdriver.Chrome(PATH)]
    elements = [0, 0]

    index = 0

    for driver in drivers:
        #Go to the game's product page
        driver.get("https://www.epicgames.com/store/en-US/free-games")
        elements[index] = driver.find_elements_by_class_name("css-1r3zsoc-StatusBar__root")
        elements[index][index].click()

        #Deal with any "Content is for Mature Audiences" pop-ups.
        warning_actions = ActionChains(driver)
        try:
            warning_actions.move_to_element(driver.find_element_by_class_name("ProductDetails-ageGateButtonsWrapper_7713c4c9"))
            warning_actions.click()
            warning_actions.perform()
        except Exception:
            pass

        driver.implicitly_wait(5)
        #Click "Get" button
        get_actions = ActionChains(driver)
        get_actions.move_to_element_with_offset(driver.find_element_by_class_name("css-m8gssx-WishButton-styles__main"), -1, 0)
        get_actions.click()
        get_actions.perform()

        #Log in to Epic Games
        driver.find_element_by_id("login-with-epic").click()
        driver.find_element_by_id("email").send_keys(EMAIL)
        driver.find_element_by_id("password").send_keys(PASSWORD)
        driver.find_element_by_id("login").click()
        
        #Check if login worked, and purchase game.
        try:
            driver.find_element_by_class_name("btn btn-primary").click()
        except Exception:
            print("Login Failed")
        index += 1


GetGames("chrisgallardo@live.com", "Remote12", "C:\Program Files (x86)\chromedriver.exe")