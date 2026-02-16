import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 
from Email import send_alert

load_dotenv()

def check_for_open_spots(driver):

    driver.get("https://sa.ucla.edu/ro/ClassSearch/Results?SubjectAreaName=Computer+Science+(COM+SCI)&CrsCatlgName=143+-+Data+Management+Systems&t=26S&sBy=subject&subj=COM+SCI&catlg=0143&cls_no=%25&undefined=Go&btnIsInIndex=btn_inIndex")
    print("woooo")
    wait = WebDriverWait(driver, 10)
    print("394923523")

    while True:

        print("hie")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "data_row")))
        
        
        class_rows = driver.find_elements(By.CLASS_NAME, "data_row")


        found_open = False
        status_report = []



        for row in class_rows:
            print (f"status report1: {status_report}")


            try:
                print("HEREEEE")
                name_element = row.find_element(By.CSS_SELECTOR, ".sectionColumn p")
                lec_name = name_element.text.strip()

                status_element = row.find_element(By.CLASS_NAME, "statusColumn")
                status_text = status_element.text.strip()

                is_open = "Open" in status_text
                current_status = "OPEN" if is_open else "CLOSED"
                
                status_report.append(f"{lec_name}: {current_status}")
                print (f"status report2: {status_report}")

                if is_open:
                    print(f"!!! ALERT: {lec_name} is OPEN!")
                    send_alert(f"{lec_name} is now {status_text}")
                    found_open = True

            except Exception as e:
                print ("failed")
                continue

        print("--- Status Check ---")
        for item in status_report:
            print(item)
        
        if found_open:
            break 

        print("Still waiting... checking again in 20 seconds")
        time.sleep(20)

    

