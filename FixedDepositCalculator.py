import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Day24_Selenium import XLUtils
serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file="D:\RESHMA PEDDETI\CalData.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")
for r in range(2,rows+1):
    #reading data from excel
    princ=XLUtils.readData(file,"Sheet1",r,1)
    rateofInterest=XLUtils.readData(file,"Sheet1",r,2)
    per1=XLUtils.readData(file,"Sheet1",r,3)
    per2=XLUtils.readData(file,"Sheet1",r,4)
    fre=XLUtils.readData(file,"Sheet1",r,5)
    exp_mv=XLUtils.readData(file,"Sheet1",r,6)

#passing data to the application

driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofInterest)
driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)

perioddropdown=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
perioddropdown.select_by_visible_text(per2)
frequencydropdown=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
frequencydropdown.select_by_visible_text(fre)
driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
act_mvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

#validation
if float(exp_mv)==float(act_mvalue):
    print("test passed")
    XLUtils.writeData(file,"Sheet1",r,8,"Passed")
    XLUtils.fillGreen(file,"Sheet1",r,8)
else:
    print("Test failed")
    XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
    XLUtils.fillRed(file, "Sheet1", r, 8)

driver.find_element(By.XPATH,"//*[@id='fdMatVal'']/div[2]/a[2]/img").click()
time.sleep(5)
driver.close()