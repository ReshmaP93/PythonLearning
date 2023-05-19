import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

windowid=driver.current_window_handle
#print(windowid) #B8F77FAD414084FB9B73E6FAEB1EF7FB

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
#time.sleep(10)
windowids=driver.window_handles

#parentwindow=windowids[0]
#childwindow=windowids[1]

#print(parentwindow,childwindow) #7C8733D107C7119B21949CDB6C4718F0 9C0FFBF6BAE6ACDFC7BDDBB007DB8B12

#driver.switch_to.window(childwindow)
#print("Title of child window",driver.title) #Title of child window OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM

#driver.switch_to.window(parentwindow)
#print("Title of parent window",driver.title) #Title of parent window OrangeHRM
#time.sleep(5)
#driver.close()

#Close specific browser window
time.sleep(3)
for windowid in windowids:
    driver.switch_to.window(windowid)
    if driver.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM" or driver.title=='XYZ':
        driver.close()