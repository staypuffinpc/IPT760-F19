# first things first: import libraries
from bs4 import BeautifulSoup
import requests

# second: create BeautifulSoup; website http://quotes.toscrape.com/
page = requests.get("http://quotes.toscrape.com")

soup = BeautifulSoup(page.content, "html.parser")

### CHALLENGES ###
# Find tags by a CSS class in an HTML document.
# for tag in soup.findAll("a", class_="tag"):
#     print(tag.string)

# Change a tag's contents by replacing with a different string.
# firstQuote = soup.find("span", class_="text")
# firstQuote.string.replace_with("I think, therefore I am.")
# print(firstQuote)

# Add to a tag's contents in an HTML document.
# h1Tag = soup.find("h1").find("a")
# h1Tag.append(" and Stuff")
# print(h1Tag)

# Insert a tag or string immediately before and after a certain tag or string.
quotes = soup.findAll("span", class_="text")
lastQuote = quotes.pop()
lastQuote.string.insert_before("Steve Martin said, ")
print(lastQuote.prettify())
lastQuote.smooth()
print(lastQuote.prettify())
lastQuote.string.insert_after(" and people thought it was funny.")
print(lastQuote)

# Create a function that replaces any tag that has a "b" in it with the word "foobar".
