#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from emoji import emojize
# Use json module to do json encoding and decoding

import json

# creating a dictionary and storing it into a variable
car_data = {"name": "VW",
            "engine": "small"}


# print(type(car_data))


# json.dumps() - serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))


# json.dump() creates a stream object and accept a file object to write to
with open("new_json_file.json", "w") as jsonfile:  # w is write permissions
    json.dump(car_data, jsonfile)


with open("new_json_file.json", "r") as jsonfile:
    car = json.load(jsonfile)  # load(), copies data into variable
    print(type(car))
    # getting the value by keys
    print(car["name"])
    print(car["engine"])

# json is used heavily in the industry so reading, writing, parsing and converting data are
# the most commonly utilised options

# json.dump() with exception handling
# json.dump() creates a stream object and accept a file object to write to
with open("new_json_file.json", "w") as jsonfile:  # w is write permissions
    try:
        json.dump(car_data, jsonfile)
    except Exception as e:
        print(e.__class__, " has occured")
    finally:
        print("Double check the directory to see if anything has been made :smile-face:")
