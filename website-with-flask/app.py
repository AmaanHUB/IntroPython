#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# import the relevant libraries
from flask import Flask, url_for, redirect, render_template

# create an instance of an app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/login/")
# function for logging in, doesn't go anywhere yet
def login():
    return render_template("login.html")


# if it is run from this file, run this
if __name__ == "__main__":
    app.run(debug=True)
