# Calculator With OOP

## Task
* Build a basic object Orientated Calculator
* Phase 1: build a simple calculator class containing add, subtract, multiply, divide.
* Phase 2 (Expand by creating):
	* Divisible by method that returns true or false dependent on the outcome
	* Work out and return the area of a triangle
	* Inch to cm converter
	* NOTE -> Must be in class and method format

## Summary Of Code

* Addition, subtraction and multiplication of two numbers:
```python
    # Add two numbers together
    def add(self, num1, num2):
        return num1 + num2

    # Subtraction of two numbers
    def subtract(self, num1, num2):
        return num1 - num2

    # Multiplication of two numbers
    def multiply(self, num1, num2):
        return num1 * num2
```
* Division, with a check to prevent infinity as an answer:
```python
    # Division of two numbers
    def divide(self, num1, num2):
        # checks if one of the numbers is 0, as that would give infinity
        if (num1, num2) == 0:
            print("Cannot divide by 0")
        else:
            return num1 / num2
```
* Printing true or false depending on whether the modulus is 0 or not:
```python
    # Give true or false if number is fully divisible
    def true_divide(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False
```
* Finding the area of a simple triangle with the following formula:
```python
    def true_divide(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False
```
* Finding the area of a simple triangle with the following formula:
```python
    # Print out the area of a triangle
    def triangle_area(self, base, height):
        return 0.5 * base * height
```
* Converting inches to centimetres:
```python
    # convert inches to centimetres
    def inch_to_cm(self, inch):
        return inch * 2.54
```
