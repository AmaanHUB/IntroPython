#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.
#
# As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.
#
# The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.
#
# Create two files nw_products.py & nw_runner.py and then we will move into creating our object.
#
# Our first requirement...
# We've had a requirement for the stock department to print out the average value of all of our stock items.
#
# Away we go....
#
# !!!Important Note!!! It would be more efficient to write the SQL query to find the data and compute the value and simply return the value in Python.

# import the library
import pyodbc


class Products:
    def __init__(self):
        # declare the variable for accessing the server
        # note that these are placeholder, change with actual details
        self.server = "server_name"
        self.database = "database"
        self.username = "username"
        self.password = "password"
        # connect to the database with the variable shown above
        self.connection = pyodbc.connect(f"""DRIVER=ODBC Driver 17 for SQL Server;
                                    SERVER={self.server};
                                    DATABASE={self.database};
                                    UID={self.username};
                                    PWD={self.password};""")
        # creation of cursor variable
        self.cursor = self.connection.cursor()

    # function to show the average number in stock
    def avg_stock(self):
        # Test the section that is most likely to fail
        try:
            # use SQL query to calculate the average
            avg_stock = self.cursor.execute("""SELECT AVG(UnitsInStock)
                                            FROM Products;""").fetchall()
            # SQL variable makes into a tuple within a list
            avg_stock = avg_stock[0][0]
        # assumed to be the most common exceptions
        except (TimeoutError, ConnectionError,
                ConnectionAbortedError) as e:
            print("Error: " + str(e))
        print("Average Stock Value: " + str(avg_stock))


# initialise an object for testing
# products = Products()
# testing the avg_stock() method
# products.avg_stock()
