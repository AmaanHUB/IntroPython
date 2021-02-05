# Simple Bank Account
## Task
* Create an AccountHolderDetails class with private attributes name, address, age
* Create MyAccount which inherits from AccountHolderDetails which contains:
	* Attributes:
		* account_number (numeric type)
		* balance
	* Constructor those attributes as parameters
	* Methods:
		* deposit() - manages deposit actions
		* withdrawal() - manages withdrawal actions
		* bank_fees() - 5% of bank balance fee
		* display() - displays account details
* Create ManageAccount class, import from MyAccount, and call all the methods that are available

## Code Summary
### AccountHolderDetails
* Firstly the class was initialised with 3 private variables, denoted as such with the ```__```.
```python
class AccountHolderDetails:
    # Initialise AccountHolderDetails class
    def __init__(self, name, address, age):  # adding name, address, age as parameters
        # declaring variables as private
        self.__name = name
        self.__address = address
        self.__age = age
```
* The getters and setters were created so that these variables could be manipulated outside of the constructor due to the variables being private. One of these is shown below.
```python

    # Gets the name
    def get_name(self):
        return self.__name

    # Setter for the name, as people can change their name
    def set_name(self, new_name):
        self.__name = new_name
```
* N.B. These could be changed using the ```@property``` and ```@variable_name.setter``` flags.


### MyAccount
* Imported the ```AccountHolderDetails``` class and then initialised the ```MyAccount``` class.
	* ```account_number``` and ```balance``` made into private variables
	* ```name```, ```address```, ```age``` added to the first line of the constructor as these need to be declared when creating a ```MyAccount``` object.
	* The variables in the ```super().init()``` section must be added to show that we are using them from the ```AccountHolderDetails``` class.

```python
# import AccountHolderDetails class
from account_holder_details import AccountHolderDetails
# Class for MyAccount


class MyAccount(AccountHolderDetails):
    # Initialise class
    # need to add parameters like name here so they can be added
    # when object is created
    def __init__(self, account_number, balance, name, address, age):
        # allows one to use variables from class inheriting from
        super().__init__(name, address, age)  # tells that using these variable
        # declare parameters as private variables
        self.__account_number = account_number
        self.__balance = balance
```
* The getters and setters for the newly declared variables in the constructor are similar to the ones mentioned in the previous section so there is no need for showing examples of them.
* The functions to deposit and withdraw money are relatively simple, with adding or subtracting from the balance with the setter and getter methods for balance.
	* Both functions check whether the amount will be above 0 (as one cannot withdraw a negative amount of money, that is a withdrawal and vice versa) and gives an error message if not.
```python
    # Adds to balance using the set_balance() method
    def deposit(self, deposit_value):
        # check if the number depositing is positive
        if int(deposit_value) > 0:
            self.__balance = self.get_balance() + deposit_value
        # gives an error message if not positive
        else:
            print(f"{deposit_value} is an invalid value")

    # Reduces balance using the set_balance() method
    def withdrawal(self, withdrawal_value):
        # check if the number withdrawing is positive
        if int(withdrawal_value) > 0:
            self.set_balance(self.get_balance() - withdrawal_value)
        # gives an error message if not positive
        else:
            print(f"{withdrawal_value} is an invalid value")
```
* The ```bank_fees()``` method allows the percentage as a whole number, which is then passed into the function and converted into a decimal number, so that the current balance (of the account) can be multiplied by it.
```python
    # Implement the bank fees on the total balance
    def bank_fees(self, percentage):
        self.set_balance((self.get_balance() * (1 - (percentage / 100))))
```
* The output for ```display_details()``` uses getter methods of all the attributes, and displays them in a nice fashion.
```python
    # displays the full account details in a formatted way
    def display_details(self):
        print(f"Account No.: {self.get_account_number()}\n" +
              f"Balance: {self.get_balance()}\n" +
              f"Name: {self.get_name()}\n" +
              f"Address: {self.get_address()}\n" +
              f"Age: {self.get_age()}")
```

### ManageAccount
* This class essentially just calls the relevant methods from the MyAccount class.
* Firstly, MyAccount methods are imported with:
```python
# import class  from my_account
from my_account import MyAccount
```
* Initialisation of the class is followed, with no attributes.
```python
class ManageAccount:
    # initialisation of the class
    def __init__(self):
        print("Time to test all the methods available")
```
* Finally, the relevant methods are tested on a newly created object with print statements to check various factors.
```python
# Creation of an object for testing
account1 = MyAccount(1521031, 150, "Chicken", "123 Wing Rd.", 10)
# Testing the methods
account1.display_details()  # display input details
account1.deposit(100)  # add 100 to account1
print(account1.get_balance())  # display the balance only
account1.withdrawal(50)
print(account1.get_balance())  # display the balance only
account1.bank_fees(10)
print(account1.get_balance())  # display the balance only
account1.set_name("Chicken Little")
account1.set_address("Buck Lane")
account1.display_details()
```
### Future Improvements
* Make an 'interface' in the ManageAccount class, so that the relevant function can be selected. Using a while loop could be a start.
