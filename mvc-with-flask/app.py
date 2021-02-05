#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# import module
from flask import Flask, jsonify, redirect, url_for, render_template


# create an instance an app
app = Flask(__name__)


# in a list to make it easier to transfer it into json
student = [
    {"id": 0,
     "title": "Dr.",
     "first_name": "Chicken",
     "last_name": "Little",
     "course": "DevOps"
     }
]

# decorator - to create our API/URL for user to access our data in browser
# string is HTTP url
@app.route("/")  # localhost:5000 is default port for flask
# function runs when URL/API is accessed
def home():
    return """<h1>This is a team from the DevOps consultants,
                celebrating a WOW moment!</h1>"""  # put html stuff here


# Creating our own API to display data on the specific route/URL/end point/API
# [GET] will add this API/URL to home path
# also uses HTTP GET
@app.route("/api/v1/student/data/", methods=["GET"])
# goes to 127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(student)  # transform data into Json
    # Utilising Extract Transform Load

# greet the user function ITERATION ONE
# @app.route("/welcome/")  # trailing slash, so user can access with or without on URL
# def greet_user():
#     return "Ayup, welcome to the DevOps team"

# greet the user function ITERATION TWO with html document
@app.route("/welcome/")  # localhost:5000/welcome/
def greet_user():
    return render_template("welcome.html")

# find out the module to redirect the user back to the specific page (welcome)
@app.route("/login/")
def login():
    # if someone tries to go to this page localhost:5000/login
    # redirected to the welcome page
    return redirect(url_for("greet_user"))


# the <> around the username, makes it 'dynamic', don't need to store username
# we get the data and display it back to them
@app.route("/user/<username>/")
# takes the username in the URL and passes it to the function .e.g.
# localhost:5000/chicken
# would
def welcome_user(username):
    # customised message to user
    return f"<h1>Hello {username}, welcome to the DevOps team!</h1?"


# similar to url as above
# @app.route("/index/")  # based off original index file, change name
# def index():
#     # calls the HTML file with python rendering (in templates directory)
#     return render_template("index.html")


# testing the inheritance in the template pages
@app.route("/testing/index")
def testing_templates():
    return render_template("index.html")


# if it is this file, run this
if __name__ == "__main__":
    app.run(debug=True)
