# Loop Task

# Make a loop with a range that says 'hello' 10 times
# Create another loop with a range that asks for names
# and appends it to list_names
# Make a loop that iterated over each name in list_name and
# format's it into lowercase in a new variable called
# list_names_lower
# Iterate over the list of values to find if they are even


# Hello 10 times
for i in range(10):
    print("Hello")

# List_names

number = int(input("How many names do you wish to input?: \n"))
list_name = []

for items in range(number):
    list_name.append(input("Name: \n"))

print("Names list: \n")
print(list_name)

# Iterate over list_name and format to lowercase
list_names_lower = []

for items in list_name:
    list_names_lower.append(items.lower())

print("Names List in lower case: \n")
print(list_names_lower)

# Words even length?
# first get the word, then find length of word

for items in list_name:
    if len(items) % 2 == 0:
        print(items + " is EVEN")
    else:
        print(items + " is ODD")
