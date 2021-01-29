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

# Declaring strings with single and double quotes
single_quotes = 'single_quotes\'wow\''  # can make readability and coding harder than double quotes

double_quotes = "double quotes wow"

# String slicing - why
# Indexing in Python starts as 0
greetings = "Hello World!"
print(greetings[6:])  # leaving the second value blank does to the end of the string


white_spaces = "lot's of spaces at the end          "
print(len(white_spaces))
print(len(white_spaces.strip()))
# strip() deletes all the spaces at the end of string

# count() method counts the number of times any word is used in a string
example_text = "lots of text with some text"

print(example_text.count("text"))

print(example_text.replace("with", "chicken"))  # replace the 'with' with 'chicken'

# capitalize() makes the first letter a capital, everything else lower
print(example_text.capitalize())
print(example_text.lower())
print(example_text.upper())

# fstring
print(f"{example_text} testing")
