#### PURPOSE: show how to use BeautifulSoup to scrape web page data ####

## import needed libraries
from bs4 import BeautifulSoup
import requests

#fetch all the data from a single URL
url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C45&q=%22Randall+Davies%22&btnG="
page = requests.get(url)

#turn the page into Soup
soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())

first_link = soup.a
# print(first_link)

#get the name of the first link
# print(first_link.attrs)

bodyTag = soup.body
# for child in bodyTag.children:
#     print(child.name)
#
# for child in bodyTag.descendants:
#     print(child.name)

print(len(list(bodyTag.descendants)))

#print the text of all the descendants of body
# for child in bodyTag.descendants:
#     print(child.string)

special_link = bodyTag.li.a
print("Grandma:",special_link.parent)

print("Sister: ",special_link.next_element)
