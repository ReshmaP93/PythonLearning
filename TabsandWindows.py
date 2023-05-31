import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()
#reglink=Keys.CONTROL+Keys.RETURN
#driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)
#time.sleep(5)

#New Tab - Selenium 4 - Opens a new tab and switches to a new tab
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")
