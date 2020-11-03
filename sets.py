# Sets (and frozen sets) - data collections with sets
# indexing, NO INDEXING IN SETS (UNORDERED)

#  Syntax: {} for sets

car_parts = {"wheels", "doors", "radio"}
print(car_parts)  # print out in different order each time

# managing data with sets
# add an item to a set
car_parts.add("seatbelts")
print(car_parts)

# remove an item from a set
car_parts.remove("wheels")
print(car_parts)
