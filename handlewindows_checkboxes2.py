#Using another website to test multiple checkboxes

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://www.ironspider.ca/forms/checkradio.htm")

#1. Select specific checkbox
driver.maximize_window()
time.sleep(10)
#driver.find_element(By.XPATH,"//input[@value='red']").click()

#2.Select all the checkboxes
#driver.find_elements(By.CSS_SELECTOR,"//input[@type='checkbox']")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#print(len(checkboxes))

#Approach 1
#for i in range(len(checkboxes)):
    #checkboxes[i].click()
    #time.sleep(5)
time.sleep(5)
#Approach 2
for checkbox in checkboxes:
    checkbox.click()

#driver.quit()

#3.Select multiple checkboxes by choice
#for checkbox in checkboxes:
    #colors=checkbox.get_attribute("name")
    #if colors=='Blue' or colors=='Green':
        #checkbox.click()

#4 Select last 2 checkboxes
#totalnumberofelements-2 =starting index
#for i in range(len(checkboxes)-2,len(checkboxes)):#(5,7)--->6,7
    #checkboxes[i].click()
    #time.sleep(2)

#5  Select first 2 checkboxes
for i in range(len(checkboxes)):
    if i<2:
     checkboxes[i].click()
     time.sleep(2)

#6 clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
       checkbox.click()

