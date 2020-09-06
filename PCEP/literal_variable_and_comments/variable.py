#!/usr/local/bin/python3.8

# assigning a string to a variable
name = "Nabeel"

print ("Hello, my name is " + name)

# replacing the content of an existing variable
name = "Majid"

print ("Hello, my new name is " + name)

# Adding to an existing variable
name += " Ahmed"

print ("Hello, my full name is " + name)

# Assining an integer to a variable (same as assigning string)
# You mix strings and intergers in a print statement so easily. Two methods to solving this
# - Method 1: Make them all either a string / integer
# - Method 2: Make sure the print function is aware of the incosistancy

age = 28

# Method 1
print ("I am " + str(age) + " years old")

# Method 2
print ("I am %d years old" %age)