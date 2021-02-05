#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Practical use cases for try, raise, except, and finally


# # iteration 1
# # create a variable to store a file data using open()
# try:  # try block for a line of code that we know that will throw an error
#     file = open("orders.text")
# except:
#     print("file not found ma dude")



# Iteration 2
# create a variable to store a file data using open()
try:  # try block for a line of code that we know that will throw an error
    file = open("orders.text")
except FileNotFoundError as errmsg:
    # cast to string as do not know if it will be one
    print("File unavailable" + str(errmsg))  # custom message with actual exception

    raise  # raise will send back the actual full exception unprompted .e.g. traceback etc.
finally:  # execute regardless of above conditions
    print("Have a nice day")
