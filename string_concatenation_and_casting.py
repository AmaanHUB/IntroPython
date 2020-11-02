#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# What is concatenation?

# first_name = "James"
# middle_name = "Bond"
# last_name = input("ID #: \n")

# Casts last_name to int
# print(type(int((last_name))))

# age = 23

# print(first_name + " " + middle_name + " " + last_name)


# Casting is used to cast integer to string or vice versa

# print(first_name + " " + middle_name + " " + last_name + " " + str(age))


name = input("Please enter your name: \n")
# print(f"Hello + {name}") # just a practice with an fstring


age = input("Please enter your age: \n")
dob = input("Please enter date of birth: \n")
address = input("Please enter first line of address with the post code: \n")

print("Hello " + name)
print("Your age is " + str(age))
print("Your date of birth is " + str(dob))
print("Your address is " + str(address))
