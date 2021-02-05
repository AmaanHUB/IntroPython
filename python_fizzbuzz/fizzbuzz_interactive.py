#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Class to hold the fizzbuzz function


class FizzBuzz():

    # Initialise the class, no arguments since hardcoded
    def __init__(self, fizz_num, buzz_num):
        self.fizz_num = fizz_num
        self.buzz_num = buzz_num

    def fizzbuzz(self):
        # need to use args in __init__ otherwise not recognised in function
        fizz_num = int(input("Number for Fizz? "))
        buzz_num = int(input("Number for Buzz? "))
        # for loop up to 100
        for x in range(101):
            if x % fizz_num == 0:
                print("Fizz")
            elif x % buzz_num == 0:
                print("Buzz")
            elif x % fizz_num == 0 and x % buzz_num == 0:
                print("FizzBuzz")
            else:
                print(x)


test = FizzBuzz(3, 5)
# find a way to not need to add numbers when initialising
# as seems pointless because have to input numbers anyway

print(test.fizzbuzz())

