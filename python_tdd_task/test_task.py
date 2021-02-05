#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File with the relevant tests to test the code

# import testing libraries
import pytest
import unittest

# import class
from task import Task

# class made, inherit from unittest.testcase
class TestTask(unittest.TestCase):

    # testing whether a number is divisible or not
    def test_divisable(self):
        # assertTrue checks if output gives true, which this should
        # as 6 % 3 = 0, which returns true in function
        self.assertTrue(self.test.divisible(6, 3), "This should be True")
        # assertFalse checks if output gives false, which this should do
        # as 7 % 3 = 1, which returns false in the function
        self.assertFalse(self.test.divisible(7, 3), "This should be False")

    def test_positive(self):
        # assertFalse checks if output gives false, which this should do
        # -1 should return a False as is negative, assertTrue should be the
        # opposite
        self.assertFalse(self.test.positive(-1), "This should be False")
        self.assertTrue(self.test.positive(15), "This should be True")

    # initialise an object to apply the methods to in testing
    test = Task()

