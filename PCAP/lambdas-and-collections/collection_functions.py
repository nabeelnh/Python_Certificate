from functools import reduce # importing reduce module

"""
Mapping a function
f(x) = 1 + x

domain: [0, 1, 2, 3]       # The domain is being mapped to the function and in return it returns the range
range:  [1, 2, 3, 4]       # the output is the range
"""

# Function: f(x) = 1 + x
domain = [1, 2, 3, 4]

our_range = map(lambda num: 1 + num, domain)             # map(function, domain)
print(list(our_range))                                   # [2, 3, 4, 5]

our_filter = filter(lambda num: num % 2 == 0, domain)    # filter(function which returns either True/False, domain)
print(list(our_filter))                                  # [2, 4]

our_sum = reduce(lambda acc, num: acc + num, domain, 0)  # adding all the domains
print(our_sum)                                           # 10


my_list = ['b' ,'a', 'Bravo', 'd', 'c', 'Alpha', 'Delta']

print("\nSorting by default:")
print(sorted(my_list))          # only separates the letters based on Capital or lowercase

print("\nSorting with a lambda key:")
print(sorted(my_list, key=lambda string: string.lower() ))    # orders the letters correctly

print("\nSorting with a list method:")
my_list.sort(key=str.lower)#, reverse=True)  
print(my_list)



### LESSON
# Option 1: function 
"my_string".lower() 

# Option 2: method
str.lower("my_string")

# print("my_string".lower() == str.lower("my_string"))    # True

# key=str(type).function  the function without the () means it will be called here 
# without needing the option of a parameter to be called elsewhere