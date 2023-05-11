from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge("C:\Program Files\Drivers\msedgedriver.exe")
driver.get("https://www.nykaa.com")
driver.maximize_window()
#sliders=driver.find_elements(By.CLASS_NAME,"5c464f1b8341e5604add22e5 css-17quusp en1fyme1")
#print(len(sliders))

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))


