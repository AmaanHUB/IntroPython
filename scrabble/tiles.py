#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Class called Tiles, should set and contain the values of the letter tile


class Tiles:
    # initialise the class
    def __init__(self):
        # using a list for each of the letter groups
        self.value_one = ["A", "E", "I", "O", "L", "N", "R", "S", "T"]
        self.value_two = ["D", "G"]
        self.value_three = ["B", "C", "M", "P"]
        self.value_four = ["F", "H", "V", "W", "Y"]
        self.value_five = ["K"]
        self.value_eight = ["J", "X"]
        self.value_ten = ["Q", "Z"]

    #  function to find the score of a word
    def score(self):
        # choose_word() function to assign user input to the word variable
        word = self.choose_word()
        # capitalise the word so can compare easily to list and output nicer
        word = word.upper()
        #  initialise the score variable so can add to
        score = 0
        #  for loop to loop through the word
        for letter in word:
            # if-elif-else statements to add to the score
            if letter in self.value_one:
                score += 1  # add to the running score
                print(f"{letter}: 1")  # display the value of the letter
            elif letter in self.value_two:
                score += 2
                print(f"{letter}: 2")
            elif letter in self.value_three:
                score += 3
                print(f"{letter}: 3")
            elif letter in self.value_four:
                score += 4
                print(f"{letter}: 4")
            elif letter in self.value_five:
                score += 5
                print(f"{letter}: 5")
            elif letter in self.value_eight:
                score += 8
                print(f"{letter}: 8")
            elif letter in self.value_ten:
                score += 10
                print(f"{letter}: 10")
            else:
                print("Not a letter")
        print(f"{word} : {score}")

    # added a small function to help the user input a word of choice
    def choose_word(self):
        word = str(input("Please enter a word: "))
        return word


word = Tiles()  # initialising the object
# word.score("bcmp")
word.score()  # small test
