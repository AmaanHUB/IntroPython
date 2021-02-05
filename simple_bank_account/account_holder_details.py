#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Account holder details in a class

# reminder that all classes are named in camel case


class AccountHolderDetails:
    # Initialise AccountHolderDetails class
    def __init__(self, name, address, age):  # adding name, address, age as parameters
        # declaring variables as private
        self.__name = name
        self.__address = address
        self.__age = age

    # Gets the name
    def get_name(self):
        return self.__name

    # Setter for the name, as people can change their name
    def set_name(self, new_name):
        self.__name = new_name

    # Getter for the address
    def get_address(self):
        return self.__address

    # Setter for address, as people can move
    def set_address(self, new_address):
        self.__address = new_address

    # Getter for the age
    def get_age(self):
        return self.__age

    # Setter for the age, hopefully increment into something
    # that automatically increases age at some point
    def set_age(self, new_age):
        self.__age = new_age
