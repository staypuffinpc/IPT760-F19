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

first_num = re.search("Amend.*",constitution)
print (first_num)
# print (first_num.group())
if first_num:
    print ("Yes,that string is in the text!")
else:
    print ("Sorry, I can't find that string")


#find alphanumeric sequence \w
all_nums = re.findall("\W",constitution)
#print (len(all_nums))
#print (all_nums)

#find numbers \d
all_nums = re.findall("\d.+", constitution)
print (len(all_nums))
#print (all_nums)

#find white space \s
white_space = re.findall("\s",constitution)
print (len(white_space))
#print (white_space)

#find sequences starting with any of a set of letters []
minimal_pair = re.findall("[bmfch]at",constitution)
print (minimal_pair)

more_pairs = re.findall("\d*\s?shall\sa[a-z]+",constitution)
print (more_pairs)

# wildcard characters . + and *
x = re.findall("[^tT]he", constitution)
print(x)

#optional ?

#beginning and ending ^ and $
beginning = re.findall("^Article",constitution)
print (beginning)

#specific # of characters {}

# groups ()

#either/or using a pipe |
