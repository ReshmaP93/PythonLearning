#we need to install requests package to work on these broken links

import requests as requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in alllinks:
    url=link.get_attribute('href')
    try:
      response=requests.head(url)
    except:
        None
    if response.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url, "is valid link")
print("No. of broken links",count)