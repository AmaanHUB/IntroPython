#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

# Getters and setters
# Why?
# To hide the data - separation of concern


# create a class called student

class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company


    def getStudent(self, value):
        self.__name  # __ are used to hide the data

    def setStudent(self, value):
        self.__name = value


student = Student("chicken", "sparta")


print(f"Student name is {student.getStudent()}")
