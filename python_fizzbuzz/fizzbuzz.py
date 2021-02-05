#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Class to hold the fizzbuzz function


class FizzBuzz():

    # Initialise the class, no arguments since hardcoded
    def __init__(self):
        self.self = self  # appears need this bit for it to function

    def fizzbuzz(self):
        # for loop up to 100
        for x in range(101):
            if x % 3 == 0:
                print("Fizz")
            elif x % 5 == 0:
                print("Buzz")
            elif x % 3 == 0 and x % 5 == 0:
                print("FizzBuzz")
            else:
                print(x)


# Initialising FizzBuzz object
test = FizzBuzz()

test.fizzbuzz()  # testing if it works

