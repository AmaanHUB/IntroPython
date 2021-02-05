# Python Test Driven Development Task

## Task
- Create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- Create a class and method to write code to pass the test
- Create a test to check if the given values are positive
- Create a method in the class to pass the test


## Code Summary

### Testing Functions
* Create a file named ```test_task.py``` or something similar. As long as the format is ```test_something``` or ```testsomething``` it should be fine, as pytest searches for the keyword test
* The relevant modules are imported as well as the class contains the functions that are being tested.
```python

# import testing libraries
import pytest
import unittest

# import class
from task import Task
```

* Class should be initialised whilst inheriting from the unittest library with ```unittest.TestCase```
```python
# class made, inherit from unittest.testcase
class TestTask(unittest.TestCase):
```
* Test methods created with the ```assertTrue``` or ```assertFalse``` since the functions (made after this) have been decided to return true or false depending upon the relevant criteria
```python
    # testing whether a number is divisible or not
    def test_divisable(self):
        # assertTrue checks if output gives true, which this should
        # as 6 % 3 = 0, which returns true in function
        self.assertTrue(self.test.divisible(6, 3), "This should be True")
        # assertFalse checks if output gives false, which this should do
        # as 7 % 3 = 1, which returns false in the function
        self.assertFalse(self.test.divisible(7, 3), "This should be False")

    def test_positive(self):
        # assertFalse checks if output gives false, which this should do
        # -1 should return a False as is negative, assertTrue should be the
        # opposite
        self.assertFalse(self.test.positive(-1), "This should be False")
        self.assertTrue(self.test.positive(15), "This should be True")
```
* It should be noted than an object of the class that one is testing needs to be initialised for these tests to work (and apply the relevant functions from the non-test class to)
```python
    # initialise an object to apply the methods to in testing
    test = Task()
```
* To run the tests, in the command line run:
	* The latter only works if you are in the virtual environment that is running python
``` python -m pytest ```  or ``` pytest ```

* **None of these tests should pass yet**, as the file with the functions as well as the relevant functions has not been created yet.

### Functions
* In the function file, the criteria for the methods is met within the 'Task' class
	* The modulus is used to check whether the two numbers are divisible by each other (with no remainder)
	* Positive number is found by checking if it is greater than 0
```python
class Task:

    # function to check if numbers are divisible by each other
    def divisible(self, num1, num2):
        # if modulus is 0, then they are wholly divisible
        if num1 % num2 == 0:
            return True
        else:
            return False

    # function to check if a number is positive or not
    def positive(self, number):
        # if higher than 0, is a positive number
        if number > 0:
            return True
        else:
            return False
```

* Finally, one can use the tests written with the previously mentioned python commands. If the tests are failing, one can use ```pytest -v``` to get some more information and start debugging what went wrong
