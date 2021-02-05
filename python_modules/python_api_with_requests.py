#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Import the requests package
import requests
# gives the ability to use emoji
from emoji import emojize


# .get() 'gets' the website
live_response = requests.get("https://www.bbc.co.uk/")

# status_code provides integer response code .e.g. 404
# Rather than : Response [404]
print(live_response.status_code)


print(type(live_response.headers))
print(type(live_response.content))

# first iteration
if live_response.status_code == 200:  # success code is 200
    print("Mission successfull " + str(live_response.status_code))
    print(emojize((":thumbs_up:")))  # adding an actual emoji works here too
elif live_response.status_code == 404:
    print("Error, the site is unavailable until further notice. Please contact your SysAdmin.")
else:
    print("Something went wrong, try again later. ")

# second iteration

# def check_response_code():
#     if live_response.status_code == 200:  # success code is 200
#         print("Mission successfull " + str(live_response.status_code))
#         print(emojize((":thumbs_up:")))  # adding an actual emoji works here too
#     elif live_response.status_code == 404:
#         print("Error, the site is unavailable until further notice. Please contact your SysAdmin.")
#     else:
#         print("Something went wrong, try again later. ")
#
# check_response_code()

# third iteration
# what is the advantage of using the requests module
def check_response_code():
    # request checks if working essentially behind the scenes
    if live_response.status_code:  # True
        print("Mission successfull " + str(live_response.status_code))
        print(emojize((":thumbs_up:")))  # adding an actual emoji works here too
    elif live_response.status_code:  # False
        print("Error, the site is unavailable until further notice. Please contact your SysAdmin.")
    else:
        print("Something went wrong (IS DEAD), try again later. ")

# it will evaluate to True if status code was true between 200 and 400, otherwise False
