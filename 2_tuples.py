# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_tuples_unpack.asp

# You are given the following tuple:
# person = ("Alice", 21)
#
# Write a function print_person(info) that:
#   - unpacks the tuple into name and age
#   - prints: "Alice is 21 years old."
#
# Call the function with person.

# Write your code here:
person = ("Alice", 21)
name,age=person
def print_person(name,age):
    print(name ,"is ",age, "yers old")
print_person(name,age)


