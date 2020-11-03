# What is a Dictionary?
# A way of managing data more dynamically
# key value pairs to store and manage data
# Syntax : {"key": "value"}
# Use case:
# Can store any type of data

# Create a dictionary
devops_students_data = {
    "key": "value",
    "name": "chicken",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lesson_names": ["operators", "data types", "variables"]
}

# print(devops_students_data)
# print(type(devops_students_data))

# display the data for a specific key by using a key name
# print(devops_students_data["name"])
# print(devops_students_data["completed_lessons"])
#
# print(devops_students_data.keys())  # print the keys for dict
# print(devops_students_data.values())  # print the values for dict
# print(devops_students_data["completed_lesson_names"][1])  # way of getting out specific list value

# How can i change a specific key value?
# devops_students_data["completed_lesson_names"] = 3
# print(devops_students_data["completed_lessons"])
#
# print(devops_students_data.items())  # print everything in the dictionary
# print(type(devops_students_data.items()))


# TASK --
# create a new dictionary to store user details
# all the details that you utilised in the last task, last task name, DOB, Address, course, grades
# remove, add, replace, display type of items
# create a list of hobbies within it (at least)
# display hobbies in reverse order

student_details = {
    "task_name": "dictionary",
    "DOB": 20200101,
    "Address": "123 Street Road",
    "Course": "DevOps",
    "Grades": "A",
    "Hobbies": ["running", "baseball", "eating"]
}

# print(student_details)
#
# student_details["Grades"] = "A*"  # replace something in dictionary
# print(student_details["Grades"])
#
# student_details.update({"Address": "321 Road Street"})  # replace value in dictionary
# print(student_details["Address"])
#
#
# print(type(student_details.items()))  # display type of items
#
# print(student_details["Hobbies"][::])  # display all hobbies
# print(student_details["Hobbies"][::-1])  # display all hobbies in reverse
#
# student_details.pop("DOB")  # remove item in dictionary
# print(student_details)
#
#
#


student_details["Hobbies"].append("sleeping")  # add to list in dictionary
print(student_details["Hobbies"])


student_details["Hobbies"].remove("baseball")  # remove from list in dictionary
print(student_details["Hobbies"])
