### PURPOSE: demonstrate how to create functions, slice strings, use conditionals and loops within python ###

const = '''We the People of the <a href='https://us.gov'>United State</a>, in Order to form a more perfect Union,
establish Justice, insure domestic Tranquility, provide for the common
defence, promote the general Welfare, and secure the Blessings of Liberty to
ourselves and our Posterity, do ordain and establish this Constitution for the
United States of America.'''

# print the first char of const
print(const[0])

#print the first 10 chars of const
print(const[0:9])

#print starting from the 150th character
print (const[150:])

#print the last 10 characters
print (const[-10:])

#print
print (const[::-1])

#find the index of the word "establish"
word = const.find("establish")
print ("establish is first found at "+str(word))

##pseudocode to find a url
#1. find the index of https://
#2. read until the end of the address (single quote)

start = const.find("https://")
end = const.find("'",start+9)
print (end)
print (const[start+8:end])

## create a function ##
def avg(num1, num2):
    kai = (num1 + num2)/2
    print (kai)

avg(45,89)
avg(5,4)
avg(56,1000)
avg(2,2)
avg(90,78)

#conditionals in Python
if (5 > 6) :
    print("hello word!")
else:
    print("what a cruel world!")

if (5 == 6) :
    print ("looks like they're the same")
elif (6 < 5):
    print ("wwow, that's really weird that 6 is less than 5")
else:
    print ("that makes sense")

# loops in Python
for i in range(0,10):
    print(i)

#while loops
count = 100
while count <= 110:
    print (count)
    count = count +1
