import datetime
from datetime import date

name = input("Please write your name: \n")
age = int(input("Your age: "))

current_year = int(date.today().year)
birth_year = current_year - age

print(f"OMG {name}, you are {age} years old so you were born in {birth_year}")

# Part 2, reassign age and name, figure out if birthday has happened

name = input("Please write your name: \n")
age = int(input("Your age: "))
date_of_birth = datetime.date(1997, 2, 14)  # hard-coded date of birth
today = date.today()

if date_of_birth.month - today.month < 0 and \
        date_of_birth.day - today.day < 0:
    print(f"{name}, you are {age} and your birthday has passed!")
else:
    print(f"{name}, you are {age} and I can't wait for your birthday")


# Part 3, hours alive

# abs() returns the absolute value of the difference between
# todays today and the implemented date of birth
hours_alive = abs(date.today() - date_of_birth). total_seconds() / 3600.0
print(f"You are {hours_alive} hours old")
