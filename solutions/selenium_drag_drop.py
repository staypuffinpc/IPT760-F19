### PURPOSE [1 pt] Go to https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop and drag w3schools logo to the box above it.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop")

driver.implicitly_wait(3)
driver.switch_to.frame(driver.find_element_by_id("iframeResult"))
time.sleep(1)
source = driver.find_element_by_id("drag1")
target = driver.find_element_by_css_selector("#div1")

try:
    ActionChains(driver).drag_and_drop(source, target).perform()
    # # ActionChains(driver).click_and_hold(source).move_to_element(target).release(target).perform()
    # alert = driver.switch_to_alert.alert
    # alert.accept()

    # ActionChains(driver).drag_and_drop_by_offset(source,30,-150).perform()
except:
    print ("Could not drag elements")
    pass

time.sleep(3)
driver.quit()
