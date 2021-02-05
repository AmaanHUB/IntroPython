#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import the nw_products file and relevant class

from nw_products import Products

# create the class Runner that inherits from Products
class Runner(Products):
    # initialise the class
    def __init__(self):
        # super() means gets all attributes from previous class
        super().__init__()


# initialise an object for testing
runner = Runner()
# testing the avg_stock() method to see ouput
runner.avg_stock()
