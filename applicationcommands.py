import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(10)
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()