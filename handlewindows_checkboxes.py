import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("http://the-internet.herokuapp.com/")

#1. Select specific checkbox
driver.maximize_window()
time.sleep(10)
driver.find_element(By.PARTIAL_LINK_TEXT,"Checkboxes").click()
time.sleep(10)
driver.find_element(By.XPATH,"//input[1]").click()
time.sleep(2)

#2.Select all the checkboxes
driver.find_element(By.XPATH,"//input[2]").click()
checkboxes=driver.find_elements(By.XPATH,"//input[2]")
print(len(checkboxes))

#Approach 1
#for i in range(len(checkboxes)):
    #checkboxes[i].click()

#Approach 2
#for checkbox in checkboxes:
    #checkbox.click()

#driver.quit()

#3.Select multiple checkboxes by choice
for checkbox in checkboxes:
    colors=checkbox.get_attribute("id")
    if colors=='Blue' or colors=='Green':
        checkbox.click()
