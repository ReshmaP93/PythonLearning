import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(5)

#MouseHover
blogs=driver.find_element(By.ID,"blogsmenu")
actions=ActionChains(driver)
actions.move_to_element(blogs).perform()
time.sleep(3)

selenium_143=driver.find_element(By.XPATH,"//span[normalize-space()='Selenium143']")
actions.move_to_element(selenium_143).perform()
time.sleep(5)
#driver.quit()