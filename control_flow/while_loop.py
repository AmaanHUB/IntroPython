# Creating a while loop
# break and continue are key words that we can use to control of our program
# Syntax: while variable_name condition value:

# number = 0
#
# while number < 10:
#     print(f"It's working → {number}")
#     if number == 4:
#         break  # break out of loop if reaches 4
#     number += 1  # increment by +1

# Take user input with while loop

user_prompt = True

#  if not a digit in age, will continually loop until an age less than 117 is added
while user_prompt:
    # user input here
    age = input("Please enter your age: \n")
#  isdigit() checks if input is all in digits
    if age.isdigit() and int(age) < 117:
        user_prompt = False  # breaks out of while, since no longer true
    else:
        print("Please provide age in digits")

print(f"Your age is {age}")
