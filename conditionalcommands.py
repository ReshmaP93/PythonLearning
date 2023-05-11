import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
time.sleep(10)
#is_displayed  #is_enabled
#searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#print("Display status:",searchbox.is_displayed())
#print("Display status:",searchbox.is_enabled())
#driver.quit()

#is_selected
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("default radio button status.....")

print(rd_male.is_selected()) #False
print(rd_female.is_selected()) #False

rd_male.click() #select male radio button

print("After selecting the male radio button....")
print(rd_male.is_selected()) #True
print(rd_female.is_selected()) #False

time.sleep(10)

rd_female.click() #select female radio button

print("After selecting the female radio button....")
print(rd_male.is_selected()) #False
print(rd_female.is_selected()) #True