# Loops - for and while loops

# For loop is used to iterate through the data
# Syntax: for variable_name in name_of_data_collection

shopping_list = ["eggs", "milk", "banana"]
print(shopping_list)

for items in shopping_list:
    if items == "milk":
        print(items)
        # break  # breaks out of the loop


# Small dictionary task
student_details = {
    "task_name": "dictionary",
    "DOB": 20200101,
    "Address": "123 Street Road",
    "Course": "DevOps",
    "Grades": "A",
    "Hobbies": ["running", "baseball", "eating"]
}

print("Student detail keys:")
for items in student_details.keys():
    print(items)

print("Student detail values:")
for items in student_details.values():
    print(items)


