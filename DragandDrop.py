import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(5)
rome_element=driver.find_element(By.ID,"box6")
italy_element=driver.find_element(By.ID,"box106")
action=ActionChains(driver)
action.drag_and_drop(rome_element,italy_element).perform() #drag and drop operation
time.sleep(5)

washington_element=driver.find_element(By.ID,"box3")
unitedstates_element=driver.find_element(By.ID,"box103")
action=ActionChains(driver)
action.drag_and_drop(washington_element,unitedstates_element).perform() #drag and drop operation
time.sleep(5)