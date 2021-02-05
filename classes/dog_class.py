#! /usr/bin/env python
# -*- coding: utf-8 -*-
#  Classes, Objects, And Instantiation

# How to create a class?

# Syntax: class Class_name
# starts with capital letter always

# Classes are a way of bringing data and functionality together


class Dog:

#     animal_kind = "Canine is running"
# defining class variable

    def __init__(self, name, colour):  # initialise Dog class
        self.name = name
        self.colour = colour
        self.animal_kind = "Canine"  # instialisation of the class

    def bark(self):
        # self refers to current class
        return "woof"

# EVERYTHING COMMENTED OUT WAS BEFORE __init__ METHOD CREATED

# to execute a class, we have to create an object of this class
# toffee = Dog()  # creating an object/instance in our Dog class
#
# print(toffee)  # would output memory location of object

# # print(toffee.animal_kind)
# # print(toffee.bark())


# toffee.animal_kind = "Big Dog"  # only animal_kind is changed for toffee object
# print(toffee.animal_kind)

# basil = Dog()  # instantiating basil in Dog class
# print(basil.animal_kind)
# print(basil.bark())


fido = Dog("fido", "brown")  # instantated an object of a Dog class
print(fido.name)
print(fido.colour)
print(fido.bark())
print(fido.animal_kind)
