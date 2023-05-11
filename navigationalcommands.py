import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")
driver.back() #snapdeal
driver.forward() #amazon
driver.refresh()
driver.quit()
