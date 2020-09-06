#!/usr/local/bin/python3.8

# Methods are functions that are attached to items


# 'append' : append(<appended_item>)
my_list = [1, 2, 3]
my_list.append(4)


# 'insert' : insert(<position>, <appended_item>)
my_list.insert(0, 'a')        #  ['a', 1, 2, 3, 4]


# 'index' : tells you the position of an item
my_list = ['a', 1, 2, 3, 4]
my_list.index('a')            # 0


# 'in' keyword finds whether something exists in a list
my_list = ['a', 1, 2, 3, 4]

'a' in my_list                # True
'a' not in my_list            # False
'b' in my_list                # False


# 'sort' function - sorts out a list in order
my_list = [6, 8, 10, 4]
sorted(my_list)               # 4, 6, 8, 10]

# 'reversed' function - reverses the list 
my_list = [6, 8, 10, 4]

reversed(my_list)             # not useful: <list_reverseiterator object at 0x7f51ad4eea60>
list (reversed(my_list))      # useful list back: [4, 10, 8, 6]

## sort and reverse           # to use both, only one type can be used: i.e. int, str, float
my_list = [6, 8, 10, 4]
list (reversed(sorted(my_list)))    # [10, 8, 6, 4]