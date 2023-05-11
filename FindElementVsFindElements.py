import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://demo.nopcommerce.com/")

###find_element() - returns single web element

#1. Locator matching with single web element
#element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#driver.maximize_window()
#element.send_keys("Apple MacBook Pro 13-inch")
#time.sleep(5)

#2.Locator matching with multiple web element
#element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
#driver.maximize_window()
#time.sleep(5)
#print(element.text)

#3. Element not available then throw NoSuchElementException
#login_element=driver.find_element(By.LINK_TEXT,"Log")
#login_element.click()
#time.sleep(5)

###find_elements() - returns multiple web elements
#1. Locator matching with single web element
#elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
#print(len(elements)) #1
#print(elements[0].send_keys("Apple MacBook Pro 13-inch"))

#2.Locator matching with multiple web element
#elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
#print(len(elements)) #23
#print(elements[0].text)

#for ele in elements:
    #print(ele.text)

#3. Element not available then throw NoSuchElementException
login_elements=driver.find_elements(By.LINK_TEXT,"Log")
print("elements returned:",len(login_elements))