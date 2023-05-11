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

driver=webdriver.Edge("C:\Program Files\Drivers\msedgedriver.exe")
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/")
driver.find_element(By.ID, "Email").send_keys("")
driver.find_element(By.ID, "Password").send_keys("")
driver.find_element(By.CSS_SELECTOR,"button").click()
time.sleep(5)
act_title = driver.title
exp_title = "nopCommerce"
if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.close()
