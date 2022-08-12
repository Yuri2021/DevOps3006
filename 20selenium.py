from selenium import webdriver
my_driver = webdriver.Chrome()
my_driver.get("https://github.com")
my_driver.find_element(by ="id",value="billamt").send_keys("100")
my_driver.find_element(by="xpath",value='//*[@id="serviceQual"]/otion[4]').click()

expected="8.00"
actual=my_driver.find_element(by="id",value="tip").text
assert expected!= actual
