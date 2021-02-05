#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# class to run a naan factory

class NaanFactory:

    # Initialises class with booleans whether flour and water available
    # next iteration should make them boolean
    def __init__(self, water_available, flour_available):
        self.water_available = water_available
        self.flour_available = flour_available

    # method to make the dough
    def make_dough(self):
        # checks if water and flour are present
        if self.water_available is True and self.flour_available is True:
            # returns true if both are present
            return True
        else:
            return False

    # method to bake dough based upon presence of dough
    def bake_dough(self):
        # if make.dough() returns True, then this method shall too
        if self.make_dough() is True:
            return True
        else:
            return False

    # method to essentially run the factory
    def run_factory(self):
        # if both functions return true, then return true
        if self.make_dough() and self.bake_dough():
            return True
        else:
            return False

## second iteration starting

#     @property
#     def water_available(self):
#         return self.water_available
#
#     @water_available.setter
#     def water_available(self, true_or_false):
#         true_or_false = str(input("Is water available at the factory?"))
#         true_or_false.capitalize()
#         if true_or_false == "True":
#             return self.water_available is True
#         elif true_or_false == "False":
#             return self.water_available is False
#         else:
#             print("Error, not correct value, try again")




