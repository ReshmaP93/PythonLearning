import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
minslider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
maxslider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print("Location of sliders Before moving........")
print(minslider.location) #{'x': 59, 'y': 126}
print(maxslider.location) #{'x': 545, 'y': 126}

actions=ActionChains(driver)
actions.drag_and_drop_by_offset(minslider,100,0).perform()
actions.drag_and_drop_by_offset(maxslider,-45,0).perform()

print("Location of sliders after moving........")
print(minslider.location) #{'x': 161, 'y': 126}
print(maxslider.location) #{'x': 501, 'y': 126}