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

### Navigating the Tree ###
## Going down
# using tag names
tag = soup.p.b
# print(tag)
# .contents and .children
bodyTag = soup.body
# print(bodyTag.contents)

# for child in bodyTag.children:
#     print(child)

# # .descendants
# print(len(list(soup.children)))
# print(len(list(soup.descendants)))

# .string, .strings, and .strippped_strings
titleTag = soup.title
# print(titleTag.string)
#
# headTag = soup.head
# print(headTag)
# print(headTag.string)
#
# for string in soup.stripped_strings:
#     print(repr(string))

## Going up
# .parent
# print(titleTag.parent)
# # .parents
aTag = soup.a
# for parent in aTag.parents:
#     print(parent.name)



## Going sideways
# .next_sibling and .previous_sibling
# pTag = soup.p
# print(pTag)
# print(pTag.next_sibling.next_sibling.previous_sibling)
#
# # .next_siblings and .previous_siblings
# for sibling in aTag.next_siblings:
#     print(repr(sibling))



## Going back and forth
# .next_element and .previous_element
print(aTag.next_element)
print(aTag.previous_element)
# .next_elements and .previous_elements
for element in aTag.next_elements:
    print(repr(element))
