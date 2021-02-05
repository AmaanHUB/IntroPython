# Simple DNA Base Counting
The Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:

20 12 17 21

NOTE -> Must be in class and method format

## Summary Of Code

* Initialised a 'base set' for the nucleotide sequence and print a message for the user to see at the beginning, as well as generally initialise the class.
```python
    # instantiate a class
    def __init__(self):
        # print a message to say what it is
        print("DNA Base Counter")
        # define the allowed bases
        self.bases = ["A", "C", "G", "T"]
```
* The main function is below, with the code commented to elaborate on what does what.
```python
    # Function to count the number of DNA bases in the given dataset set
    def base_counting(self, dataset):
        # convert the dataset into capitals
        dataset = dataset.upper()
        # initialise the variable for counting the individual bases
        # this area has room for improvement perhaps
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        # instead of a loop, could use count() method
        # loops through data string (nucleotide sequence)
        for letter in dataset:
            # informs user that sequence has non-standard characters in it
            if letter not in self.bases:
                print("This contains non-standard DNA bases!")
            # checks if letter is in sequence and adds it to its counter
            elif letter == "A":
                a_count = a_count + 1
            elif letter == "C":
                c_count = c_count + 1
            elif letter == "G":
                g_count = g_count + 1
            else:
                t_count = t_count + 1
        # print out counts in a nice formatted manner
        print(f"A: {a_count}\nC: {c_count} \nG: {g_count}\nT: {t_count}")
```
