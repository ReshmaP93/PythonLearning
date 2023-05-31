import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
time.sleep(5)
driver.switch_to.frame("iframeResult") #switch to frame
field1=driver.find_element(By.XPATH,"//*[@id='field1']")
field1.clear()
field1.send_keys("Welcome")
button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
actions=ActionChains(driver)
actions.double_click(button).perform() #double click action
