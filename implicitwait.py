import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.implicitly_wait(10) #10 is seconds
driver.get("https://www.google.com")
driver.maximize_window()
searchbox=driver.find_element(By.NAME,'q')
searchbox.send_keys('Selenium')
searchbox.submit()
#time.sleep(10)
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
#time.sleep(5)
driver.quit()