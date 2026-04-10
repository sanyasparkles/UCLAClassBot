import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  
from LogIn import ucla_login
from Email import send_alert
from Tracker import check_for_open_spots
from PTE import start_brute_force

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#03461, 21007,  40496, 60610, 80551

try:
    ucla_login(driver)
    #driver.minimize_window()
    start_brute_force("07878", "COM SCI 118", "https://sa.ucla.edu/ro/ClassSearch/Results?SubjectAreaName=Computer+Science+(COM+SCI)&CrsCatlgName=118+-+Computer+Network+Fundamentals&t=26S&sBy=subject&subj=COM+SCI&catlg=0118&cls_no=%25&undefined=Go&btnIsInIndex=btn_inIndex", driver)
    #check_for_open_spots(driver, "COM SCI 143", "https://sa.ucla.edu/ro/ClassSearch/Results?SubjectAreaName=Computer+Science+(COM+SCI)&CrsCatlgName=143+-+Data+Management+Systems&t=26S&sBy=subject&subj=COM+SCI&catlg=0143&cls_no=%25&undefined=Go&btnIsInIndex=btn_inIndex")
    
  

finally:
    driver.quit()