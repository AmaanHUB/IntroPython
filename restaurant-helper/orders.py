#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Class containing Orders and related functions

from menu import Menu


class Orders(Menu):

    def __init__(self):
        # super() used to inherit from the parent class
        super().__init__()
        # initialise an order list to add to
        self.order_list = []

    # small function to add items to an order_list
    def order_item(self, *args):  # args to add as many items as like
        for item in args:
            # add a conditional here to check if item is on menu if possible
            self.order_list.append(item)

    # function to show what the customer has ordered so far
    def show_ordered(self):
        print("You have currently ordered: \n")
        for item in self.order_list:
            print(item)


# Initialise an object for testing
customer = Orders()

# Testing the methods
customer.check_menu()  # check menu from parent class
customer.show_ordered()  # to check if empty to start with
customer.order_item("chicken", "fish")  # add something to order_list
customer.show_ordered()  # check again if added to order_list
