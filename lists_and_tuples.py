# # Collections in Python
#
# # Lists
# # Lists are mutable
# # We can add, remove, change an item
# # Indexing starts with 0
# # "Hello world!"
# # Syntax: ["word1", "word2", "word3"]
#
#
# # Create a list
# shopping_list = ["apples", "milk", "bread"]
# print(shopping_list)
# print(type(shopping_list))
#
# # Look at indexing in the list items
#
# print(shopping_list[1])
# print(shopping_list[-1])
# print(shopping_list[1:])  # print from index to end (inclusive)

# Managing a list

# Add an item to this list

# shopping_list.append("eggs")
# print(shopping_list)
#
# # How to remove an item from our list
# shopping_list.remove("apples")
# print(shopping_list)
#
#
# # pop() deletes last item from the list that we appended earlier
# shopping_list.pop()
# print(shopping_list)


# How can I replace an item in my list?
# shopping_list[1] = "chicken"
# print(shopping_list)

# Can we have mixed data types in the list?
# mixed_shopping_list = [1, 2, 3, "apples", "milk", "bread"]
# print(mixed_shopping_list)
# YES

# Task: create a mixed data type list of 7 items
# display the type of the data
# add, delete, replace, pop()
# use indexing to print the list in reverse order


mixed_data_type_list = ["brown", "red", 54, "yellow", 13, 67, "pink"]
print(mixed_data_type_list)
print(type(mixed_data_type_list))

mixed_data_type_list.append(43)
print("Append: ", mixed_data_type_list)

mixed_data_type_list.remove("brown")
print("Remove: ", mixed_data_type_list)

mixed_data_type_list[5] = "chicken"
print("Replace: ", mixed_data_type_list)

mixed_data_type_list.pop()
print("Pop: ", mixed_data_type_list)

print("Reverse: ", mixed_data_type_list[::-1])