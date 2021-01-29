#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

name = input("What is your name? ")
DOB = input("What is your date of birth? ")
age = input("What is your age? ")

print(f"Name: {name}\nDate of birth: {DOB}\nAge: {age}")
print(
    f"Types of variables: \nName = {type(name)}\nDate of birth = {type(DOB)}\nAge = {type(age)}"
)
