import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.save_screenshot("C:\\Users\\hi\\PycharmProjects\\PythonTraining\\Day23_Selenium\\homepage.png")
driver.get_screenshot_as_file("C:\\Users\\hi\\PycharmProjects\\PythonTraining\\Day23_Selenium\\homepage.png")
#driver.get_screenshot_as_png()
#driver.get_screenshot_as_base64() #saves in binary format

driver.quit()