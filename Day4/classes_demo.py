### PURPOSE: To demonstrate how to create an work with classes in Python ###

#create a class in the same document
class Pet:
    ''' A virtual pet just for you '''

    owner = "Peter" #class variable shared by all instances

    def __init__(self, type="dog", age=0, name="Fido"): #must always include "self" in class methods
        self.type = type
        self.age = age
        self.fur = True
        self.legs = 4
        self.fixed = False
        self.name = name

    def makeNoise(self,sound):
        print("%s! %s!" % (sound, sound))

myPet = Pet("dog",9,"Rafa")
myPet.makeNoise("bark")
print("My pet is named %s and it is %d years old.  It is a %s" % (myPet.name, myPet.age, myPet.type))
print("My pet's owner is: "+myPet.owner)

yourPet = Pet()
print("Your pet is named %s. It is %d years old.  It is a %s"%(yourPet.name, yourPet.age, yourPet.type))

anotherPet = Pet("fish")
print("Another pet is named %s. It is %d years old.  It is a %s"%(anotherPet.name, anotherPet.age, anotherPet.type))


#change the class variable
myPet.owner = "Bob"
print("myPet's owner",myPet.owner)
print ("yourPet's owner",yourPet.owner)


#Delete properties or entire objects using the "del" keyword.  Be careful when using this.
del myPet.name
# print("My pet is named "+myPet.name)

del myPet
# print(myPet.owner+" is the owner of my Pet.")

## IMPORT class from external file ###
from assignment import Assignment

homework1 = Assignment()
homework1.title = "All about me"
due = homework1.due.strftime("%B %d, %Y")
print("%s is due on %s and is worth %d points." % (homework1.title, due, homework1.value))
