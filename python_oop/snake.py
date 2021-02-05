#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from reptile import Reptile
# Creating Snake class as child class of Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    # creating some functions for our Snake class
    def use_tongue_to_smell(self):
        return "Mlem to smell"


# snake_object = Snake()

# print(snake_object.limbs)
# print(snake_object.breathe())  # from original Animal class

# We have double inheritance and encapsulated in functions in parent class
