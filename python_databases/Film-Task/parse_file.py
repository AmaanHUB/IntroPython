#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# Code to parse a csv into Python


# import relevant libraries
import csv
import pyodbc
# only used for exporting, though can be used for csv to SQL
import pandas as pd


class Movies:
    def __init__(self):
        # declare the variable for accessing the server
        # note that these are placeholder, change with actual details
        self.server = "server"
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

    def create_table(self, table_name):
        # SQL query to create table
        # can be improved by not hardcoding the titles
        # could read them from the file
        # like in the column_headers
        print("Table creation in progress:\n")  # small message to show something is being done
        self.cursor.execute(f"""CREATE TABLE {table_name}(
                                titleType VARCHAR(MAX),
                                primaryTitle VARCHAR(MAX),
                                originalTitle VARCHAR(MAX),
                                isAdult VARCHAR(MAX),
                                startYear VARCHAR(MAX),
                                endYear VARCHAR(MAX),
                                runtimeMinutes VARCHAR(MAX),
                                genres VARCHAR(MAX)
                                );""")
        self.cursor.commit()
        # create empty list to load films etc into
        imdb_list = []
        # read csv file
        # utf-8-sig removes the \ufeff in the file, appears to be webscraped
        with open("imdbtitles.csv", 'r', encoding="utf-8-sig") as csvfile:
            csvreader = csv.reader(csvfile)
        # for every row in csv, add to list
            for row in csvreader:
                imdb_list.append(row)
        # remove the index 0 to get column headers and
        # remove the likelihood of having to manually remove
        # them from the created table
        column_headers = imdb_list.pop(0)  # column headers here, could make better
        # joins this list of column headers into a string
        # separated by `,` so can put straight into sql query
        column_headers = ",".join(column_headers)
        # small message to say something is being done
        print(f"Data being added to {table_name} in process:\n")
        # loop through populated list, many INSERT SQL commands
        for row in imdb_list:
            # some films have an apostrophe, this adds an escape
            # character so that is can read through properly
            values = ", ".join("'" + value.replace("'"," ") +
                               "'" for value in row)
            self.cursor.execute(f"""INSERT INTO {table_name} (
                                    {column_headers}
                                    ) VALUES (
                                    {values}
                                    );""")
            self.cursor.commit()

    # function to get all the films
    def show_films(self, table_name):
        try:
            # query to show all the films
            self.cursor.execute(f"""SELECT * FROM {table_name}""")
            # loop to print out the films
            for row in self.cursor.fetchall():
                print(row)
        except (ConnectionError, TimeoutError) as e:
            print("Error: " + str(e))

    # function to search based upon the film
    def search_film(self, film_name, table_name):
        try:
            self.cursor.execute(f"""SELECT * FROM {table_name}
                                    WHERE primaryTitle = '{film_name}';""")
            # loop to print out the results
            for row in self.cursor.fetchall():
                print(row)
        except (ConnectionError, TimeoutError) as e:
            print("Error: " + str(e))

    # function to add movie to database
    def add_to_database(self, table_name, titleType, primaryTitle, originalTitle,
                        isAdult, startYear, endYear, runtimeMinutes,
                        genres):
        try:
            self.cursor.execute(f"""INSERT INTO {table_name} (
                                    titleType, primaryTitle, originalTitle,
                                    isAdult, startYear, endYear,
                                    runtimeMinutes, genres
                                    ) VALUES (
                                    '{titleType}', '{primaryTitle}', '{originalTitle}',
                                    '{isAdult}', '{startYear}', '{endYear}',
                                    '{runtimeMinutes}', '{genres}'
                                    );""")
            self.cursor.commit()
        except (ConnectionError, TimeoutError) as e:
            print("Error: " + str(e))

    # output to csv file
    def export_database(self, table_name, file_name):
        # create the query to be used and put it in
        # the pandas read_sql_query method format
        search_query = pd.read_sql_query(f"""SELECT * FROM {table_name}""", self.connection)
        # create a dataframe to export
        data = pd.DataFrame(search_query)
        # output to csv file of choise
        data.to_csv(rf"./{file_name}.csv", index=False)


# testing
movies = Movies()
# movies.create_table("d_testing")
# movies.show_films("b_testing")
# movies.search_film("Bigfoot", "d_testing")
# movies.add_to_database("d_testing", "movie", "chicken", "chicken", "0", "1223", "1223", "93", "Animation")
# movies.search_film("chicken", "d_testing")
movies.export_database("d_testing", "export_test")
