#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# What are data types?

# Boolean gives us outcome in true or false

# a = True
# b = False
#
# print(a == b)
#
# print(a != b)
#
# print(a >= b)

greetings = "Hello World!"

print(greetings.isalpha())
# checks if all letters in our string are letters

# how can we check if the string is lower case
print(greetings.islower())

print(greetings.startswith("H"))

print(greetings.endswith("!"))


print(input("Add word to test: \n").isalpha())


# None, is a keyword

print(bool(None))
