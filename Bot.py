import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from LogIn import ucla_login, reload_class
from Email import send_alert

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    ucla_login(driver)
    reload_class(driver)

    # TARGET_PAGE = "https://be.my.ucla.edu/some_specific_page"
    # driver.get(TARGET_PAGE)

   
    # while True:
    #     driver.refresh()
    #     time.sleep(5) # Give it a second to load
        
    #     # Replace 'number-id' with the actual ID you found via Inspect Element
    #     element_text = driver.find_element(By.ID, "number-id").text
        
    #     if element_text != "0":
    #         send_alert(element_text)
    #         break # Exit after finding it, or remove 'break' to keep watching
            
    #     print(f"Still zero... checking again in 1 minutes.")
    #     time.sleep(120) 

finally:
    driver.quit()