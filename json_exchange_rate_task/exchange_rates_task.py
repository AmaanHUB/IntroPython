#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import libraries needed
import json

# opening up the json file with read permissions and
# naming it as something easy to use
with open("exchange_rates.json", "r") as jsonfile:
    # create a dictionary from the json file
    # the ["rates"] gets the nested dictionary and turns it
    # into a non-nested simple dictionary of just rates
    exchange_rates = json.load(jsonfile)["rates"]

    # checking if it has been created as type dictionary
    print(type(exchange_rates))

    # having a look at what is in the dictionary
#     print(exchange_rates)


# Function to print the exchange_rates
def print_exchange_rates():
    # loop through the exchange_rates dictionary
    for x in exchange_rates:
        # prints out the key in capitals with the exchange rate next to it
        print(f"{x.upper()}: {exchange_rates[x]}")


