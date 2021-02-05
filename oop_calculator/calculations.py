#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Class containing calculation method

class Calculations:

    # initialise the class
    def __init__(self):
        self.self = self

    # Add two numbers together
    def add(self, num1, num2):
        return num1 + num2

    # Subtraction of two numbers
    def subtract(self, num1, num2):
        return num1 - num2

    # Multiplication of two numbers
    def multiply(self, num1, num2):
        return num1 * num2

    # Division of two numbers
    def divide(self, num1, num2):
        # checks if one of the numbers is 0, as that would give infinity
        if (num1, num2) == 0:
            print("Cannot divide by 0")
        else:
            return num1 / num2

    # Give true or false if number is fully divisible
    def true_divide(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    # Print out the area of a triangle
    def triangle_area(self, base, height):
        return 0.5 * base * height

    # convert inches to centimetres
    def inch_to_cm(self, inch):
        return inch * 2.54


calculation = Calculations()  # initialisation of an object named calculation
# Testing of the functions
print(calculation.add(3, 6))
print(calculation.subtract(6, 3))
print(calculation.multiply(6, 3))
print(calculation.divide(15, 3))
print(calculation.true_divide(10, 3))
print(calculation.triangle_area(5, 10))
print(calculation.inch_to_cm(1))
