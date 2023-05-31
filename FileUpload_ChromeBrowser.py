import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://demo.automationtesting.in/FileUpload.html")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='input-4']").click()
driver.find_element(By.XPATH,"//input[@id='input-4']").send_keys("Desktop\Resume Sample from USA")
time.sleep(5)