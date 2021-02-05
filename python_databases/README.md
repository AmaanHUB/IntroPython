# Python Databases

## Why Are We Using Databases (DB)?

* To make data persistent and utilise as when required
	* To meet customer expectations


## How Does Python Interact With Databases?
![](Python-With-SQL.png)

* **Python (probably on localhost) → API → Database (on cloud or not)**
	* Two way exchange of information. Python asks something of the database and the database can return some information or is manipulated.
* Module used:
	* PYODBC (Python open database connectivity)

## Using PYODBC

* If you are using Linux, you need to install the 'Microsoft ODBC Driver for SQL Server' with the relevant package manager. Instructions for some of the major distributions are ![here](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15). If you are on Arch Linux, it is in the Arch User Repository called 'msodbcsql'
	* This is because the Northwind database is on an MSSQL server
* Need install the pyodbc package
```pip install pyodbc```

* **NOTE**: If using Linux, you often need to install the ```unixodbc``` or some variant depending upon your distribution. Use your relevant package manager

### Connection to SQL From Our Python Program

* Once it is installed, create a new python file
* Import relevant libraries
```python
# import the module

# # driver from Microsoft helps us to connect to an SQL instance
# # unixodbc driver needs to be installed on Linux beforehand
import pyodbc
```
* Declare the variables such as server etc that one will use later
```python
# # Connect to Northwind DB which we have used in SQL week
# # server etc is case sensitive
server = "databases1.spartaglobal.academy"
database = "database"
username = "username"
password = "password"
```
* Using ```pyodbc.connect()``` and assigning it to a variable, can now use these assigned variables
```python
# driver - server name - database name - username and password is required to connect to pyodbc
connection = pyodbc.connect(
    f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
)
```
#### What Is A Cursor? How To Use It?

* A cursor shows the current mouse location or file path. It is used with the ```connection.cursor()``` method
```pythom
# Cursor is location of the mouse/current path
cursor = connection.cursor()
```

### Getting Data From The Database

* Use the ```cursor_variable_name.execute()``` method with the SQL command in the brackets. CASE SENSITIVE. ```fetchall()``` doesn't necessarily need to be added, as this is used by default and selects all the records.
	* These records then can be iterated through
```python

# execute() does the SQL command, fetchall() gets all the data available
customer_rows = cursor.execute("SELECT * FROM Customers").fetchall()


for records in customer_rows:
    print(records)
```
* Another example of getting information from a DB
```python
# Note, fetchall() does not need to be explicitly said
products = cursor.execute("SELECT * FROM Products").fetchall()
```
*  Getting information from a specific column name is done with the syntax ```variable.column_name```
```python
# # iterate through the products table data and output UnitPrice
for records in products:
    # iterating variable.column_name
    print(records.UnitPrice)
```
* Getting information one row at a time, and check for NULL data
```python
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
```
