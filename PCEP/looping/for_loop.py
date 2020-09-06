#!/usr/local/bin/python3.8

print ('\nFOR LOOP\n')


# Sequence = list, tuple, dictionary or string

'''
for TEMP_VARIABLE in SEQUENCE:
    first item in the sequence      = index(0)
    second item in the sequence     = index(1)
    third item in the sequence      = index(2)
    ...
'''

##############################
# LIST
##############################
colours = ['purple', 'red', 'blue', 'pink', 'yellow']

for each_element in colours:
    print(each_element)

# OR
print ('')

for colour in colours:
    print(colour)


##############################
# TUPLE
##############################
print ('')

points = (1, 2, 3)

for point in points:
    print(point)


##############################
# DICTIONARY
##############################
print ('')

weights = {'Adam': 74, 'Smith': 60, 'Samantha': 95}

for key in weights:                             # by default it shows the keys
    print(key)

for values in weights.values():                 # to show the values
    print(values)

for each_item in weights.items():               # To show the keys and values 
    print(each_item)

for key, value in weights.items():              # unpacking the tuple, better representation than the above
    print(key, value)

##############################
# STRING
##############################
print ('')

for each_letter in 'Nabeel':
    print(each_letter)
