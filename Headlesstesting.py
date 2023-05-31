from selenium import webdriver
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
    ops=webdriver.ChromeOptions
    ops.headless=True
    driver=webdriver.Chrome(service=serv_object,options=ops)
    return driver
driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()
