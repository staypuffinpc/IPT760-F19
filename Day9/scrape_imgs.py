### PURPOSE:  to demonstrate how to interact with web pages using Selenium web driver ###

## import needed libs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #to add delays
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import os
import wget
import urllib #to be able to download images

#we need these next 3 methods in order to wait until the presence of a particular element exists
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = "pjr3"
#use this so you can type in a password and not have to store it on your system
password = getpass.getpass("BYU password?")

driver = webdriver.Chrome()
driver.get("https://my.byu.edu")

#click on the "Sign in" button
time.sleep(5)
login_btn = driver.find_element_by_xpath('//*[@id="portalCASLoginLink"]/span')
login_btn.click()

#input user and pass into the CAS login
username_input = driver.find_element_by_id("username")
username_input.send_keys(user)

password_input = driver.find_element_by_id("password")
password_input.send_keys(password)

#click on the submit button
driver.find_element_by_name("submit").click()

#check the current url
# print("current URL: ",driver.current_url)


# try:
#     dual_login = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located(driver.find_element_by_css_selector('button.auth-button'))
#         )
#     dual_login.click()
# finally:
#     driver.quit()

#dual authentication page.  Click on the "send me a push" button
#driver.find_element_by_css_selector('button.auth-button').click()

#we need to put a "wait" timer b/c of dual authentication
time.sleep(15)

#we should now see we are logged in.  Go ahead and redirect to the page we want within the system directly
driver.get("https://y.byu.edu/ry/ae/prod/class_schedule/cgi/instructorSchedule.cgi")

#navigate to "work" button, open menu, then click on "class rolls".  execute all of this as an ActionChain
# action = ActionChains(driver)
# work_btn = driver.find_element_by_xpath('//*[@id="Pluto_28_u20l1n15_25109_menu"]/li[4]/a')
# class_rolls_btn = driver.find_element_by_xpath('//*[@id="Pluto_28_u20l1n15_25109_menu"]/li[4]/a//li/a[contains(@href,"instructorSchedule")]')
# action.move_to_element(work_btn)
# action.perform()
# time.sleep(2)
# action.move_to_element(class_rolls_btn).click()
# action.perform()


# click on the "class roll" link
link = driver.find_elements_by_xpath('//*[@id="Content"]/table[2]//a')
# //*[@id="Content"]/table[2]//td[21]/a
link[2].click()

time.sleep(3)
#now a new window should be open.  Navigate to that window if not already There.  Should be 'classRoll'
driver.switch_to.window("CLASSROLL")

#click on the "picture page" link
# picture_page = driver.find_element_by_xpath('//table[2]//a[1]')
# picture_page.click()
# driver.get("https://y.byu.edu/ry/ae/prod/class_schedule/cgi/classRoll.cgi")

# time.sleep(6)
print("current page: ",driver.current_url)
#let's create an action chain to navigate to the link, hover over it, and then click on it
picture_page_link = driver.find_element_by_xpath("//a[contains(@href, 'picture')]")

ActionChains(driver).move_to_element(picture_page_link).click().perform()

#now that we're finally on the page with the images, we need to:
## 1. create a list of dicts: {url: image urls, name: student name}
student_imgs = driver.find_elements_by_xpath("//span/img")
for data in student_imgs:
    print(data.get_attribute('src')) #notice that these are all absolute, even though they're coded as relative in the HTML!

student_names = driver.find_elements_by_xpath("//span/a")
# for name in student_names:
#     print(name.text)

#create a list with all the info
students = []
for i in range(len(student_imgs)):
    this_student = [student_imgs[i].get_attribute('src'), student_names[i].text]
    students.append(this_student)

#get course title
class_name = driver.find_element_by_xpath("//h1").text
class_name = class_name.strip().replace(" ","_")
print("Class: ",class_name)

## 2. create a folder for this class (preferrably with the class name, which you'll need to get on the screen)

# detect the current directory
curr_path = os.getcwd()
print("current folder: ",curr_path)
new_path = curr_path+"/"+class_name

#create a new directory to store the photos
if os.path.isdir(new_path) is False:
    try:
        os.mkdir(new_path)
    except OSError:
        print("Could not create new directory")
    else:
        print("Successfully created the directory")
else:
    print("directory already exists")

## 3. for each dict in the list, download the img at url and name it name
from pathlib import Path #this will allow me to create paths that can be read on mac or windows!
data_folder = Path(new_path)

for i in range(len(students)):
    try:
        this_student = students[i][1]+".png"
        with open(data_folder / this_student,'wb') as file:
            file.write(student_imgs[i].screenshot_as_png) #note that you need to use the object and not just the source for this
    except :
        print(f"could not save image {students[i][1]}")

#close up shop
driver.quit()
