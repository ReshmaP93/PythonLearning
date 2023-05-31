import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_object = Service("C:\Program Files\Drivers\geckodriver.exe")
    #Settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",1)
    ops.set_preference("browser.download.dir",location)

    driver = webdriver.Firefox(service=serv_object,options=ops)
    return driver
#Automation code
mydriver=firefox_setup()
mydriver.get("https://demo.automationtesting.in/FileDownload.html")
mydriver.maximize_window()
mydriver.find_element(By.XPATH,"//a[@type='button']").click()
time.sleep(5)