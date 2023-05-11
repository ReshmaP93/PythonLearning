# TestCase
# ----------------
# 1.Open Web Browser
# 2.Open URL (https://admin-demo.nopcommerce.com/login)
# 3.Enter Username - admin@yourstore.com
# 4.Enter Password - admin
# 5.Click on login
# 6.Capture Title of the homepage(Actual Title)
# 7.Verify Title of the page (Your store - Expected)
# 8.Close Browser

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Firefox("C:\Program Files\Drivers\geckodriver.exe")
driver.maximize_window()
driver.find_element(By.ID,"username").send_keys("")
driver.find_element(By.ID,"password").send_keys("")
driver.find_element(By.CSS_SELECTOR,"button").click()
time.sleep(5)
act_title=driver.title
exp_title="nopcommerce"
if act_title==exp_title:
    print("login test passed")
else:
    print("login test failed")
driver.close()