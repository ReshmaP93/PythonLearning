from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\Program Files\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")

#tag and ID
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")

#tag and classname
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

#tag and attribute
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")

#tag,class and attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("xyz")