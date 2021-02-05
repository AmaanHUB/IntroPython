#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import testing libraries
import pytest
import unittest

# import class to test
from naan_factory import NaanFactory

class NaanFactoryTest(unittest.TestCase):

    naan_test = NaanFactory(True, True)

    # a test to see if dough can be made
    def test_make_dough(self):
        # see if it has dough and water, should come out as True
        self.assertTrue(self.naan_test.make_dough())

    def test_bake_dough(self):
        # see if it has dough to get the naan, will be True
        self.assertTrue(self.naan_test.bake_dough())

    # test run_factory method()
    def test_run_factory(self):
        self.assertTrue(self.naan_test.run_factory())

