# Control Flow
## if, elif, and else statements
* A conditional statement that can determine the outcome of program flow
* Syntax:
    * ```if then condition```
```

# age = 10
#
# if age >= 15:
#     print("You are the correct age to watch the film")
# elif age < 15:
#     print("Sorry, you are too young to watch the film.")
# else:
#     print("Error, try again later")

# TASK 1
# check age restrictions for (a cinema) with control flow, if, elif and else
# 18, 15, 12, PG
# else block should ensure to display message if other conditions do not match
#
#
# age = int(input("How old are you? \n"))
#
# if age >= 18:
#     print("You can watch any film")
# elif age >= 15:
#     print("You may watch this 15 classified film")
# elif age >= 12:
#     print("Watching films rated 12? Go for it")
# else:
#     print("Better have your parents")

```
## for loops and while loops
* For loops are for iterating throughout any data type
    * Syntax: 
        * ```for variable_name in name_of_data_collection:```
```
# simple list
shopping_list = ["eggs", "milk", "banana"]
print(shopping_list)

# iterating through shopping_list
for items in shopping_list:
    # if "milk" is found, print out
    if items == "milk":
        print(items)
        # break  # breaks out of the loop


# Small dictionary task

# Dictionary called student_details
student_details = {
    "task_name": "dictionary",
    "DOB": 20200101,
    "Address": "123 Street Road",
    "Course": "DevOps",
    "Grades": "A",
    "Hobbies": ["running", "baseball", "eating"]
}

print("Student detail keys:")

# Loop to print out the keys within the dictionary
for items in student_details.keys():
    print(items)

print("Student detail values:")

# Loop to print out the values within the dictionary
for items in student_details.values():
    print(items)
```
### while loops
* Monitoring use rather than just iterating through data
* Tends not to be regularly used in the industry
* We use key words to ```break``` and ```continue``` that help control the flow of our loop



* Creating a while loop:
    * break and continue are key words that we can use to control of our program
* Syntax: 
    * ```while variable_name condition value:```
```
number = 0

while number < 10:
    print(f"It's working → {number}")
    if number == 4:
        break  # break out of loop if reaches 4
    number += 1  # increment by +1

# Take user input with while loop

user_prompt = True

#  if not a digit in age, will continually loop until an age less than 117 is added
while user_prompt:
    # user input here
    age = input("Please enter your age: \n")
#  isdigit() checks if input is all in digits
    if age.isdigit() and int(age) < 117:
        user_prompt = False  # breaks out of while, since no longer true
    else:
        print("Please provide age in digits")

print(f"Your age is {age}")
```