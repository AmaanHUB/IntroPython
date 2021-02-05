#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

import requests
import json  # imported to read content from website

random_postcode = requests.get("http://api.postcodes.io/random/postcodes")

# argument = str(input("Please enter your postcode:\n"))
# url_target = random_postcode + argument

# print(type(random_postcode.content))
# print(random_postcode.content)

## TASK
# find a way to convert this into a dictionary
# HINT - json library can be used to resolve this

# iterate through the data and print RESULTS
# print longitude and latitude

# if live website, get contents and iterate
# create a function that returns the longitude and latitude


# print(random_postcode.status_code)

# declares the url for use later
postcode_url_api = requests.get("http://api.postcodes.io/postcodes/")

# User input
argument = str(input("Please enter your postcode:\n"))
# Add the user input to the url
url_response = requests.get(f"http://api.postcodes.io/postcodes/{argument}")

# calls the ["result"] to only get the stuff within the "result",
# otherwise get a nested dictionary with status and everything else
# within the result section
postcode_dictionary = json.loads(url_response.content)["result"]


# function to show the specific key's values
def display_location():
    # checks if web site is available
    if url_response.status_code:
        # checks in the [] list for keys and outputs them
        for x in ["postcode", "longitude", "latitude"]:
            print(f"{x.capitalize()}: {postcode_dictionary[x]}")
        # if website not available, output error
    else:
        print("Error: Unavailable")

## Alternative way
# postcode_dictionary = json.loads(url_response.content)
#
#
# def display_location():
#     if url_response.status_code:
#         for x in ["postcode", "longitude", "latitude"]:
#             print(f"{x.capitalize()}: {postcode_dictionary["result"][x]}")
#     else:
#         print("Error: Unavailable")
