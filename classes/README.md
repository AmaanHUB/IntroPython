# Python Classes

## Object Oriented Programming (OOP)
There are four pillars of OOP:
* Inheritance
	* Elimates redundant code
		* We can use all functions and variables from the parent class
* Encapsulation
	* Reduces complexity and increases reusability. It can also reduce access, such as private methods and whatnot.
* Abstraction
	* Reduces complexity and isolate the impact of changes
* Polymorphism (Poly - many, morphism - forms):
	* A programming language's ability to process objects differently depending on their data type or class. **Ability to redefine methods for derived classes**. Makes refactoring code easier .i.e. allows us to change behaviours or attributes/variables.

### What Are Classes?

* Class is the main factor that is used to implement any of the pillars


#### Why Do We Use Them?
* Extensibility!
* Classes are a way of bringing data and functionality together

#### How Do We Make Classes?

* Syntax:
	* ```class Class_name```
	* starts with capital letter always


```
class Dog:

    animal_kind = "Canine is running"
# defining class variable

    def bark(self):
        # self refers to current class
        return "woof"


# to execute a class, we have to create an object of this class
toffee = Dog()  # creating an object/instance in our Dog class

print(toffee)  # would output memory location of object

# print(toffee.animal_kind)
# print(toffee.bark())


toffee.animal_kind = "Big Dog"  # only animal_kind is changed for toffee object
print(toffee.animal_kind)

basil = Dog()  # instantiating basil in Dog class
print(basil.animal_kind)
print(basil.bark())
```

* **Syntax with an __init__ method (preferred way):**
```
def __init__(self, arg1, arg2):
			self.arg1 = arg1
			self.arg2 = arg2
			self.other_arg = other_arg

```
```

    def __init__(self, name, colour):  # initialise Dog class
        self.name = name
        self.colour = colour
        self.animal_kind = "Canine"  # instialisation of the class

fido = Dog("fido", "brown")  # instantated an object of a Dog class
```
