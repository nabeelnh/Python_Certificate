from functools import reduce

domain = [1, 2, 3, 4, 5]

# map(function, domain)
my_range = list(map(lambda num: num * 2, domain))
print(my_range)

# filter(function[Y/N], domain)
my_filter = filter(lambda num: num % 2 == 0, domain)
print(list(my_filter))

# reduce(function, domain, initial_value)
my_sum = reduce(lambda sum, num: sum + num, domain, 0)
print(my_sum)