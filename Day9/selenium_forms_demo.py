#### Purpose: to demonstrate how to interact with a page with form elements using Selenium web driver ###

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

###Now let's go to BYU's site and look at upcoming events ###
   ## need to create an action chain
driver.get('https://byu.edu')
cal_btn = driver.find_element_by_class_name("full-events-button").click()
# hover = ActionChains(driver).move_to_element(cal_btn)
# hover.click().perform()

#get the current month so we can compare it to what's in our drop-down list
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

curr_month = datetime.now().strftime('%B')
def findNextMonth(this_month,months_list):
    curr_month_index = months_list.index(this_month) #TODO add 'out of range' cases
    if this_month == "December":
        next_month = "January"
    else:
        next_month = months_list[curr_month_index+1]
    return next_month
next_month_text = findNextMonth(curr_month,months)
print("The current month is "+curr_month,"Next month is "+next_month_text)
month_select = Select(driver.find_element_by_id('monthselector'))
month_select.select_by_visible_text(next_month_text)

#filter by what's interesting to you
filters = ["Arts & Entertainment","Athletics","Conferences","Devotionals & Forums","Education","Health & Wellness","Student Life","Other"]
my_choice = ["Athletics"]
my_choice_index = filters.index(my_choice[0])
#put the checkbox list elements into your own list: field_event_type_tid[]
choices = driver.find_elements_by_name('field_event_type_tid[]')
choice_id = choices[my_choice_index].get_attribute('id')
print("This is the ID you are looking for: ",choice_id)
# the problem is that the input element is hidden and the developers are using a custom span as the checkbox.  So, let's inject a bit of jquery to get the next element and click it
    # from: https://gist.github.com/anhldbk/dc7a040b7fda199a5791
import os
fileDir = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.join(fileDir,'Web_Scraping/jquery-3.3.1.min.js')
# time.sleep(2)
with open(fileName,'r') as jquery_js:
    jquery = jquery_js.read() #read the jquery from the file
    driver.execute_script(jquery) #activate the jquery lib
    js_to_execute = "$('#"+choice_id+"').next().next().click()"
    print(js_to_execute)
    driver.execute_script(js_to_execute)
    # driver.execute_script("alert('is javascript execution working?')")

#now submit the form
choices[my_choice_index].submit()
# time.sleep(3)
#iterate over the resulting calendar and find the relevant upcoming events
events = driver.find_elements_by_css_selector('span.field-content')
print("There are %d %s events in %s" % (len(events), my_choice[0], next_month_text))
for event in events:
    xpath_for_ancestor = "./ancestor::*[7]"
    try:
        day = str(event.find_element_by_xpath(xpath_for_ancestor).get_attribute('data-day-of-month'))
    except:
        day = "No specific date"
    try:
        text = event.text
    except:
        text = "No text data"
    try:
        url = event.find_element_by_xpath('./a').get_attribute('href')
    except:
        url = "no url data"
    print("%s %s: %s. %s" % (next_month_text, day, text, url))

#close the browser
driver.close()
