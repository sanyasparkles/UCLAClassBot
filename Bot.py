import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  
from LogIn import ucla_login
from Email import send_alert
from Tracker import check_for_open_spots

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# chrome_options = Options()
# chrome_options.add_argument("--headless=new")  
# chrome_options.add_argument("--disable-gpu")   
# chrome_options.add_argument("--window-size=1920,1080")

# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()),
#     options=chrome_options
# )

try:
    ucla_login(driver)
    driver.minimize_window()
    # check_for_open_spots(driver, "MATH 170E", "https://sa.ucla.edu/ro/ClassSearch/Results?SubjectAreaName=Mathematics+(MATH)&CrsCatlgName=170E+-+Introduction+to+Probability+and+Statistics+1%3A+Probability&t=26S&sBy=subject&subj=MATH+++&catlg=0170E&cls_no=%25&undefined=Go&btnIsInIndex=btn_inIndex")
    check_for_open_spots(driver, "COM SCI 143", "https://sa.ucla.edu/ro/ClassSearch/Results?SubjectAreaName=Computer+Science+(COM+SCI)&CrsCatlgName=143+-+Data+Management+Systems&t=26S&sBy=subject&subj=COM+SCI&catlg=0143&cls_no=%25&undefined=Go&btnIsInIndex=btn_inIndex")
    


finally:
    driver.quit()