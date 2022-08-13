from selenium import  webdriver
from time import sleep
my_driver = webdriver.Chrome()
#my_driver.get("https://github.com")
#my_driver.get("file:///C:/Users/yoav_/Downloads/tip_calc/tip_calc%25204/index.html")
#billamt = my_driver.find_element(by="id", value="billamt")
my_driver.get("file:///C:/Users/yoav_/Desktop/selenium/calc/index.html")
billamt = my_driver.find_element(by="id", value="billamt").send_keys("100")
my_driver.find_element(by="xpath",value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id",value="peopleamt").send_keys("5")
my_driver.find_element(by="id",value="mustcamt").send_keys("5")
my_driver.find_element(by="id",value="culculate").click()
#TESTING

expected="8.00"
actual=my_driver.find_element(by="id",value="tip").text
assert expected!= actual

#for i in range(5):
    #sleep(5)
    #my_driver.refresh()
#my_driver.close()
