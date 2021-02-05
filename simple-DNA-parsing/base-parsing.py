#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Class to parse DNA bases and count them


class BaseParsing:
    # instantiate a class
    def __init__(self):
        # print a message to say what it is
        print("DNA Base Counter")
        # define the allowed bases
        self.bases = ["A", "C", "G", "T"]

    # Function to count the number of DNA bases in the given dataset set
    def base_counting(self, dataset):
        # convert the dataset into capitals
        dataset = dataset.upper()
        # initialise the variable for counting the individual bases
        # this area has room for improvement perhaps
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        # instead of a loop, could use count() method
        # loops through data string (nucleotide sequence)
        for letter in dataset:
            # informs user that sequence has non-standard characters in it
            if letter not in self.bases:
                print("This contains non-standard DNA bases!")
            # checks if letter is in sequence and adds it to its counter
            elif letter == "A":
                a_count = a_count + 1
            elif letter == "C":
                c_count = c_count + 1
            elif letter == "G":
                g_count = g_count + 1
            else:
                t_count = t_count + 1
        # print out counts in a nice formatted manner
        print(f"A: {a_count}\nC: {c_count} \nG: {g_count}\nT: {t_count}")


# initialising an object
test = BaseParsing()

# testing the sample string
test.base_counting("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
