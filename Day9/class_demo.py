### PURPOSE: Demonstrate how to use Selenium to interact with web pages ###

## import needed libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#set Chrome as the driver
driver = webdriver.Firefox()

#navigate to a web page
driver.get("https://my.byu.edu")

time.sleep(3)
login_btn = driver.find_element_by_xpath('//div/a[contains(@title,"Sign In")]/span')
login_btn.click()
