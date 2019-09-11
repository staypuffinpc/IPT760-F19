### PURPOSE: Show how to solve the constitution challenge problems ###

##-------------------------------------------------------------------------------------------##
#### 1. read the us_constitution.txtPreview the document file into a variable in your python file

# first, define a function to get the text of an external file ##
import os # the os library allows us to access the file system
fileDir = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.abspath(os.path.join(fileDir,"../data/us_constitution.txt"))
# open the file, read it into a variable named 'constitution' as a single string and then close it ('with' will close the file automatically after it's been read)
with open(fileName,'r') as text:
    constitution = text.read() #now we have 'constitution' as a long string.

##-------------------------------------------------------------------------------------------##
#### 2. use python's string manipulation abilities to create a list of each amendment.
amendments = []

# find where to start with the first Amendment and end at the second Amendment.  We'll advance these for each Amendment

#add all the amendments to the list
def find_amendments():
    search_string = "Amendment"
    for i in range(1,28): #start at 1 so i matches the current amendment
        start = constitution.find(search_string+" "+str(i))
        end = constitution.find(search_string,start+10)
        if i == 27:
            end = len(constitution) # this accounts for a failed search on the last amendment
        amendments.append(constitution[start:end]) #append adds an item to the amendments array

# now run the function to find all the amendments
find_amendments()


##-------------------------------------------------------------------------------------------##
#### 3. You should have a list with 27 items, each with the text of the corresponding amendment.  Use a built-in python method to print out the # of items in the list.
print (len(amendments))

##-------------------------------------------------------------------------------------------##
#### 4. Print out the 5th and 10th amendments
print (amendments[4])
print (amendments[9])

##-------------------------------------------------------------------------------------------##
#### 5. Create a copy of the "amendments" list.  Name this list [your_name_amendments]

#You might try to write peter_amendments = amendments.  However, in python, this just creates a reference to the original list; so, any changes to peter_amendments would affect amendments.  There is a great discussion on stackoverflow about possible ways to copy a list in python at: https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list

peter_amendments = list(amendments)

##-------------------------------------------------------------------------------------------##
#### 6. Change the first [your_name_amendments] to all uppercase (it's the first amendment after all. Let's shout it out!)
peter_amendments[0] = peter_amendments[0].upper()
print (peter_amendments[0])

##-------------------------------------------------------------------------------------------##
#### 7. create your own function, add_amendment(), that adds a new amendment to your personal lists of amendments.

#first, define the function to always add this amendment to the end of the current list
def add_amendment(index, new_amendment_text):
    peter_amendments.insert(index, new_amendment_text)

#call add_amendment function
budget = '''Amendment 28
Congress shall henceforth and forever maintain a balanced budget. Failure to do so will result in the ineligibility to serve in public office of all congressional members for all future elections.  '''
add_amendment(28, budget)

#make sure it got added to the list
print(peter_amendments[27])

##-------------------------------------------------------------------------------------------##
#### 8. Count how many times the word, "the" appears in each amendment.  Add a second dimension to [your_name_amendments] to store this number for each amendment.  Choose a random number between 1 and 27 and print out the # of "the"s in that amendment.
current_amendment = 0
for amendment in peter_amendments:
    the_count = amendment.count("the")
    peter_amendments[current_amendment] = [peter_amendments[current_amendment],the_count]
    current_amendment += 1

import random
randAmend = random.randint(0,len(peter_amendments)-1)
print ("Amendment "+str(randAmend)+ " has the word 'the' " +str(peter_amendments[randAmend][1])+ " times.")

##-------------------------------------------------------------------------------------------##
#### 9. Come up with at least 2 other, original ways of manipulating the string of the constitution.'''

## 9a. let's get rid of all the extra whitespace in each amendment using the 'trim()' command
current_amendment = 0
for amendment in amendments:
    amendments[current_amendment] = amendments[current_amendment].strip()
    current_amendment += 1
#show that it worked
print (amendments[5])

## 9b.  let's replace "shall" with "shan't"
current_amendment = 0
for amendment in amendments:
    amendments[current_amendment] = amendments[current_amendment].replace("shall","shan't")
    current_amendment += 1
#show that it worked
print (amendments[5])
