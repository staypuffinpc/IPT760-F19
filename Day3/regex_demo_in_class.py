##### PURPOSE: To demonstrate how to use regular expressions with python for string searching ###

#import needed libraries
import os
import re

## first, define a function to get the text of an external file ##
def getFile(filename,relativePath):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    fileName = os.path.abspath(os.path.join(fileDir,relativePath+filename))
    # open the file, read it into a variable named 'constitution' as a single string and then close it ('with' will close the file)
    with open(fileName,'r') as text:
        fileText = text.read() #now we have 'constitution' as a long string.
    return fileText

constitution = getFile('us_constitution.txt','../data/')
tip = getFile('about_tip.html','../data/')

##### Regex basics #####

first_num = re.search("About TIPS",tip)

if (first_num):
    print ("Yes, that string exists in this text")
else:
    print ("Sorry, I couldn't find that string in this text")

#find alphanumeric sequence \w

#find numbers \d

#find white space \s

#find sequences starting with any of a set of letters []

# wildcard characters . + and *

#optional ?

#beginning and ending ^ and $

#specific # of characters {}

# groups ()

#either/or using a pipe |
