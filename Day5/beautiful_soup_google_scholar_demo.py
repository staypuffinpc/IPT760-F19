#### PURPOSE: To demonstrate how to use the BeautifulSoup library to scrape data from google scholar

#import needed libraries
import re
from bs4 import BeautifulSoup
import requests

#get the data for a specific search on google scholar
search_term = "Charles+Graham"
start_results = 1
page = requests.get("https://scholar.google.com/scholar?start=20&q=%22Charles+Graham%22&hl=en&as_sdt=0,100")

print(page)

## now turn fetched page into "soup"
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
# readable (i.e., "pretty" soup)
# print(soup.prettify())

first_link = soup.li.a
print(first_link)

print (first_link.string)

#print the names of all tags on a web page
bodyTag = soup.body

for child in bodyTag:
    print(child.string)

#all tags
all_tags = soup.descendants
print(len(list(all_tags)))
for child in bodyTag.descendants:
    print (child.name)

for child in bodyTag.children:
    print ("These are my children",child.stripped_strings)
