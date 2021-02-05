#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#


# import AccountHolderDetails class
from account_holder_details import AccountHolderDetails
# Class for MyAccount


class MyAccount(AccountHolderDetails):
    # Initialise class
    # need to add parameters like name here so they can be added
    # when object is created
    def __init__(self, account_number, balance, name, address, age):
        # allows one to use variables from class inheriting from
        super().__init__(name, address, age)  # tells that using these variable
        # declare parameters as private variables
        self.__account_number = account_number
        self.__balance = balance

    # Getter method for account_number
    def get_account_number(self):
        return self.__account_number

    # don't need setter for account_number, as should not be changed

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    # probably could do with some error checking here .i.e. if is a number
    def set_balance(self, new_balance):
        self.__balance = int(new_balance)

    # Adds to balance using the set_balance() method
    def deposit(self, deposit_value):
        # check if the number depositing is positive
        if int(deposit_value) > 0:
            self.__balance = self.get_balance() + deposit_value
        # gives an error message if not positive
        else:
            print(f"{deposit_value} is an invalid value")

    # Reduces balance using the set_balance() method
    def withdrawal(self, withdrawal_value):
        # check if the number withdrawing is positive
        if int(withdrawal_value) > 0:
            self.set_balance(self.get_balance() - withdrawal_value)
        # gives an error message if not positive
        else:
            print(f"{withdrawal_value} is an invalid value")

    # Implement the bank fees on the total balance
    def bank_fees(self, percentage):
        self.set_balance((self.get_balance() * (1 - (percentage / 100))))

    # displays the full account details in a formatted way
    def display_details(self):
        print(f"Account No.: {self.get_account_number()}\n" +
              f"Balance: {self.get_balance()}\n" +
              f"Name: {self.get_name()}\n" +
              f"Address: {self.get_address()}\n" +
              f"Age: {self.get_age()}")
