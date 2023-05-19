import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(5)
#opens alert window
driver.find_element(By.ID,"confirmButton").click()
time.sleep(10)

alertwindow=driver.switch_to.alert
#print(alertwindow.text())
#alertwindow.send_keys("reshma")
alertwindow.accept() #alert window will be closed by using ok button
