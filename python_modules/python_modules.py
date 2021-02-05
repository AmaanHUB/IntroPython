#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Python modules

# Built in functions

# import is the key word we use to call modules from Python libraries

# first iteration
# we have a random method in python library which we use by importing
# from random import random
# from math import math
#
# # generates float number between 0 and 1
# # Need to specify the name of the class then the method
#
# # class.method(variable_maybe)
# print(random.random())
#
#
# num_float = 15.23
# print("Floor method rounds the figure to the lower bound")
# print(math.floor(num_float))
#
#
# print("Ceil method rounds the figure to the upper bound")
# print(math.ceil(num_float))
#
#
#
# # Task
# # get user input of a float number
# # check if number is lower than .50 then round to lower end
# # if higher than .50 round to higher end
#
# number = float(input("Choose float number: "))
# print(f"Original number: {number}")
#
# # modulo 1 helps find the number after the decimal point essentially
# # easy to do and efficient without importing the decimal library
# if number % 1 < 0.5:
#     rounded_number = math.floor(number)
# else:
#     rounded_number = math.ceil(number)
#
# print(f"Rounded number: {rounded_number}")
#
# # Second interation
# # Can do the import either way
# # import random
# # import math

# to find out the system related information
# based on information provided, we can handle the user request
import os
import math, datetime, sys  # can import more than 1 in one line

# # os.getcwd() ONLY WORKS on Linux/Mac
# working_dir = os.getcwd()  # gets the directory that the file is in
#
# print(working_dir)
#
# print(os.uname())  # works on Linux and Mac, same as uname command pretty much
#
# # Counting no. of CPUs available to our OS/system
# print(os.cpu_count())
#
#
# # Show current time
# print(datetime.datetime.today())  # the second datetime appears to be a polymorphism, but needed
#
# # Show the path
# print(sys.path)  # is an attribute, not a function


# Customised method using built in sys methods
def current_system_path():
    print("This is your current directory: ")
    return sys.path

print(current_system_path())
