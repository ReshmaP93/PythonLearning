import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
#Login
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(3)
#Admin-user management - users
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']//span[1]").click()
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//a[@role='menuitem']").click()

#total number of rows
rows=len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr"))
print("total no. of rows in a table:", rows)

for r in range(1,rows+1):
    status=driver.find_element(By.XPATH,"//table[@id='resultTable']//tbody/tr["+str(r)+"]/td[5]").text
    print(status)
