from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() #maximize the browser window
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
#driver.close()
#driver.quit()