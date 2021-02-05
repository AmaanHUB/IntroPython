#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Task:
- Create a new file and a class with function to establish connection with pyodbc
- create a function that create a table in the DB
- create a function that prompts user to input data in that table
- create a new file called PYODBC_TASK.md and document the steps to implement the task
"""

# import library
import pyodbc


class Task:
    # initialise the class
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

    # NOTE, need to find a way to skip this if table already exists
    # function to create a table
    def create_table(self, table_name, column_name1, column_name2,
                     column_name3):
        # sql command to create the table with specified name, and columns
        self.cursor.execute(f"""CREATE TABLE {table_name}(
                          Animal_id INT IDENTITY PRIMARY KEY,
                          {column_name1} VARCHAR(MAX),
                          {column_name2} VARCHAR(MAX),
                          {column_name3} VARCHAR(MAX)
                            )""")
        # try to commit it, as this is one of the parts that could go wrong
        try:
            # try to finalise the table creation
            self.connection.commit()
        # error looking for would be the timeout error
        # if already made then would happen or slow connection
        except (TimeoutError, FileExistsError) as e:
            # print out the error message with a small string
            print("Error: " + str(e))

    # function to add values to the table
    def add_data(self, table_name):
        # shows the columns one can add to first
        print("See available columns below:")
        # SQL query show the table information
        table_information = self.cursor.execute(f"""SELECT TABLE_NAME, COLUMN_NAME
                                                FROM INFORMATION_SCHEMA.COLUMNS
                                                WHERE TABLE_NAME = '{table_name}';""")
        # for loop to print out the information
        for i in table_information:
            print(i)
        # get user input on columns want to add info to
        # NOTE, \n at end of string messes with the sql adding
        column_1 = str(input("Please choose a column to insert into: "))
        value_1 = input("Value for chosen column: ")
        column_2 = str(input("Please choose another column to add to: "))
        # get the value input for the columns
        value_2 = input("Values for chosen column: ")
        column_3 = str(input("Please choose another column to add to: "))
        value_3 = input("Values for chosen column: ")
        try:
            # CHECK what is in the values and columns first
            self.cursor.execute(f"""INSERT INTO {table_name}
                                ({column_1}, {column_2}, {column_3})
                                VALUES
                                ('{value_1}', '{value_2}', '{value_3}');""")
            self.connection.commit()
        except TimeoutError as e:
            print("Error: " + str(e))
        except pyodbc.ProgrammingError as pe:
            print("Error: " + str(pe))
        # show the table to see what is in it
        self.see_table(table_name)

    # function to show the current table, can be used for checks
    def see_table(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")


# instantiating an object for testing
testing = Task()
testing.create_table("Vet_Patients_2", "cat_name", "colour", "owner_name")
testing.add_data("Vet_patients_2")
row = testing.cursor.fetchone()
# testing.cursor.execute("SELECT @@VERSION")
print(row)

