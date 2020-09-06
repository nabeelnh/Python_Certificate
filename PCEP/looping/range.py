#!/usr/local/bin/python3.8

# A safer means of iterating through unknown number of times (as in a while loop) is to use a 
# range function range(). range() are immutable sequence type.

# range(<start_value>, <stop_value>, <step_value>)
# by default: range(<stop_value>)   --> range(0, <stop_value>)

my_range = range(10)

print (my_range)                    # range(0, 10)  i.e range of 0 to 10

my_range_list = list(my_range)

print(my_range_list)                # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


my_range_in_full = range(0, 10, 2)

print( list(my_range_in_full) )     # [0, 2, 4, 6, 8]


##############################################
print('\nWhile loop vs. For loop with range\n')
##############################################

print('While loop')
count = 1
while count <= 3:
    print('looping')
    count += 1

print('\nfor loop')
for _ in range(1, 4):                   # _ conventional way of indicating you don't care what the variable is
    print('looping')

