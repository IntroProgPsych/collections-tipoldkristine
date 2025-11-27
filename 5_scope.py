# https://www.w3schools.com/python/python_variables_global.asp
# https://www.w3schools.com/python/python_scope.asp

# Create a global variable:
# counter = 0
#
# Write a function increase_counter() that:
#   - uses the 'global' keyword
#   - increases counter by 2 each time it is called
#   - prints the updated value
#
# Call the function three times and observe how the global variable changes.
# 
# Write your code here:

counter = 0
def increase_counter():
    global counter
    counter += 2
    print(counter)
increase_counter()
increase_counter()
increase_counter()
increase_counter()
increase_counter()
increase_counter()
