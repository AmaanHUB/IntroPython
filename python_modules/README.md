# Python Modules

## Built In Functions
* They help accelerate our development of our software.
* Creating a customised method and utilising the built in functionality at the same time:
```python
# Customised method using built in sys methods
def current_system_path():
    print("This is your current directory: ")
    return sys.path
```
## Python Library

* A library contains modules that provide access to certain functionalities that can be useful .e.g. wrappers for APIs, climate models etc., in addition to the standard Python library which contains all the core tools with a clean Python installation.

## Using Pip

* Package manager for Python and helps us install external packages such as requests
* Syntax:
	* ```pip install package_name```
## APIs with Python
* From localhost → using API calls and protocols (.e.g. SSH, HTTP/S) → web
* Can be used for:
	* Finding out if the 'website' is live
	* To handle the user as per the response to the web
	* Meeting the user's expectations

## Requests Module

```python
from emoji import emojize
import requests
# third iteration
# what is the advantage of using the requests module
def check_response_code():
    # request checks if working essentially behind the scenes
    if live_response.status_code:  # True
        print("Mission successfull " + str(live_response.status_code))
        print(emojize((":thumbs_up:")))  # adding an actual emoji works here too
    elif live_response.status_code:  # False
        print("Error, the site is unavailable until further notice. Please contact your SysAdmin.")
    else:
        print("Something went wrong (IS DEAD), try again later. ")
```
* **NOTE** It will evaluate to True if status code was true between 200 and 400, otherwise False
* See website below for more status code information:
	* ![status_code](https://github.com/psf/requests/blob/master/requests/status_codes.py)

### Task with Requests
* Find a way to convert this the postcode website content from a json into a dictionary, and iterate through the results and print longitude and latitude. Create a function that does this.

#### Code Summary

* Firstly the url is saved as a variable using ```requests.get()``` and user input is taken for adding to the end of the URL do get the desired postcode.

```python
# declares the url for use later
postcode_url_api = requests.get("http://api.postcodes.io/postcodes/")

# User input
argument = str(input("Please enter your postcode:\n"))
# Add the user input to the url
url_response = requests.get(f"http://api.postcodes.io/postcodes/{argument}")
```
* The content from this url is parsed into a dictionary using the ```json.loads()``` method.
	* The ```["result"]``` section is needed due to the this key containing a nested dictionary with all of the relevant data. This allows one to only get the data one needs in a simple dictionary.

```python
# calls the ["result"] to only get the stuff within the "result",
# otherwise get a nested dictionary with status and everything else
# within the result section
postcode_dictionary = json.loads(url_response.content)["result"]
```
* The dictionary is then iterated through, checking whether the website is up using the ```status_code``` attribute in a boolean, and outputted in a nice format.

```python
# function to show the specific key's values
def display_location():
    # checks if web site is available
    if url_response.status_code:
        # checks in the [] list for keys and outputs them
        for x in ["postcode", "longitude", "latitude"]:
            print(f"{x.capitalize()}: {postcode_dictionary[x]}")
        # if website not available, output error
    else:
        print("Error: Unavailable")
```
* It should be noted that when converting into a dictionary, one does not need to specify the result key, one can specify the key in the for loop .e.g.
```python
print(f"{x.capitalize()}: {postcode_dictionary["result"][x]}")
```

## CRUD

* The life cycle of an API:
	* C - Create
	* R - Read
	* U - Update
	* D - Delete


## JSON Basics

* JavaScript Object Notation
* Data is in key value pairs
* JSON can be encoded into a dictionary and from a dictionary
* Handling/Creating files with Python
* Writing/Reading files

### Using JSON in Python

* Dictionary is made to show some functions in the json library
```python
# creating a dictionary and storing it into a variable
car_data = {"name": "VW",
            "engine": "small"}
```

* A dictionary can be made into a formatted json string using ```json.dumps()```
	* **Not to be confused with** ```json.dump()```

```python
# json.dumps() - serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
```
* It can also be made into a separate .json file using ```json.dump()```

```python
# json.dump() creates a stream object and accept a file object to write to
with open("new_json_file.json", "w") as jsonfile:  # w is write permissions
    json.dump(car_data, jsonfile)
```
* Finally it can also be read from a json file, and converted back into a dictionary with ```json.loads()```

```python
with open("new_json_file.json", "r") as jsonfile:
    car = json.load(jsonfile)  # load(), copies data into variable
    # getting the value by keys
    print(car["name"])
    print(car["engine"])
```
## Permissions

* Syntax:
	* ```open("file_name", "permission_mode")```

| Permission Mode | Description |
| :---------------|------------:|
|	r 			   | Default mode. Opens file read-only |
|  w 			| Opens file for writing. If it does not exist, creates file. If it does, it truncates it |
| x				| Creates a new file. If it already exists, operation fails |
| a 			| Open file in append mode. If it does not exist, creates it |
|  t 			| Opens in text mode |
| b 			| Opens in binary mode |
|   + 			| Opens for reading and writing (updating) |

## Exception Handling

* We use these blocks when we expect an error or an exception from the python interpreter.
* **Why?**:
	* Helps us hangle errors or exceptions
	* Add customised messages as well as make a decision based upon customer needs

### ```try``` and ```except``` Blocks

* ```try``` is for the line of code that we know can potentially throw an error
* ```except``` is to do with how we handle a potential exception
	* `except` .e.g. `except (FileNotFoundError, AttributeError) as e:`
```python
# iteration 1
# create a variable to store a file data using open()
try:  # try block for a line of code that we know that will throw an error
    file = open("orders.text")
except:
    print("file not found ma dude")
```
### ```raise``` and ```finally```
* ```raise``` sends back the full exception unprompted (shows the full traceback error message with the line etc.)
* ```finally``` executes regardless of the conditions in ```try```, ```except``` etc.
```python

# Iteration 2
# create a variable to store a file data using open()
try:  # try block for a line of code that we know that will throw an error
    file = open("orders.text")
except FileNotFoundError as errmsg:
    # cast to string as do not know if it will be one
    print("File unavailable" + str(errmsg))  # custom message with actual exception

    raise  # raise will send back the actual full exception unprompted .e.g. traceback etc.
finally:  # execute regardless of above conditions
    print("Have a nice day")
```
