import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)

driver.get("https://www.ironspider.ca/forms/dropdowns.htm")
driver.maximize_window()
time.sleep(5)

#drpcountry_element=driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcoffee=Select(driver.find_element(By.XPATH,"//select[@name='coffee']"))

#select option for the dropdown
drpcoffee.select_by_visible_text("Black")
#drpcountry.select_by_value("10") #black
#drpcountry.select_by_index(13) #index

#select all the options
alloptions=drpcoffee.options
print("Total no.of options",len(alloptions))

#for opt in alloptions:
     #print(opt.text)

#select option from dropdown without using built-in method
for opt in alloptions:
     if opt.text=="Black":
        opt.click()
        break

