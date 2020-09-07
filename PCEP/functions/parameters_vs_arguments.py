#!/usr/local/bin/python3.8

# Parameters: When you are creating the functions, you are writing the parameters

# Arguments: When you are calling on the functions, you are specifying the arguments.

'''
def add_function( parameter, parameter )    # Creating the function
    parameter + parameter

add_function(arugment, argument)            # Calling the function
'''

##########################################
# Assigning arguments
##########################################

# When you are not aware of the argument order, you can assing the arguments to keyword
# i.e. keyword arugment

def users_car(name, age, model):
    return f'{name} is {age} and drives a {model}'

print ( users_car('Richard', 33, 'Honda Civic') )                    # Postional argument: knowing the order

print ( users_car(age=40, name='Michael', model='Ford Focus') )      # Keyword argument: not knowing the order

print ( users_car('Sikandar', model='Ford Focus', age=24) )          # Mixture: Positional + keyword argument

# Limitation of mixture: Once you start using positional arugement, you must continue using it only.



##########################################
# Default arguments for parameter
##########################################

def can_drive(age, driving_age=16):
    return age >= driving_age

output = can_drive(10)

print (output)                  # False 


# But you can overide the system and trick it

output = can_drive(10, 5)       # or driving_age=5

print (output)                  # True - You've overwritten the systems default driving_age to 5 years old!



# Note: once you've writen a default argument, all parameters that follow must be default 
# e.g.

def can_drive(age, driving_age=16, car_type='standard'):
    return age >= driving_age