#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Creating a Python class as a child class of our Snake class

from snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True  # always remember the self.
        self.venom = False
        self.two_lungs = True


# creating functions for our python class

    def digest_large_prey(self):
        return "Unhinge that massive jaw!"

    def climb(self):
        return "Climb climb"

    def constrict(self):
        return "Death hug!"


# creating an object of our Python class
python_object = Python()

print(python_object.breathe())  # function from our Animal class
print(python_object.hunt())  # function from our Reptile class
print(python_object.use_tongue_to_smell())  # function from our Snake class
