import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 
import random
from datetime import datetime
from Email import send_alert

load_dotenv()

def check_for_open_spots(driver, class_name, class_URL):

    driver.get(class_URL)
    wait = WebDriverWait(driver, 10)

    while True:

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "data_row")))
        
        
        class_rows = driver.find_elements(By.CLASS_NAME, "data_row")


        found_open = False
        status_report = []



        for row in class_rows:


            try:
                name_element = row.find_element(By.CSS_SELECTOR, ".sectionColumn p")
                lec_name = name_element.text.strip()

                status_element = row.find_element(By.CLASS_NAME, "statusColumn")
                status_text = status_element.text.strip()

                is_open = "Open" in status_text
                current_status = "OPEN" if is_open else "CLOSED"
                
                status_report.append(f"{lec_name}: {current_status}")

                if is_open:
                    print(f"!!! ALERT: {lec_name} is OPEN!")
                    send_alert(class_name, lec_name)
                    found_open = True

            except Exception as e:
                print ("failed")
                continue

        print("--- Status Check ---")
        for item in status_report:
            print(item)
        
        if found_open:
            break 

        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Last Check: [{current_time}]")


        wait_time = random.randint(20, 60)
        time.sleep(wait_time)

    

