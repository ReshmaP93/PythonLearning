import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Linktext
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
time.sleep(5)
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click() #some portion of the word is enough for partial linktext
#time.sleep(5)

#Find the total number of links in a page
links=driver.find_elements(By.TAG_NAME,'a') #using tagname
#links=driver.find_elements(By.XPATH,'//a') #using xpath
#print("Total no. of links:",len(links))

#print all the link names
for link in links:
    print(link.text)
    
