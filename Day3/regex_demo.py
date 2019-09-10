##### PURPOSE: To demonstrate how to use regular expressions with python for string searching ###

## first, let's get some data from an external file.  I'll use the U.S. constitution #
import os
fileDir = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.abspath(os.path.join(fileDir,'../data/us_constitution.txt'))
# open the file, read it into a variable named 'constitution' as a single string and then close it ('with' will close the file)
with open(fileName,'r') as text:
    constitution = text.read().replace('\n','') #now we have 'constitution' as a long string.
print (constitution[:100])
##### Regex basics #####
import re

first_Article = re.search("USCons*", constitution)
print (first_Article)

doolittle = "The rain in Spain falls mainly on the plain"
#x = re.search("ain*",doolittle)

z = re.findall("ain{0}",constitution)
#print (z)

a = re.findall("Article|Section",constitution)
#print(a)
#split the original using a pattern as the delimitter
s = re.split("^r*",doolittle)

#find all numbers in the constitution
nums = re.findall("[0-9]+",constitution)
#print(nums)

#find all 2-digit numbers in the constitution
doubles = re.findall("[0-9]{2}",constitution)
#print(doubles)

#find all instances of words with US the do not start or end with "US"
us = re.findall("us\B",constitution)
#print(us)

htmlStuff = '''<div class="PromoFullWidth-Large-container container-fixed">
      <div class="PromoFullWidth-Large-content">


    <div class="PromoFullWidth-Large-title promo-title-large ">
        <a class="Link" href="https://byuphoto.exposure.co/mangolia" target="_blank">Life-Saving Design<svg class="icon icon-external-link"><use xlink:href="#icon-external-link"></use></svg></a>
    </div>



    <div class="PromoFullWidth-Large-description  promo-description">The humanitarian arm of The Church of Jesus Christ of Latter-day Saints asked BYU students to address a toxic pollution problem in Mongolia.


    </div>




    <div class="PromoFullWidth-Large-cta promo-cta">



            <a class="btn " href="https://byuphoto.exposure.co/mangolia" target="_blank"> Watch the video </a>



    </div>


      </div>
    </div>'''

#replace all the white space in htmlStuff with __
repl = re.sub("\s","_",htmlStuff)
#print(repl)

htmlDir = os.path.dirname(os.path.realpath('__file__'))
htmlName = os.path.abspath(os.path.join(fileDir,'../data/theories.html'))
# open the file, read it into a variable named 'constitution' as a single string and then close it ('with' will close the file)
with open(htmlName,'r') as text:
    htmlSample = text.read() #now we have 'constitution' as a long string.

#print(htmlSample)

#get just the text between  carats by using parentheses
# links = re.findall("<a href=.*>(.*)</a>",htmlSample)
# print ("There are "+str(len(links))+" links in this html file.")
# for link in links:
#     print (link)

#we can even nest groups and return a tuple of information.  Let's use the same search to get the links, but also to get the names of the researchers in the links
links_w_researchers = re.findall("<a href=.+>(.*)</a>",htmlSample)
print (len(links_w_researchers))
for link in links_w_researchers:
    print (link)

links2 = re.search("<a href=.+>(.*)</a>",htmlSample)
print(links2.group())
