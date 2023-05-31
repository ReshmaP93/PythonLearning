#1. Count no. of rows and columns
#2. Read specific row and column data
#3. Read all the rows and columns data
#4. Read data based on conditions (List books name whose author is Mukesh)


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_object=Service("C:\Program Files\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_object)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

#1. Count no. of rows and columns
numberofrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
numberofcolumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

#print(numberofrows) #7
#print(numberofcolumns) #4

#2. Read specific row and column data - Master in selenium

data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
#print(data)

#3. Read all the rows and columns data

print("printing all the rows and columns............")

for r in range(2,numberofrows+1):
    for c in range(1,numberofcolumns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)
    print()

#4. Read data based on conditions (List books name whose author is Mukesh)

for r in range(2,numberofrows+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname=="Mukesh":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookname,"          ",authorname,"      ",price)

driver.close()




