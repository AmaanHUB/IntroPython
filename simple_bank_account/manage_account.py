#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import class  from my_account
from my_account import MyAccount

# Creation of ManageAccount class


class ManageAccount:
    # initialisation of the class
    def __init__(self):
        print("Time to test all the methods available")


# Creation of an object for testing
account1 = MyAccount(1521031, 150, "Chicken", "123 Wing Rd.", 10)
# Testing the methods
account1.display_details()  # display input details
account1.deposit(100)  # add 100 to account1
print(account1.get_balance())  # display the balance only
account1.withdrawal(50)
print(account1.get_balance())  # display the balance only
account1.bank_fees(10)
print(account1.get_balance())  # display the balance only
account1.set_name("Chicken Little")
account1.set_address("Buck Lane")
account1.display_details()
