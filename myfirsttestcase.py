#TestCase
#----------------
# 1.Open Web Browser
# 2.Open URL (https://opensource-demo.orangehrmlive.com)
# 3.Enter Username - Admin
# 4.Enter Password - admin123
# 5.Click on login
# 6.Capture Title of the homepage(Actual Title)
# 7.Verify Title of the page (Orange HRM - Expected)
# 8.Close Browser

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button").click()
time.sleep(5)
act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login Test passed")
else:
    print("Login Test failed")

driver.close()
