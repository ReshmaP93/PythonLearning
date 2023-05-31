import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_object = Service("C:\Program Files\Drivers\chromedriver.exe")
#download the files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=serv_object)
    return driver

#Automation code
mydriver=chrome_setup()
mydriver.get("https://demo.automationtesting.in/FileDownload.html")
mydriver.maximize_window()
mydriver.find_element(By.XPATH,"//a[@type='button']").click()
time.sleep(5)