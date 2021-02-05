#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Creating an Animal Class as a PARENT/BASE/SUPER class


class Animal:

    def __init__(self):  # initialising the Animal class
        self.alive = True
        self.spine = True  # assume all have spine for now
        self.lungs = True
        self.eyes = True

    # create behaviours as functions/methods
    def breathe(self):
        return "Just keep breathing"

    def move(self):
        return "Up, down, left, right"

    def eat(self):
        return "Nom, nom, nom"

    def procreate(self):
        return "Find partner/s"


# instantiate our class/create an object

# cat = Animal()  # creating an object of Animal class
# Abstracted eat() method fro our parent class
# cat as child has instantiated everything from Animal/Parent class
# print(cat.eat())
