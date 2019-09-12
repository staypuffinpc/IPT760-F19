import class_demo_2 as info

#old string formatting
#print ("Hello there %s, %s, %s."(info.dummy, info.smarty_pants, info.smart_alec))

#using the .format() method
print ("Hello there {}, {}, {}.".format(info.dummy, info.smarty_pants, info.smart_alec))

#using f at the beginning
print (f"Hello there {info.dummy}, {info.smarty_pants}, {info.smart_alec}.")

print (info.getMean(23, 25))

from class_demo_2 import getMean as mean

print(mean(5,10))

### Demonstrate how to create a class ###
class Pet:

    alive = "yes"

    def __init__(self, color, type, name, food, legs, sound, amount=3 ):
        self.color = color
        self.type = type
        self.name = name
        self.food = food
        self.legs = legs
        self.sound = sound
        self.amount = amount

    def _chew_(self,times=3):
        for i in range(0,times):
            print("chewing")

    def feed_pet(self,amount):
        for i in range(0,amount):
            self._chew_()
            print (f"I like {self.food}")
        print(self.sound)

#####-----------------#######

myPet = Pet("red", "cat", "nip", "Lasagna", 5, "meow!")
yourPet = Pet("blue","dog","Rafa","bread",4,"woof!")
print(myPet.color, myPet.sound, myPet.name, myPet.food)
print(yourPet.color, yourPet.sound, yourPet.name, yourPet.food)

myPet.feed_pet(3)
yourPet.feed_pet(yourPet.amount)
print(yourPet.alive)
print(myPet.alive)

Pet.alive = "no"
print(yourPet.alive)
print(myPet.alive)

myPet.alive = "yes"

print(yourPet.alive)
print(myPet.alive)

Pet.alive = "undead"

print(yourPet.alive)
print(myPet.alive)
