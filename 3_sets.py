# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/python_sets_add.asp

# Create a set called fruits:
# fruits = {"apple", "banana", "orange"}
#
# Write a function add_fruit(fruit_set, new_fruit) that:
#   - adds new_fruit to the set
#   - returns the updated set
#
# Call the function with "kiwi" and print the result.

# Write your code here:
fruits = {"apple", "banana", "orange"}
def add_fruit(fruit_set, new_fruit):
    fruit_set.add(new_fruit)
    return fruit_set

print(add_fruit(fruits, "kiwi"))
