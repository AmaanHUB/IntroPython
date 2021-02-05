# Functions in Python
## What Are Functions And Why Are They Used?
* **DRY**:
    * Don't
    * Repeat
    * Yourself

* Essentially prevent one from repeating blocks of code
## How Can We Create A Function?
* Syntax:
    * ```def function_name():```
	* Calling a function:
		* ```function_name()```
* Returns vs print:
	* print only pushes to output, whereas return gives the 'result' of the function

```
# Creating functions

# Syntax: def function_name():


def greeting(name):
    # Function to create a greeting, ideally each function only does one task
    print(f"Ahoy! Welcome aboard {name}, mi matey")


# if we execute this program now, it would display nothing
# as we have not called this function


# calling our greeting function
greeting("Chicken")

```
* Create a new function that takes two arguments as ints and adds them together

```
def add(num1, num2):
    # creating an add function that takes 2 arguments
    print(num1 + num2)
    # Displaying the sum of args received


add(23, 15)


def subtract(num1, num2):
    # creating a function to subtract 2 args provided
    print(num1 - num2)


subtract(23, 15)
```


* **TASKS**:
	* Create one function that does each of:
		*	\*, \/, \%, USE RETURN STATEMENTS

```

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
```

### Function Best Practices
* Small blocks of code in any function that does one job **(KISS)**
* Pseudocode - one line of explanation
* Create hints in simple bullet points or pointers
* Comments regarding your function results
