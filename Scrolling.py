import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#1.Scroll down the page by pixel
#driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return window.pageYOffset;")
#print("No.of pixels moved:",value)
#time.sleep(5)

#2.Scroll down page till the element is visible
#flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#value=driver.execute_script("return window.pageYOffset;")
#print("No.of pixels moved:",value) #No.of pixels moved: 7549
#time.sleep(5)

#3.Scroll down page till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("No.of pixels moved:",value) #No.of pixels moved: 9522
time.sleep(5)

#4.Scroll up to the starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("No.of pixels moved:",value) #No.of pixels moved: 0
time.sleep(5)