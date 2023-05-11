from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\Program Files\Drivers\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

#Absolute Xpath
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/input[1]").send_keys("Tees")
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/span[1]/input[1]").click()

#Relative Xpath
#driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Tees")
#driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()

#Or
#driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox' or @name='field-keywords']").send_keys("Tees")
#driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button' or @class='nav-input nav-progressive-attribute']").click()

#contains()
#driver.find_element(By.XPATH,"//input[contains(@id,'twotabsearchtextbox')]").send_keys("Tees")
#driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()

#text()
driver.find_element(By.XPATH,"//a[@text()='Mobiles']").click()