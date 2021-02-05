# Python OOP Example Lesson

## Step 1
* Creating an **Animal** class as our parent/super class

```python

class Animal:

    def __init__(self):  # initialising the Animal class
        self.alive = True
        self.spine = True  # assume all have spine for now
        self.lungs = True
        self.eyes = True

    # create behaviours as functions/methods
    def breathe(self):
        return "Just keep breathing"

    def move(self):
        return "Up, down, left, right"

    def eat(self):
        return "Nom, nom, nom"

    def procreate(self):
        return "Find partner/s"
```

## Step 2
* Create a **Reptile** class as the child class
//TODO example of super().__init__() part
### Why?
* So we can inherit from our parent class
* Abstraction


## Step 3
* Create a **Snake** class as the child class of the reptile class
//TODO example of super().__init__() part

## Step 4
//TODO example of super().__init__() part

## __name__ and __main__

These are used to check if the code is run from the current file directly or a different file/importing it.
* We will create 2 files and use ```__name__``` and ```__main__``` in both files and the outcome will show the difference
