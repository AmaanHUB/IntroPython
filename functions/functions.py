# Creating functions

# Syntax: def function_name():


def greeting(name):
    # Function to create a greeting, ideally each function only does one task
    print(f"Ahoy! Welcome aboard {name}, mi matey")


# if we execute this program now, it would display nothing
# as we have not called this function


# Syntax to call the function: function_name()

# calling our greeting function
greeting("Chicken")


# Create a new function that takes two arguments as ints
# and adds them together

def add(num1, num2):
    # creating an add function that takes 2 arguments
    print(num1 + num2)
    # Displaying the sum of args received


add(23, 15)


# def subtract(num1, num2):
#    # creating a function to subtract 2 args provided
#    print(num1 - num2)
#

def subtract(num1, num2):
    return num1 - num2

subtracted_value  = subtract(4, 3)


# Create one function that does each of:
# *, /, %, USE RETURN STATEMENTS


# returns vs print:
# print only pushes to output, but return makes it the result of the function


def multiply(num1, num2):
    # creating a function to multiply 2 args provided
    return num1 * num2


def divide(num1, num2):
    # creating a function to divide 2 args by each other
    return num1 / num2


def modulus(num1, num2):
    # creating a function to do the modulus on 2 args
    return num1 % num2


print(multiply(1, 2))
print(divide(4, 2))
print(modulus(5, 4))
