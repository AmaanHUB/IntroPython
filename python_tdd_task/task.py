#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Task file

class Task:

    # function to check if numbers are divisible by each other
    def divisible(self, num1, num2):
        # if modulus is 0, then they are wholly divisible
        if num1 % num2 == 0:
            return True
        else:
            return False

    # function to check if a number is positive or not
    def positive(self, number):
        # if higher than 0, is a positive number
        if number > 0:
            return True
        else:
            return False

