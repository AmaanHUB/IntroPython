#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Connection to an SQL DB from Python using pyodbc

# import the module

# # driver from Microsoft helps us to connect to an SQL instance
# # unixodbc driver needs to be installed on Linux beforehand
import pyodbc

# # Connect to Northwind DB which we have used in SQL week
# # server etc is case sensitive
server = "server_name"
database = "database_name"
username = "username"
password = "password"

# driver - server name - database name - username and password is required to connect to pyodbc
connection = pyodbc.connect(
    f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
)

# Cursor is location of the mouse/current path
cursor = connection.cursor()

# select the version of the current database
# cursor.execute("SELECT @@VERSION")

# see line 1
# row = cursor.fetchone()
# print(row)


# In DB, have a table called Customers (contains customer data)


# execute() does the SQL command, fetchall() gets all the data available
# customer_rows = cursor.execute("SELECT * FROM Customers").fetchall()
#
# print(type(customer_rows))  # prints out the type, is a LIST # iterate through the data and output
#
# for records in customer_rows:
#     print(records)

# Note, fetchall() does not need to be explicitly said
# products = cursor.execute("SELECT * FROM Products").fetchall()
#
# # iterate through the products table data and output UnitPrice
# for records in products:
#     # iterating variable.column_name
#     print(records.UnitPrice)
product_rows = cursor.execute("SELECT * FROM Products")

# getting the Product table data

# iterating through the data until the last line of the data
# until condition is False
while True:
    # fetchall() in original product_rows would fetch all
    # the fetchone() bit grabs it one at a time
    records = product_rows.fetchone()
    # if is empty
    # None is equivalent to NULL in SQL
    if records is None:  # normally would throw an exception
        break  # this helps keep the program under our control
    print(records.UnitPrice)
