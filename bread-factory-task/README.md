# Bread/Naan Factory Task

## Tasks

This exercise is going to bring together lots of concepts.

### Learning Outcomes
Learning outcomes include:
- git
- github
- functions
- TDD
- Separation of concerns - this is important do not ignore!
- DRY code
- DOD


## Installing and running
To run the naan factory do the following:

```python
import naan factory
run factory()
```


### TDD - test driven development

1. write the test
2. run it, and read the error
3. code and make it pass the test

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

##### Unit Tests

Test single pieces of code. Like a function.

**base of a test**
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with know variables
- asserting for expect output


### User stories for Naan Factory

```
#1
As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake dough with dough to get naan.

#3
As a user, I can user the run factory with water and flour and get naan.

```

## Acceptance Criteria

* you have written tests
* test pass
* you have written more test to make sure everything works as indented
* all user stories are satisfied
* code does not break
* code has exit condition
* DOD is followed

# First Iteration

## Testing
* In a file called ```test_naan_factory.py```, first imported the relevant testing libraries and the class to be tested
```python
# import testing libraries
import pytest
import unittest

# import class to test
from naan_factory import NaanFactory
```
* Declare the testing class that inherits from ```unittest.TestCase```
```python
class NaanFactoryTest(unittest.TestCase):
```
* An object should be declared to be used for the testing methods
```python
    naan_test = NaanFactory(True, True)
```
* The methods for testing are created with ```assertTrue``` in the body. This could have used ```assertEqual``` if one decides to use Strings or integers rather than booleans which I had decided to do originally
```python
    def test_make_dough(self):
        # see if it has dough and water, should come out as True
        self.assertTrue(self.naan_test.make_dough())

    def test_bake_dough(self):
        # see if it has dough to get the naan, will be True
        self.assertTrue(self.naan_test.bake_dough())

    # test run_factory method()
    def test_run_factory(self):
        self.assertTrue(self.naan_test.run_factory())
```

### Running The Test
```python -m pytest```
* The command should give all errors, given that the class that we would be testing has not been made yet


## The Code!

* The class is declared with a constructor, used for initialising the class and any objects that come from it
```python
class NaanFactory:

    # Initialises class with booleans whether flour and water available
    # next iteration should make them boolean
    def __init__(self, water_available, flour_available):
        self.water_available = water_available
        self.flour_available = flour_available
```
*  All the functions are very similar at this stage, returning a boolean, which can then be passed onto the next one. The comments explain how they work
```python
    # method to make the dough
    def make_dough(self):
        # checks if water and flour are present
        if self.water_available is True and self.flour_available is True:
            # returns true if both are present
            return True
        else:
            return False

    # method to bake dough based upon presence of dough
    def bake_dough(self):
        # if make.dough() returns True, then this method shall too
        if self.make_dough() is True:
            return True
        else:
            return False

    # method to essentially run the factory
    def run_factory(self):
        # if both functions return true, then return true
        if self.make_dough() and self.bake_dough():
            return True
        else:
            return False
```

# Second Iteration
* TODO → add setters and getters for water_available and flour_available to be used within the ```run_factory()``` method
	* Interactive while loop within this method, just to change whether there is flour and water
* TODO → Some extra testing functions maybe? Though will have to see what happens with the interactive section
