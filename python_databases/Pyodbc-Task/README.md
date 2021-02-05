# Pyodbc Task

* Create a new file and a class with function to establish connection with pyodbc
* create a function that create a table in the DB
* create a function that prompts user to input data in that table
* create a new file called PYODBC_TASK.md and document the steps to implement the task

## Code Explanation

* First make sure all the software is installed on the main README.md page

* Import the libraries
```python
# import library
import pyodbc
```

* Declare the class and initialise all the variables that one will use to connect to the database server. *Note that these shown are placeholders and should be replaced with your values*
```python
class Task:
    # initialise the class
    def __init__(self):
        # declare the variable for accessing the server
        # note that these are placeholder, change with actual details
        self.server = "server_name"
        self.database = "database"
        self.username = "username"
        self.password = "password"
```

* In the `__init__` method, one needs to connect to the database and assign a cursor variable
	* Syntax for the `connect()` method is:
		* ``.connect(f"DRIVER = {driver}; SERVER = {server}; DATABASE = {database}; UID = {username}; PWD = {password};")``
			* Note that this is using f-strings for clarity, it can also be done with concatenation
			* Also note that the triple double quotations denote a multiline string
```python
        # connect to the database with the variable shown above
        self.connection = pyodbc.connect(f"""DRIVER=ODBC Driver 17 for SQL Server;
                                    SERVER={self.server};
                                    DATABASE={self.database};
                                    UID={self.username};
                                    PWD={self.password};""")
        # creation of cursor variable
        self.cursor = self.connection.cursor()
```

* Creation of a function to create the table in the first place
	*  The `self.cursor.execute()` contains the full `CREATE TABLE ...` SQL statement
	* The `self.connection.commit()` is within a `try` block as this is when the change are done to the database and this would be the point of failure, with the `except` containing two common errors (the `TimeoutError` occurred to me a few times when trying to access the database) though the FileExistsError is not technically correct in this context
```python
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
```

*  A function to see what is in the table, will be used within other functions for checking.
	* Again the SQL query is within the `cursor.execute()` method, though we do not need the `cursor.commit()` statement anymore as we are not making any changes to the table/database
```python
    # function to show the current table, can be used for checks
    def see_table(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
```

* Finally, the function to add information to the table_name
	* Firstly the columns are printed using an SQL statement and a for loop to let the user know what is available
	* Secondly, column names and values for said columns are assigned to variables to be used in a later SQL statement
	* Thirdly, an `INSERT` SQL statement is done and committed within a try statement, since this is the place where errors are likely to happen
		* You've already seen the `TimeoutError` above
		* I've included another `except` statement with `pyodbc.ProgrammingError`, because I found this was another common error that kept popping up when making this. It would likely come in handy if one were making any changes to the `INSERT` statement in this function
			* Functionality needs to be checked for this though
	* Fourthly, the `see_table()` function is called to confirm the values have been added
```python
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
```

* Some testing was done by instantiating an object and testing out the methods. See below
```python
# instantiating an object for testing
testing = Task()
testing.create_table("Vet_Patients_2", "cat_name", "colour", "owner_name")
testing.add_data("Vet_patients_2")
row = testing.cursor.fetchone()
# testing.cursor.execute("SELECT @@VERSION")
print(row)
```
## Improvements For The Future

* Some error checking for if the database already exists, and if does, can skip this step
	* A creation of own error classes for custom messages etc could be done too, ![see here](https://www.programiz.com/python-programming/user-defined-exception)
* Be able to create as many columns as want, as well as define their data type
	* Could be done with a dictionary and `**kwargs`
* A `test*.py` file to check these methods with different criteria for some automated testing (with `pytest`)


# Pyodbc Task 2

* Create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.

* As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.

* The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.

* Create two files nw_products.py & nw_runner.py and then we will move into creating our object.

* Our first requirement...
* We've had a requirement for the stock department to print out the average value of all of our stock items.

* !!!Important Note!!! It would be more efficient to write the SQL query to find the data and compute the value and simply return the value in Python.

## Code Explanation

### nw_products.py

* A file called `nw_products.py` should be created
* Import the relevant libraries
```python
# import the library
import pyodbc
```

* Create the class (entitled `Products`) and the `__init__` method. This should contain the real details that one will use to connect to their own database.
	* The `connection` variable should contain the `pyodbc.connect()` method with the relevant variables inserted.
	* The `cursor` variable should be initialised as well for usage later

```python
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
```

*  The function to determine the average uses an SQL statement that itself calculates the average. This should reduce computational load.
	* `cursor.execute()` contains an SQL statement that calculates the average of that column
	* Everything except print statement in a `try-except` statement
	* The SQL query outputs a tuple in a list so one needs to get the index to show only the number if only want to show that (even though the tuple and list is empty apart from that)
```python
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
```

### nw_runner.py

* Import the `nw_products` file and `Products` class
```python
# import the nw_products file and relevant class

from nw_products import Products
```

* Create the class and inherit everything from Products with a `super()` method in the `__init__` method
```python
# create the class Runner that inherits from Products
class Runner(Products):
    # initialise the class
    def __init__(self):
        # super() means gets all attributes from previous class
        super().__init__()
```
* Initialise an object to test the `avg_stock()` method from the Products class
```python
# initialise an object for testing
runner = Runner()
# testing the avg_stock() method to see ouput
runner.avg_stock()
```
