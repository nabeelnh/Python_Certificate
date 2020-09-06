#!/usr/local/bin/python3.8

# Deals with the collection of items
    # A list allows us to have a collection of items 
    # Amazing: a list can take a collection of different items i.e. strings, integers, floats, boolean

my_list = ['string', 1, 1.0, True]          # different items in one list

print (my_list)                 

indexing = my_list[0]                       # indexing - like with string

print (indexing) 

length = len(my_list)                       # length - finding the length of a string

print (length)


# Strings are **** NOT IMMUTABLE ********

# - you change each item inside a string
# - you can add another set to the list i.e. cancatinate two things together

my_list = [0, 1, 2, 3, 4, 5]

my_list[0] = 'a'                           # Indexing - reassign item

print (my_list)                            # ['a', 1, 2, 3, 4, 5]     


my_list + [6, 7, 8, 9, 10]                 # Cancatinate: ['a', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#                                           but my_list will still be [0, 1, 2, 3, 4, 5] unless you

concat = my_list + [6, 7, 8, 9, 10]        # assign it to a new variable: 
my_list += [6, 7, 8, 9, 10]                # reassign the variable again (nothing to do with immutability)



my_list = ['a', 1, 2, 3, 4, 5]             

my_list[1:3] = ['b', 'c']                  # Slicing - reassign item :  ['a', 'b', 'c', 3, 4, 5]

my_list = ['a', 1, 2, 3, 4, 5]             

my_list[1:2] = [4, 5, 6]                   # Slicing - reassign and add : ['a', 4, 5, 6, 2, 3, 4, 5]


# REMOVING ITEM FROM A LIST

# - reassgin to empty list

my_list = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c'] 

my_list[7:] = []                           

my_list                                   # [1, 2, 3, 4, 5, 6, 7]


# - 'del' keyword / statement

my_list = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']

del my_list[7:]                           # 'del' is a keyword    

my_list                                   # [1, 2, 3, 4, 5, 6, 7]

del my_list                               # delete entire list