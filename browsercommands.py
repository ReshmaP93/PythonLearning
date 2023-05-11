import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(15)
#driver.close()
driver.quit()

