# MVC With Python


## MVC - Model View Controller

Add image here
<++>
## Display Data On The Browser Using HTML, CSS, JavaScript and BOOTSTRAP

* HTML (Hypertext Markup Language)
* CSS (Cascading Style Sheets)
* JavaScript (JS)
* BOOTSTRAP


### Building Our API

* Display data from Python Flask to specific API call/URL/end point
* **Why Flask?:**
	* Flask is a web development framework
	* Very powerful to interact with DB (databases) and user interface/browsers etc
	* Can be used to create an API
	* Allows us to integrate with HTML, CSS and JavaScript
	* Allows us to map HTTP requests to Python functions:
		* GET
		* HTTP
		* URL
	* Allows us to set the API as URL to view in the browser

#### Installing And Running Flask

* Install using `pip` (using terminal)
```
pip install python
```
* Run using the `flask` command in the terminal (when app is created)
```
flask run

# or

python -m flask run
```

#### Creating A Simple Message Display With Flask

* Create a file named `app.py`, as Flask looks for a file with this name
* Import the relevant library
```python
# import module
from flask import Flask
```

* Create an instance of the app
```python
# create an instance an app
app = Flask(__name__)
```

* Create a list with a dictionary inside (to ease the transfer to json, though can just use a dictionary)
```python
# in a list to make it easier to transfer it into json
student = [
    {"id": 0,
     "title": "Dr.",
     "first_name": "Chicken",
     "last_name": "Little",
     "course": "DevOps"
     }
]
```

* Using a decorator (to access API calls/URL), create a function with a simple message inside just to test things
	* HTML sections can be added within the String
```python
# decorator - to create our API/URL for user to access our data in browser
# string is HTTP url
@app.route("/")  # localhost:5000 is default port for flask
# function runs when URL/API is accessed
def home():
    return """<h1>This is a team from the DevOps consultants,
                celebrating a WOW moment!</h1>"""
```

* In the file, tell it to run the app using `app.run()` function (with the debug trait set as True optionally). This can be within an `if __name__ = "__main__"` statement if only want this to run in this file
```python
# if it is this file, run this
if __name__ == "__main__":
    app.run(debug=True)
```

* Run flask from the command line (as shown above)

#### Redirects, Json and More!

**JSON**
* Import the `jsonify` methods
```python
from flask import Flask, jsonify
```

* To show the 'raw' json, need to use the `jsonify` method
```python
# Creating our own API to display data on the specific route/URL/end point/API
# [GET] will add this API/URL to home path
# also uses HTTP GET
@app.route("/api/v1/student/data/", methods=["GET"])
# goes to 127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(student)  # transform data into Json
    # Utilising Extract Transform Load
```

**Redirects**
* Import the `redirects` and `url_for` functions in the `Flask` class
```python
from flask import Flask, jsonify, redirect, url_for
```

* Create a function to redirect to (.e.g. a welcome page)
```python
# greet the user function
@app.route("/welcome/")  # trailing slash, so user can access with or without on URL
def greet_user():
    return "Ayup, welcome to the DevOps team"
```

* Create the redirection function
```python
@app.route("/login/")
def login():
    # if someone tries to go to this page localhost:5000/login
    # redirected to the welcome page
    return redirect(url_for("greet_user"))
```

**Dynamic URL**

* Essentially allows the input of a url with a "new user" and returns a customised message
	* Further explanation is in the comments
```python
# the <> around the username, makes it 'dynamic', don't need to store username
# we get the data and display it back to them
@app.route("/user/<username>/")
# takes the username in the URL and passes it to the function .e.g.
# localhost:5000/chicken
# would
def welcome_user(username):
    # customised message to user
    return f"<h1>Hello {username}, welcome to the DevOps team!</h1?"
```

### Interacting With HTML

* Naming conventions are essential
* We need to create a `templates` folder in our directory
* Flask looks for this folder and anything inside the folder
* We will create index.html inside our templates folder

### BOOTSTRAP To Design Our Page With HTML, CSS, and JavaScript
