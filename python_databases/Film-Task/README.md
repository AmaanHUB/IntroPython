# Film Task

* CRUD the DB

* Hint: create abstraction and methods to deal with db so you don't have too
* Acceptance Criteria:
    * You can get all the movies
    * You can search based on title
    * You can add movies to DB
* Your task is to move data from text files into the db and from the the db into text files
* Tasks:
    * Read the text file and create object
    * Save object in DB
    * Load that from DB and create object
    * Output object to text file
* Extra:
	* Explore other APIs
* Acceptance Criteria:
    * Able to take in 10 film names in text file and save to db
    * Able to load data from DB and create text file with names

## Summary Of Code

* Import the relevant libraries (pandas is used exclusively for the csv output)
```python
# import relevant libraries
import csv
import pyodbc
# only used for exporting, though can be used for csv to SQL
import pandas as pd
```

* Initialise the class and variables, and those variables in a connection variable statement using the pyodbc library
```python
class Movies:
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
```
### Create Table Function

* The `create_table()` function is a very large function, that could will be broken down into two sections for the explanation
* **Part 1, Creating the TABLE**
```python
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
```
* The function is declared with the parameter `table_name` to create a table with that name
	* The SQL statement is in `self.cursor.execute()` statement, though the titles for each of the columns are hard-coded for now
	* The `self.cursor.commit()` 'commits' the changes to the database
	* These statements could be in `try` `execute` statement, and would be in another iteration, with checks to see if the table already exists
* **Part 2, Adding The Data from the csv file**
```python
        # create empty list to load films etc into
        imdb_list = []
        # read csv file
        # utf-8-sig removes the \ufeff in the file, appears to be webscraped
        with open("imdbtitles.csv", 'r', encoding="utf-8-sig") as csvfile:
            csvreader = csv.reader(csvfile)
        # for every row in csv, add to list
            for row in csvreader:
                imdb_list.append(row)
```
* Initialise an empty list to add data to
* Using the `csv` module, `open` is used to essentially 'stream' the file to be saved
	* Within  the `open` statement, the encoding as set as it is, as it ignores certain artifacts that are within the csv file as a result of scraping from the web
*  The `for` loop essentially adds all in the csv file to the previously declared list
```python
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
```
* The `values...` section in the `for` loop is used to add escape characters to the information in the csv file, as this causes some problems later down the line when trying to do the `INSERT INTO` statement and `commit()`

### Show Films Functions

* The function takes the table name as a parameter and then uses it in an SQL statement (within the `self.cursor.execute()`
```python
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
```

### Show Specific Film Function

*  Similar to the `show_films()` function, except one specifies which film one wants to see, which is implemented using a `WHERE` section in the SQL statement
	* Needs something to output if the film is not within the database, like an error message
```python
    # function to search based upon the film
    def search_film(self, film_name, table_name):
        try:
            self.cursor.execute(f"""SELECT * FROM {table_name}
                                    WHERE primaryTitle = {film_name}""").fetchone()
            # loop to print out the results
            for row in self.cursor.fetchall():
                print(row)
        except (ConnectionError, TimeoutError) as e:
            print("Error: " + str(e))
```

### Adding Something To Table

* This function takes data, but only works if all the column headings have been satisfied
	* This could be improved with user input, and checking for the variable type too
* The `INSERT INTO` has hardcoded values in the column names, this could be improved with a similar solution in the `create_table()`
```python
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
```

### Exporting Into A CSV File

* This function takes advantage of the `pandas` library, though it can also be done with the default `csv` library
```python
    def export_database(self, table_name, file_name):
        # create the query to be used and put it in
        # the pandas read_sql_query method format
        search_query = pd.read_sql_query(f"""SELECT * FROM {table_name}""", self.connection)
        # create a dataframe to export
        data = pd.DataFrame(search_query)
        # output to csv file of choise
        data.to_csv(rf"./{file_name}.csv", index=False)
```
