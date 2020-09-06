#!/usr/local/bin/python3.8

print ('Dictionary')

# A dictionary maps a key to a value or in the generic sense, a word to a defition (running: the action or movement of a runner.)
# dictionary => { key : value }
# Dictionaries don't care about position, just the key conent. Useful when you only care about the key too i.e. name of a person
# The key must be any immutable type e.g. a string = Michal
# each key must be unique (becuase the position is not garanteed to be unique i.e. you can have two Michals == error)

users_age = { 'Matt': 29, 'Martyn': 39, 'Sikandar': 55}

print (users_age)               # {'Matt': 29, 'Martyn': 39, 'Sikandar': 55}

users_age['Sikandar']           # 55  --> reading the value (it's like indexing)


# Dictionaries are NOT immutable  

# ADD: you can add to the list

users_age['Richard'] = 42

print (users_age)               # {'Matt': 29, 'Martyn': 39, 'Sikandar': 55, 'Richard': 42}

# MODIFY: We can reassign values

users_age['Sikandar'] = 24

print (users_age)               # {'Matt': 29, 'Martyn': 39, 'Sikandar': 24, 'Richard': 42}

# REMOVE: we can remove values

del users_age['Sikandar']       # Deleting Sikandar

print (users_age)               # {'Matt': 29, 'Martyn': 39, 'Richard': 42}

# print ( users_age['Sikandar'] ) # This should error because Sikandar was removed from the list


# CHECKING: we can check if an item exists in dictionary, the same way as List & Tuples
### !!!! List and Tuples search by values
### !!!! Dictionary searches by key

users_age = { 'Matt': 29, 'Martyn': 39, 'Sikandar': 55}

print( 'Prem' in users_age )            # False - doesn't exist

print( 'Sikandar' in users_age )        # True

print( 55 in users_age )                # False - because 55 is a value not a key. Dict looks for keys only


# CREATING DICTIONARY

# 1) { }
users_age = { 'Matt': 29, 'Martyn': 39, 'Sikandar': 55}
print( users_age ) 

# 2) dict() function
users_age_dict = dict(Richard=29, Julian=39, Vincent=55)
print( users_age_dict )

# 3) a list of tuples() function
users_age_tuples = dict( [ ('Lily', 29), ('Rahmat', 39), ('Katie', 55) ] )
print( users_age_tuples )

#       Good thing thing with list of tuples is the items inside them cannot be changed and 
#       you will only be allow to enter enter the key and it's value (limiting errors)