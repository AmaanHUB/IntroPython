# A Simple Website With Flask

## Prerequisites

* Install relevant libraries
```sh
pip install flask
```

## App

* Import the relevant libraries
```python
# import the relevant libraries
from flask import Flask, url_for, redirect, render_template
```

* Create an instance of `Flask`
```python
# create an instance of an app
app = Flask(__name__)
```

* A few 'functions' to redirect to the relevant html pages that will be shown later
```python
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
```

## HTML Files and Templates

* A folder is created entitled `templates`, as `Flask` will only look for this folder and what is inside it
* A file entitled `layout.html` should be created with the following content inside. This shall be the 'parent' file for many of the other templates, that will get their layout from
	* Relatively self-explanatory with the comments
```html
<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
	</head>
	<body>
		<div class="container">
				<h1 class = "logo">Amaan's Web App</h1>
				<strong><nav>
								<!-- Section here to add the links -->
					<ul class = "menu">
							<!-- call the various pages to link to -->
							<li><a href = "{{ url_for("home") }}">Home</a></li>
							<li><a href = "{{ url_for("about") }}">About</a></li>
					</ul>
				</nav></strong>
		</div>
		<div class = "container">
				<!-- helps link to files that extend from this, will be replaced with relevant stuff in those files-->
				{% block content %}
				{% endblock %}
	</body>
</html>
```

* Another three files are created to inherit from the `layout.html` file, of which the python functions redirect to (home, about and login)
* The `login.html` is shown below. The `{% extends "layout.html" %}` causes it to inherit from the `layout.html` file. The `{% block content %}` and `{% endblock %}` denote where the `layout.html` inherited parts wll be
	* In the head section, there are some `script` and `link` sections, which refer to a theme and relevant css style.
	* Within the body, the `form` part refer to the parts one would enter the username and password when one is logging in
		* Though the login page does not go anywhere at this moment unfortunately, as that would involve linking it to a database that stores passwords and another page that is hidden behind a successful login attempt
```html
<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
		<title>Login</title>
		<link href="css/main.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->
	</head>
	<body>
	{% extends "layout.html" %}
	{% block content %}

<div class="wrapper fadeInDown">
  <div id="formContent">
    <!-- Tabs Titles -->

    <!-- Icon -->
    <div class="fadeIn first">
      <img src="http://danielzawadzki.com/codepen/01/icon.svg" id="icon" alt="User Icon" />
    </div>

    <!-- Login Form -->
    <form>
      <input type="text" id="login" class="fadeIn second" name="login" placeholder="login">
      <input type="text" id="password" class="fadeIn third" name="login" placeholder="password">
      <input type="submit" class="fadeIn fourth" value="Log In">
    </form>

    <!-- Remind Passowrd -->
    <div id="formFooter">
      <a class="underlineHover" href="#">Forgot Password?</a>
    </div>
  </div>
</div>
	{% endblock %}
	</body>
</html>
```

* The `home.html` and `about.html` files are basically the same with some changes in the content of the text, with the `about.html` file hopefully being full of actual content about the creator. See below for both of these files
```html
<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
		<title>Home</title>
	</head>
	<body>
	<!-- this extends the the layout class, and tells where to put the relevant stuff -->
	{% extends "layout.html" %}
	{% block content %}
	<div class = "home">
			<h1>Testing home page</h1>
	</div>
	{% endblock %}
	</body>
</html>
```
```html
<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
		<title>About</title>
	</head>
	<body>
	<!-- this extends the the layout class, and tells where to put the relevant stuff -->
	{% extends "layout.html" %}
	{% block content %}
	<div class = "about">
		<h1>About me</h1>
		<p> This is a small site that shows off a section of my portfolio, as well as practice for creating simple websites in Python with Flask</p>
	</div>
	{% endblock %}
	</body>
</html>
```

### CSS

* CSS layouts can be used, as is shown in the login file. Though this is not particularly working at the moment. Needs more investigation.

