#!/usr/local/bin/python3.8

###############################################
# Literals, Variables, and Comments
###############################################
# Simple comment
'''
This is a:
multi-line string
'''
name = 'Nabeel'
variable = f'Hello my name is {name}'
print(variable)
variable += '. What\'s your name?'
print(variable)

print ('Yo' + 'lo')        # adding two of the same thing together words. i.e. int, str, float

variable = 'HaHa' * 4      # you can multiple (not divide or subtract string)
print(variable)

print( variable.find('a') )     # find the index of the first occuaranc of that letter
print( variable.index('a') )    # alternative to .find() method is the .index() method
print( variable[1] )            # opposite of the above. Find the letter in index 1

print( 'Hello'.islower() )              # False
print( 'Hello'.lower().islower() )      # True

print(f'Please print your name in a new line with tab:\n\t{name}')

print( 2 == 2 )         # True: Boolean
print (True)

print( 2 == 3 )         # False: Boolean
print (False)           

# Multipication
print ( 4.5e9 == 4.5 * ( 10**9 ) == 4.5E9 )


###############################################
# Number Systems and Numeric Operators
###############################################
print(2 + 2)
print(4 - 4)
print(9 * 9)
print(2 / 3)
print(2 // 3)       # returns number without reminder
print(2 % 3)        # returns reminder without number
print(2 ** 2)      # exponent


###############################################
# Operators and Binding
###############################################
print (False and False)     # False
print (False and True)      # False
print (False or True)       # True (always goes for the first Truth)

print( ord('a') )           # 97 ord() gives the value of the strings unicode code point value
print( ord('b') )           # 98

print('a' > 'b')            # False
print('a' < 'b')            # True
print( 10 >= 10 )           # True

# in maths follow the BIDMAS RULE


###############################################
# Input and Output Operations
###############################################
print ( float(1) )        # 1.0
print ( int(1.00) )       # 1
print ( str(1.00) )       # '1.00'

print ( bool('<anything>') )    # True
print ( bool('') )              # False  : empty or 0

# name = input('Please enter your name: ')


###############################################
# Strings (immutable)
###############################################
print( 'it\'s capitalized'.capitalize() )           # Hello
print ( len('What is it?') )                        # 11

print ( 'What is it?'[::-1] )                       # ?ti si tahW : opposite direction
print ( 'What is it?'[0:4:1] )                      # What

my_string = 'What is it?'
print ( my_string[ len(my_string) - 1 ] )           # last letter


###############################################
# Lists (not immutable)
###############################################
my_list = ['apple', 'banana', 'monkey']
print(my_list)

my_list.append('rice')
print(my_list)

print (my_list[3])                          # rice

print (len(my_list))                        # 4 : it counts each unit in the lest as one element

print (my_list[::-1])                       # slice as stings : ['rice', 'monkey', 'banana', 'apple']

my_list[0] = 1.0                            # change the value of 'apple' to a float 1.0
print(my_list)

my_list[1:3] = ['chuna', 'elephant']        # change ['banana', 'monkey'] to ['chuna', 'elephant']
print(my_list)

my_list += ['liver', 'gizzard', 'milk']     # multiple addition
print(my_list)

my_list[4:] = []                            # removing multiple items
print(my_list)

del my_list[0]                              # removing one item from the list
print(my_list)

del my_list                                 # deleting the entire list
#print(my_list)

my_list = [1, 8, 20, 2, 3]
print (my_list)

print ( sorted(my_list) )

print ( list(reversed(my_list)) )
print ( list(reversed(sorted(my_list))) )   # [20, 8, 3, 2, 1]

my_matrix = [ [1, 2, 3], [4, 5, 6] ]
print(my_matrix)            # [[1, 2, 3], [4, 5, 6]]

print(my_matrix[0])         # [1, 2, 3] : each unit is a list

print(my_matrix[0][0])      # 1 : first element in the first list

print(len(my_matrix))       # 2


column_count = len(my_matrix[0])       # 3
print (column_count)

row_count = len(my_matrix)             # 2
print (row_count)

###############################################
# Tuples (immutable)
###############################################
point_2d = ('3.0', '7.0')

print(name)

point_3d = point_2d + (2.0,)
print(point_3d)

x , y, z = point_3d

print(x)
print(y)
print(z)

print('My name is %s %s and I am %i years old.' % ('Matt', 'Parrel', 40))

person = ('Richard Smith', 36, '555-555-555')
person1 = ('Mick Richard', 26, '555-555-551')

print('My name is', person[0], 'and I am', person[1])
print('My name is %s and I am %i' % (person1[0], person1[1]))
print(f'My name is {person[0]} and I am {person[1]}')


my_list = ['apple', 'banana', 'carrot']
my_tuple = ('firrari', 'Lexus')

list_in_tuples = (my_list, 'Lexus')
print(list_in_tuples)

tuples_in_list = ['monkey', 'dog', my_tuple]
print(tuples_in_list)

tuples_in_list.append('lion')
print(tuples_in_list)

print( 'lion' in tuples_in_list )          # True

###############################################
# Dictionary
###############################################
name = {'mick': 29, 'James': 36, 'Richard': 48, 'Smith': 55}
print(name)

print(name['mick'])             # similar to .find() or .index() you must specify the key you're looking for

name['Samantha'] = 25           # add user
print(name)

del name['Samantha']            # delete user
print(name)

print ('mick' in name)          # True : like in List and Tuple 'in' and 'not in' work here too
print ('Lizard' in name)        # False
print ('Lizard' not in name)    # True

print( name )
print( name.keys() )
print( name.values() )
print( name.items() )

print( list(name.items()) )


###############################################
# Strings
###############################################
print('hello'.capitalize())             # Hello

my_string = 'PCEP course'

print( id(my_string) )                  # 139640280195248
print( id('PCEP course') )              # 139640280195248

print( id('PCEP') )                     # 140368024469936 

print ( id(my_string) == id('PCEP course') )       # True

# This shows how Strings cannot be changed - immutable.
# id('PCEP course') and id(my_string) are the same ans hence take the same location in memory.
# but if we medofiy the string i.e. id('PCEP') instead of id('PCEP course'), we have a different id
# i.e. the string takes a different location in memory i.e. not the same string.

print(len('Pipe'))                      # 4

my_string = 'Welcome to the PCEP course'

split_string = my_string.split()
print ( split_string )

join_string = ' '.join(split_string)
print ( join_string )

# a forth way of writing a string
my_string = 'Hello my name is {} and I really like to {} with my {}'.format('Ahmed', 'swim', 'brother')
print (my_string)

my_string = 'Hello my name is {0} and I really like to {1} with {0}'.format('Ahmed', 'swim')
print (my_string)
