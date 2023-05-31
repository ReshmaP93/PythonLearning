import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(5)
driver.switch_to.frame(0) #switch to frame
#mm/dd/yyyy
#straightforward
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("06/29/2022")
time.sleep(5)

year="2024"
month="June"
date="29"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click() #opens a date picker
while True:
      mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
      yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

      if mon==month and yr==year:
          break;
      else:
          driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click() #next arrow
         # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]").click()  # previous arrow
#select date
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for element in dates:
    if element.text==date:
        element.click()
        break