#### Solutions for 6 different challenges on classes and regex ####

# [ 2pts] Write a python class that takes the width and height of a rectangle as input.  Write methods to calculate the hypotenuse of a rectangle's diagonal measurement, the perimeter, and the area of the rectangle.
import math

class rectStuff:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_hypotenuse(self):
        return math.sqrt(self.width**2+self.height**2)

    def get_perimeter(self):
        return self.width*2 + self.height*2

    def get_area(self):
        return self.width*self.height

rect1 = rectStuff(3,4)
print(f"hypotenuse: {rect1.get_hypotenuse()}")
print(f"perimeter: {rect1.get_perimeter()}")
print(f"area: {rect1.get_area()}")


# [2 pts] Write a python class that takes a string as input.  Then, create two methods.  One called, "Uppers()" that will create a list of all words in that string that begin with an upper-case; and another called, "Enders()" that creates a list words that end a sentence.

class textFun:

    def __init__(self, someString):
        self.string = someString

    def uppers(self):
        #need to get each word in self.string and capitalize it
        words = self.string.split()
        uppers = ""
        for word in words:
            uppers += word[0].upper()+word[1:]+" "
        return uppers

    def lowers(self):
        #need to get each word in self.string and capitalize it
        words = self.string.split()
        uppers = ""
        for word in words:
            uppers += word[0].lower()+word[1:]+" "
        return uppers

text1 = textFun("this, is a text without any upper case lettering.")
print (text1.uppers())

text2 = textFun("THIS IS A TEXT WITH ALL UPPERCASES LETTERS TO START WITH.  I PROMISE.")
print (text2.lowers())

#[3 pts] Write a python class that will change the words in a string to pig-latin.  For example, the string, "I am Peter Rich," would be "Iay amay eterpay ichray" (see http://www.worldwidewords.org/weirdwords/ww-ixn1.htm
class pigLatin:

    def __init__(self, yourString):
        self.string = yourString


# [3 pts] Write a python class that extracts all the numbers from a string and converts them to their word form.  There should be at least two different methods.  One for printing the list of all numbers, and another for printing the list of those numbers in word form.



# [3 pts] Write a python class that creates several methods of finding specific textual sequences in a string.  For example, the method get_emails() would get all the emails in that text, get_dates() might get all the dates, and so on.


# [4 pts] Write three python classes: Assignment, Student, and Grades.  Assignment should create a basic classroom assignment and have methods for updating that assignment.  Student should create a basic student and have methods for updating the student's information.  Grades, should take a student and an assignment object and create an entry in a list for that student turning in that assignment with a specific date, grade, and teacher feedback.
