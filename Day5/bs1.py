#### PURPOSE:  Demonstrate how to use beautiful soup to scrape info from html pages ####

## import needed libraries
import requests

## download a single page
page = requests.get("http://books.toscrape.com/")

# check the website response
print(page)

#examine the html
# print(page.content)

### beautiful Soup ####
from bs4 import BeautifulSoup

## creating an instance of the BeautifulSoup class
soup = BeautifulSoup(page.content, "html.parser")

##print out the Soup
# print(soup.prettify())

### BS4 objects ###

##tags — elements of an HTML page
tag = soup.li.a
print(tag)

#name of tag
print(tag.name)

#tag attributes
print(tag.attrs)

#Navigable string — the stuff inside of a tag
print(tag.string)
