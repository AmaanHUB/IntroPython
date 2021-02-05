#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Creating a reptile class as a child of Animal class

from animal import Animal
# Syntax to import files and classes:
# from file import class


class Reptile(Animal):
    def __init__(self):
        # super key word used to inherit everything from parent class
        super().__init__()
        self.cold_blooded = True
        # an animal that is descended from an ancestor with 4 limbs
        self.tetrapod = True
        self.heart_chambers = [3, 4]

    # creating functions for our reptile class
    def seek_heat(self):
        return "Brr, better find somewhere warm"

    def hunt(self):
        return "Working hard to catch a meal..."

    def use_venom(self):
        return "If I've got it, I'm using it"


# Create an object of our Reptile class to utilise OOP functionalities
# reptile_object = Reptile()
#
# print("Below is inherited from Animal parent class: \n")
# print(reptile_object.breathe())  # print method from parent class
# print(reptile_object.eat())
#
#
# # print methods from this class
# print("Below is printing methods from our current Reptile class: \n")
# print(reptile_object.seek_heat())
# print(reptile_object.hunt())
# print(reptile_object.use_venom())


