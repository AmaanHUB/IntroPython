#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Class containing methods and details related to the menu


class Menu():

    # initialise the class
    def __init__(self):
        # create a menu as a list, though a dictionary would work for prices
        self.menu = ["chicken", "fish", "steak",
                     "quorn burgers", "chips"]

    # function to loop through menu and print it out for the user
    def check_menu(self):
        # for loop through self.menu
        print("Please see below for the items that we offer: \n")
        for item in self.menu:
            print(item)  # remember not to use return, as only outputs 1st


# Initialisation of an object Menu()
# test = Menu()

# Print out menu items test
# test.check_menu()
