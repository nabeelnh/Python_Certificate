#!/usr/local/bin/python3.8

print ('Tuples vs Lists\n')

# If you don't know how many items you'll be storing ==> choose: List

# If you need to return multiple pieces of information from one function ==> Tuples (unpacking)

# I need to model something with specific fields and specific number of those fields ==> Tuples 

person = ('Mike Tyson', '28', '07945728019')
person_2 = ('Mike Ross', '32', '076645888910')

print ( person[0] )                 # Mike Tyson
print ( person_2[0] )               # Nabeel Mike Ross

# Peoples names cannot be modified (immutable unlike list)
print ('')

# Adding: Tuples > List  &  Lists > Tuples

## Adding Lists to Tuples
my_list = [1, 2, 3, 4]
my_tuple = ( my_list, 5 )

print ( 'Tuple:', my_tuple)

my_list.insert(0, 0)

print ( 'appended_Tuple:', my_tuple )
print ('')

## Adding Tuples to Lists
my_tuple = (1.0, 2.0)
my_list = [my_tuple, 3.0 ]

print ( 'List:', my_list)

my_list.append(4.0)

print ( 'appended_List:', my_list)


# Note: you cannot change the length of the tuples itself. It always retained the number of units it can see.
