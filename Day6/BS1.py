### Requests Library in order to download a webpage ###
## import the Library
import requests
## downloading a sample website
page = requests.get("http://books.toscrape.com/")
# checking the website response
print(page)
# looking at the HTML
# print(page.content)

# understanding what HTML is, how it's different from CSS & Javascript
# Tags, properties, classes, ids
# relationship tree

### Beautiful Soup ###
## import the Library
from bs4 import BeautifulSoup

## creating an an instance of the Beautiful Soup class
soup = BeautifulSoup(page.content, "html.parser")
## printing out the Soup
# print(soup.prettify())
### Kinds of Objects ###
## Tags - elements of an HTML page
tag = soup.li.a
print(tag)
# name #
print(tag.name)
# attributes #
print(tag.attrs)

## Navigable String - the stuff inside of a tag
# becomes a BS object
print(tag.string)
print(type(tag.string))
# but can become a regular Python string with str() for use outside of BS
pyTag = str(tag.string)
print(pyTag)
print(type(pyTag))

## Comments (or other special strings) - comments within HTML, just a special type of NavigableString
# mostly can ignore
