from functools import reduce

# High-order functions are those that can take more functions inside them

my_list = [1, 2, 3, 4, 5]

# Mapping function - (function, domain)
print( list(map(lambda var1: var1 + 10, my_list)))          # add 10

# Filter function - (condition, domain)
print ( list(filter(lambda x: x > 1, my_list)) )            # print only > 1
print ( list(filter(lambda x: x % 2 == 0, my_list)) )       # print only even numbers

# Reduce function - (function, domain)
print ( reduce(lambda a, b: a + b, my_list, 0) )            # (((1+2)+3)+4)+5 = 15


########################################
# Sorting function
########################################
print("")

my_list = ['a', 'B', 'b', 'C', 'c', 'D']

# Simple sorting
print ( sorted(my_list) )

# Key sorting
print ( sorted(my_list, key=lambda a: a.lower() ) )

########################################
# list method sorting
########################################
my_list.sort(key=str.lower)
print (my_list)
