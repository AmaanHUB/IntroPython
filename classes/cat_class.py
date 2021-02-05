#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Creating a cat class

# One function that returns 'MEOW!'


# create 2 class level variables
# create 3 objects
# display all information with each object
# change the class variable values in each object and display

# pseudo code each block of code

class Cat:
# created Cat class
    def meow(self):
        # turns the string "MEOW!!" when called
        return "MEOW!!"

# 2 class level variables
    animal_kind = "Feline"  # class level variable for type of animal
    colour = "white"  # class level variable for cat colour


# Create 3 objects
prada = Cat()  # instantiate object called prada of class Cat
muffin = Cat()  # instantiate object called muffin of class Cat
trixie = Cat()  # instantiate object called trixie of class Cat

print("Information for Prada: \n")
print(prada.animal_kind)
print(prada.meow())
print(prada.colour)
prada.colour = "black"
print(prada.colour)

print("Information for Muffin: \n")
print(muffin.meow())
muffin.colour = "mixed"
print(muffin.colour)


print("Information for Trixie: \n")
print(trixie.meow())
trixie.colour = "tabby"
print(trixie.colour)
