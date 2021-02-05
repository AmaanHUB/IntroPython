# Restaurant Waiter Helper Program

## Summary

Now that we've created had some time to use our lists, time to make something more useful.

You are going to make a program that helps a waiter with his menu and his orders.

See tasks for the user stories.

## Tasks

User stories:

```
# User Stories
#1
# AS a User I want to be able to see the menu in a formatted way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.
```


## Acceptance Criteria

* It's own project on your laptop and Github
* Be git tracked
* Have 5 commits mininum!
* Haves documentation
* Follows best practices


## Menu class
* The menu class contains the menu of available items to order as well as a method to see what it on the menu. In the future, this could be expanded to add another function to add or remove items off the menu, in addition to using a dictionary for prices.

```python
class Menu():

    # initialise the class
    def __init__(self):
        # create a menu as a list, though a dictionary would work for prices
        self.menu = ["chicken", "fish", "steak",
                     "quorn burgers", "chips"]

    # function to loop through menu and print it out for the user
    def check_menu(self):
        # for loop through self.menu
        print("Please see below for the items that we offer: \n")
        for item in self.menu:
            print(item)  # remember not to use return, as only outputs 1st


# Initialisation of an object Menu()
# test = Menu()

# Print out menu items test
# test.check_menu()
```


## Order class
* This class contains a list for the orders as well as functions for showing what has been ordered so far, and to order. It inherits from the menu class so the check_menu() function is available too.

```python

from menu import Menu


class Orders(Menu):

    def __init__(self):
        # super() used to inherit from the parent class
        super().__init__()
        # initialise an order list to add to
        self.order_list = []

    # small function to add items to an order_list
    def order_item(self, *args):  # args to add as many items as like
        for item in args:
            # add a conditional here to check if item is on menu if possible
            self.order_list.append(item)

    # function to show what the customer has ordered so far
    def show_ordered(self):
        print("You have currently ordered: \n")
        for item in self.order_list:
            print(item)


# Initialise an object for testing
customer = Orders()

# Testing the methods
customer.check_menu()  # check menu from parent class
customer.show_ordered()  # to check if empty to start with
customer.order_item("chicken", "fish")  # add something to order_list
customer.show_ordered()  # check again if added to order_list
```
