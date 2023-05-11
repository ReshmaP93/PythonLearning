from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\Program Files\Drivers\chromedriver.exe")
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
#text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Glycols')]/self::a").text
#print(text_msg) #India Glycols

#parent
#text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Glycols')]/parent::td").text
#print(text_msg)

#child
#childs=driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/child::td")
#print(len(childs))

#driver.close()

#ancestor
#text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr").text
#print(text_msg) #India Glycols A 543.70 559.00 + 2.81

#descendant
#descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/descendant::*")
#print("No. of descendant nodes",len(descendants))

#following
#followings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/following::*")
#print("No. of followings nodes",len(followings)) #2783


#following-sibling
#followingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]//ancestor::tr/following-sibling::tr")
#print("No. of following siblings",len(followingsiblings)) #330

#preceding
#precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/preceding::*")
#print("No. of precedings",len(precedings)) #944

#preceding-sibling
precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/preceding-sibling::*")
print("No. of precedings siblings",len(precedingsiblings)) #98