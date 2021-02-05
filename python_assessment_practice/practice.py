#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

# # Lists
# # declare a list with numbers 1 to 5, add the number 6 to the end of the list
# num_list = [1, 2, 3, 4, 5]
# print("Number List: " + str(num_list))
# num_list.append(6)
# print("Number List: " + str(num_list))
#
#
# # Tuples
# # create a tuple with values 1 to 5
# tuple_list = (1, 2, 3, 4, 5)
# print("Tuples List: " + str(num_list))
#
#
# # Sets
# set_list = {1, 2, 3, 4, 5}
#
# # when get to the number 3, want loop to stop
# # not just an index thing since sets can reorder
# for i in set_list:
#     print(i)
#     if i == 3:
#         break
#
# # Dictionaries
# # Declare a dictionary for a shopping list with three items
# shopping_list = {"banana": 0.3,
#                  "quorn": 5,
#                  "soup": 1
#                  }
# # show the
# print(type(shopping_list))
# print(shopping_list)
#
# # print price for one item
# print(shopping_list["soup"])


# # Replace the price for one of the items in the dictionary
# shopping_list["soup"] = 2
# print(shopping_list["soup"])

# Question 5
# function to add
# def add(num1, num2):
#     return num1 + num2


# print(add(1, 3))

# # CLASS Inheritance
# # Create a class called person with name and age class Person:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # create an object of the task
# testing = Person("chicken", 20)
# print(testing.name)
# print(testing.age)
#
#
# # class Student that inherits  from Person
#
#
# class Student(Person):
#     def __init__(self, name, age, student_id, course):
#       # the super() class method allows one to access methods and attributes from
#       # the parent class
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.course = course
#
#
# # instantiate an object
# student = Student("chicken1", 32, 1521031, "Eng74")
# print(student.name, student.age, student.student_id, student.course)

# INDEXING
# Create a dictionary with 4 shopping items with prices
# shopping_list = {"potatoes": 0.3,
#                  "tomatoes": 1,
#                  "passion fruit": 2
#                  }
# print(shopping_list)
#
# print(sum(shopping_list.values()))  # can use sum() method
#
#
# def added_dict(dictionary_name):
#     return sum(dictionary_name.values())
#
#
# # add item to dictionary, after tomatoes before end
# # adds kiwis at end of dictionary
# shopping_list["kiwis"] = 1
#
# print(shopping_list)


# create a list with items

list_shopping = ["kiwis", "bananas", "quorn", "sweet potatoes"]
print(list_shopping)

# iterate through list, if quorn is found in list, stop

for item in list_shopping:
    print(item)
    if item == "quorn":
        break
