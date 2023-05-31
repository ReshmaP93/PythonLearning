#Ctrl+A
#Ctrl+C
#Tab
#Ctrl+V
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()
input1=driver.find_element(By.XPATH,"inputText1")
input2=driver.find_element(By.XPATH,"inputText2")
input1.send_keys("Welcome to Selenium")
action=ActionChains(driver)

#input1 - Ctrl A - select the text
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#input1 - Ctrl C - Copy the text

action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#Tab key to navigate to second input box
action.send_keys(Keys.TAB).perform()

#Paste to second input box
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(15)