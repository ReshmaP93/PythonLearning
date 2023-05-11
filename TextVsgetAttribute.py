import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
time.sleep(5)
emailbox.clear()
emailbox.send_keys("abc@gmail.com")
print("result of text:",emailbox.text)
print("result of get_attribute:",emailbox.get_attribute('value'))
button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print(button.text)
print("result of get_attribute:",button.get_attribute('value'))
print("result of get_attribute:",button.get_attribute('type'))