import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from LogIn import ucla_login
from Email import send_alert
from Tracker import check_for_open_spots

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    ucla_login(driver)
    check_for_open_spots(driver)


finally:
    driver.quit()