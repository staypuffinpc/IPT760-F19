#### Working with and manipluting strings in python ###

#sample string to work with
article1S2 = '''The actual Enumeration shall be made within three Years after the first Meeting of the Congress of the United States, and within every subsequent Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until such enumeration shall be made, the State of New Hampshire shall be entitled to choose three, Massachusetts eight, Rhode Island and Providence Plantations one, Connecticut five, New York six, New Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South Carolina five and Georgia three.
'''
#split the text into a list with each word
words = article1S2.split()
for word in words:
    print(word)

#how many words are in the list?
print("There are "+str(len(words))+" words in this list.")

#replace each "The" with "Yikes!"
yikes = article1S2.replace('The','Yikes!')
print(yikes)

#upper case (.lower() for lower case)
print(article1S2.upper())

#strip: removes  leading characters from both ends
print(article1S2.lstrip())

#check if all characters are alphabetic
print("All alphabetic? ",article1S2.isalpha())

#check if the first character is a space
print("Is first character a space?",article1S2[0:1].isspace())
print("Is LAST character a space?",article1S2[-1:].isspace())


#reverse the list:  nothing before 1st colon mean start at the beginning; nothing after first colon means go to the end.
print(article1S2[::-1])

#find the index of the first occurrence of "Georgia"
print(article1S2.index("Georgia"))

#count how many times a word occurs
print(article1S2.count("the"))

#find the first index of a string
print(article1S2.find("New York"))

#print the last 3 characters
print(article1S2[-3:])
