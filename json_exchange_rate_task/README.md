# JSON Exchange Rate Task
* Get the exchange_rates.json file
* Display all the data in the .json file
* Iterate through the data and display exchange rate by country

## Code Summary

* Import the relevant libraries
```python
# import libraries needed
import json
```
* Open up the json file, convert it into a dictionary and assign to a variable
```python
# opening up the json file with read permissions and
# naming it as something easy to use
with open("exchange_rates.json", "r") as jsonfile:
    # create a dictionary from the json file
    # the ["rates"] gets the nested dictionary and turns it
    # into a non-nested simple dictionary of just rates
    exchange_rates = json.load(jsonfile)["rates"]
```
* In a function, loop through the dictionary and output the exchange rate in a formatted fashion
```python
# Function to print the exchange_rates
def print_exchange_rates():
    # loop through the exchange_rates dictionary
    for x in exchange_rates:
        # prints out the key in capitals with the exchange rate next to it
        print(f"{x.upper()}: {exchange_rates[x]}")
```
* This function can then be called with:
```python
print_exchange_rates()
```
