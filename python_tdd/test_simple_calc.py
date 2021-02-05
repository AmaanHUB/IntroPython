#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Tests for the simple calculator

# import the class from simple_calc
from simple_calc import SimpleCalc

# import requiring testing frameworks
import unittest
import pytest


# create a class to write tests input

# unittest.TestCase works with the unittest framework as a parent class
class CalcTest(unittest.TestCase):

    # IMPORTANT - we must use TEST word in our functions, so python interpretor
    # knows what we are testing

    # Test the add function
    def test_add(self):
        # self.assertEqual(self.calc.add(num1, num2), total)
        # checks the numbers in the original function, and it should come to 6
        self.assertEqual(self.calc.add(2, 4), 6)  # True if pass

    # Test the subtract function
    def test_subtract(self):
        # Test if 4 - 2 = 2
        self.assertEqual(self.calc.subtract(4, 2), 2)  # True if pass

    def test_multiply(self):
        # Test if 4 * 2 = 8
        self.assertEqual(self.calc.multiply(4, 2), 8)  # True if pass

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    # creating an object of our class
    calc = SimpleCalc()
