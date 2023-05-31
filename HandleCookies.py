import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#capture cookies from the browser
cookies=driver.get_cookies()
print("Size of cookies:",len(cookies)) #5

#print details of all the cookies
#for c in cookies:
    #print(c)
    # print(c.get("name"),":",c.get("value"))

#Add a new cookie to a browser
driver.add_cookie({"name":"MyCookie","value":"123"})
cookies=driver.get_cookies()
print("Size of cookies after adding one cookie:", len(cookies)) #6

#Delete a specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print("Size of cookies after deleted one cookie:", len(cookies)) #5

#Delete all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("Size of cookies after deleted one cookie:", len(cookies)) #0

driver.quit()