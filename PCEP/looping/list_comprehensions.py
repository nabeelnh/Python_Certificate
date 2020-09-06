#!/usr/local/bin/python3.8

# No true benefit - some people might write code this different way and you should learn to be 
#                   familiar with it.

####################################
# LOOPING EXAMPLE
####################################
colours = ['red', 'blue', 'orange', 'yellow', 'purple']
uppercase_colours = []              # make a new emtpy list which will contain the new change

for colour in colours:
    uppercase_colours.append( colour.upper() )
    
print ('\nNormal looping:\n', uppercase_colours)           # ['RED', 'BLUE', 'ORANGE', 'YELLOW', 'PURPLE']


####################################
# LIST COMPREHENSION
####################################
colours = ['red', 'blue', 'orange', 'yellow', 'purple']

uppercase_colours = [colour.upper() for colour in colours]       # easiest way to remember: start with the for loop

print('\nList comprehension:\n', uppercase_colours)

# BENEFITS - easier to read and less scripting


####################################
# LOOPING EXAMPLE 2
####################################
colours = ['red', 'blue', 'orange', 'yellow', 'purple']
warm_colours = []

for colour in colours:
    if colour in ['red', 'orange', 'yellow']:
        warm_colours.append(colour)

print('\nNormal looping - Warm colours:\n', warm_colours)

####################################
# LIST COMPREHENSION 2
####################################
colours = ['red', 'blue', 'orange', 'yellow', 'purple']
warm_colours = [colour  for colour in colours if colour in ['red', 'orange', 'yellow'] ]

print('\nNormal looping - List comprehension:\n', warm_colours)

# BENEFITS - easier to list