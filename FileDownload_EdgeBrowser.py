import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_object = Service("C:\Program Files\Drivers\msedgedriver.exe")
#download the files in desired location
    preferences={"download.default_directory":location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(service=serv_object)
    return driver

#Automation code
mydriver=edge_setup()
mydriver.get("https://demo.automationtesting.in/FileDownload.html")
mydriver.maximize_window()
mydriver.find_element(By.XPATH,"//a[@type='button']").click()
time.sleep(5)