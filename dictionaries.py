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
print(devops_students_data["name"])
print(devops_students_data["completed_lessons"])

print(devops_students_data.keys())  # print the keys for dict
print(devops_students_data["completed_lesson_names"][1])  # way of getting out specific list value