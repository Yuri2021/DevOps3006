# Implementation of Selenium WebDriver with Python on LambdaTest
from selenium import  webdriver
driver = webdriver.Chrome('/c:')
driver.get('https://www.google.com/')
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
import os
import unittest
import sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")


class FirstSampleTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        desired_caps = {
            "build": 'Selenium WebDriver with Python Tutorial',
            "name": 'Running Test on LambdaTest',
            "platform": 'Windows 10',
            "browserName": 'Chrome',
            "version": '73'
        }
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com:80/wd/hub".format(username, access_key),
            desired_capabilities=desired_caps)

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        # try:
        chrome_driver = self.driver

        chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_name("li1").click()
        chrome_driver.find_element_by_name("li2").click()

        title = "Sample page - lambdatest.com"
        assert title == chrome_driver.title

        sample_text = "Happy Testing at LambdaTest"
        email_text_field = chrome_driver.find_element_by_id("sampletodotext")
        email_text_field.send_keys(sample_text)
        sleep(5)

        chrome_driver.find_element_by_id("addbutton").click()
        sleep(5)

        output_str = chrome_driver.find_element_by_name("li6").text
        sys.stderr.write(output_str)

        sleep(2)


if __name__ == "__main__":
    unittest.main()