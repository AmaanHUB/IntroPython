# Scrabble

Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided.

```text
Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
```

## Explanation of Code
* This section of code creates lists with the relevant letters as well as initialising the class itself. The values are not assigned to the letters yet.
```python
class Tiles:
    # initialise the class
    def __init__(self):
        # using a list for each of the letter groups
        self.value_one = ["A", "E", "I", "O", "L", "N", "R", "S", "T"]
        self.value_two = ["D", "G"]
        self.value_three = ["B", "C", "M", "P"]
        self.value_four = ["F", "H", "V", "W", "Y"]
        self.value_five = ["K"]
        self.value_eight = ["J", "X"]
        self.value_ten = ["Q", "Z"]
```
* This small function allows a user to input their own word of choice interactively.
* The return statement allows one to 'pipe' it to the larger function that does most of the work.
```python
    # added a small function to help the user input a word of choice
    def choose_word(self):
        word = str(input("Please enter a word: "))
        return word
```
* The below function assigns values to the letters in the lists made during the intialisation, as well as looping through the word and outputting the score of each letter.
* This also has functionality of taking user input by using the previously mentioned function.
```python
    #  function to find the score of a word
    def score(self):
		# this uses the choose_word() function to assign user input to the word variable
        word = self.choose_word()
        # capitalise the word so can compare easily to list and output nicer
        word = word.upper()
        #  initialise the score variable so can add to
        score = 0
        #  for loop to loop through the word
        for letter in word:
            # if-elif-else statements to add to the score
            if letter in self.value_one:
                score += 1  # add to the running score
                print(f"{letter}: 1")  # display the value of the letter
            elif letter in self.value_two:
                score += 2
                print(f"{letter}: 2")
            elif letter in self.value_three:
                score += 3
                print(f"{letter}: 3")
            elif letter in self.value_four:
                score += 4
                print(f"{letter}: 4")
            elif letter in self.value_five:
                score += 5
                print(f"{letter}: 5")
            elif letter in self.value_eight:
                score += 8
                print(f"{letter}: 8")
            elif letter in self.value_ten:
                score += 10
                print(f"{letter}: 10")
            else:
                print("Not a letter")
        print(f"{word} : {score}")
```
