#!/usr/local/bin/python3.8

# Functions enable to call on written code multiple times without having to repeat ourselves.
# i.e. code reuse

# FUNCTIONS RULE
# - function names should start with lower case letter or underscore _ (hidden function)


'''
def function_name(parameter, patemeters, ...):
    pass
'''

# Create the function
def print_name(name):
    print('User\'s name is:', name)

# Call the function
print_name('Mike')


'''
Functions do not return values / results. 
The example above will print the results because it is told but you will not be able to assing the
result to anything.
'''

output = print_name('Richard')

print (output)           # none

'''
To return a value you must use the 'return' statement
'''

def add_two(num):
    return num + 2

output = add_two(2)

print (output)          # 4  - it worked! It returned the result from the function


#########################################
# Multiple parameters
#########################################

def mult(num1, num2):
    return num1 * num2

print ( mult(5, 5) )

