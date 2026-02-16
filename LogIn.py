import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 

load_dotenv()



def ucla_login(driver):
    driver.get("https://my.ucla.edu")
    wait = WebDriverWait(driver, 10)

    login_button = driver.find_element(By.CSS_SELECTOR, "#ctl00_signInLink")
    login_button.click()

    username_entry = driver.find_element(By.ID, "logon")
    username_entry.send_keys(os.getenv("UCLA_USER"))

    password_entry = driver.find_element(By.ID, "pass")
    password_entry.send_keys(os.getenv("UCLA_PASS"))


    return_button = driver.find_element(By.CSS_SELECTOR, '#sso > form > div > table > tbody > tr > td:nth-child(1) > button')
    return_button.click()
                     
    input("Press ENTER once you finish the touch-id")






   
