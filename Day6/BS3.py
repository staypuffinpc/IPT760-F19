htmlDoc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

### Beautiful Soup ###
## import the Library
from bs4 import BeautifulSoup

## creating an an instance of the Beautiful Soup class
soup = BeautifulSoup(htmlDoc, "html.parser")

### SEARCHING ###
## find() and find_all()
# print(soup.find("p"))
# print(soup.find_all("p"))
# # filters as a strings
# print(soup.find("b"))
# # filters as a regex
import re
#
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
# # filter as true
# for tag in soup.find_all(True):
#     print(tag.name)
#
# # filters as a list
# print(soup.find_all(["a", "b"]))
#
# # filters as a function
# def has_class_but_no_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")
#
# print(soup.find_all(has_class_but_no_id))

## additional agruments of find(name, attrs, recursive, string, **kwargs) and find_all(name, attrs, recursive, string, limit, **kwargs)
# name

# attrs
# print(soup.find("a", attrs={"href": re.compile("elsie")}))
# # recursive
# print(soup.html.find_all("title"))
# print(soup.html.find_all("title", recursive=False))
# # string
# print(soup.find_all(string="Elsie"))
# print(soup.find_all("a", string="Lacie"))
# # limit
# print(soup.find_all("a", limit=2))
# kwargs as arguments
# print(soup.find_all(id="link2"))

## searching by CSS class
# print(soup.find_all(class_="sister"))

## find_parent() and find_parents()
# lacie = soup.find(string="Lacie")
# print(lacie.find_parent("p"))

# find_next_sibling() and find_next_siblings()
# aTag = soup.find("a")
# print(aTag.find_next_sibling(id="link3"))

## find_previous_sibling() and find_previous_siblings()
# lastATag = soup.find(id="link3")
# print(lastATag.find_previous_sibling(id="link1"))

## find_next() and find_all_next()
# body = soup.find("body")
# print(body.find_next(class_="story"))

## find_previous() and find_all_previous()
# aTag = soup.find('a')
# print(aTag.find_previous("b"))


# ## SoupStrainer class
# from bs4 import SoupStrainer
#
# onlyATags = SoupStrainer("a")
#
# print(soup.prettify())
# print(BeautifulSoup(htmlDoc, "html.parser", parse_only=onlyATags).prettify())




### MODIFYING THE HTML ###
# soup1 = BeautifulSoup("<b class = 'boldest'>Extremely bold</b>")
# tag = soup1.b
#
# tag.name = "blockquote"
# tag["class"] = "verybold"
# print(tag["class"])

## append()
# soup.title.append(" is great!")
# print(soup.title)
#
# ## extend()
# soup.a.extend([" ", "S", "m", "i", "t", "h"])
# print(soup.a)

## NavigableString and new_tag()
# from bs4 import NavigableString
#
# newSoup = BeautifulSoup("<b></b>", "html.parser")
# tag = newSoup.b
# tag.append("Hello")
# newString = NavigableString(" world!")
# tag.append(newString)
# print(tag)

# newTag = newSoup.new_tag("a", href="http://example.com")
# tag.append(newTag)
# print(tag)

## insert(), insert_before(), and insert_after()
# tag.insert(1, "test")
# print(tag.contents)
# newerSoup = BeautifulSoup("<b>stop</b>", "html.parser")
#
# tag = newerSoup.new_tag("i")
# tag.string = "Don't"
#
# newerSoup.b.string.insert_after(tag)
# print(newerSoup)

## clear()
soup.a.clear()
# print(soup.a)

## extract()
lacie = soup.find("a", id="link2").extract()
# print(soup.find_all("a"))
# print(lacie)

## decompose()
tillie = soup.find("a", id="link3").decompose()
# print(soup.find_all("a"))
# print(tillie)

## replace_with()
# newSoup = BeautifulSoup("<a href='http://example.com'>I linked to <i>example.com</i></a>", "html.parser")
# aTag = newSoup.a
#
# newTag = newSoup.new_tag("b")
# newTag.string = "example.net"
# aTag.i.replace_with(newTag)
#
# print(aTag)
## wrap() and unwrap()
# newSoup = BeautifulSoup("<a href='http://example.com'>I linked to <i>example.com</i></a>", "html.parser")
# aTag = newSoup.a
# aTag.i.wrap(newSoup.new_tag("b"))
# print(aTag)
#
# aTag.i.unwrap()
# print(aTag)

## smooth()
newSoup = BeautifulSoup("<p>A one</p>", "html.parser")
newSoup.p.append(", a two")

newSoup.smooth()
print(newSoup.p.contents)
print(newSoup.p.prettify())




### OUTPUT ###
## using .prettify() to get a nicely formatted OUTPUT
