#!/usr/local/bin/python3.8

# Generators: allow you to build functions that behave like iterators.

########################################
# EXAMPLE
########################################

def gen_range(stop, start=1, step=1):
    count = start
    while count <= stop:
        yield count                    # yield is like a return for generators
        count += 1

generator = gen_range(5)               # sets the range i.e. stop value. In this rage, 5 is max
#                                        The stop value is mandatory. The rest are optional with default value

print ( next(generator) )               # 1
print ( next(generator) )               # 2
print ( next(generator) )               # 3
print ( next(generator) )               # 4
print ( next(generator) )               # 5
# print ( next(generator) )               # error - it's out of the range: 5


########################################
# PRATICAL APPLICATION
########################################
def gen(stop, start=1, step=1):
    count = start
    while count <= stop:
        yield count                    # yield is like a return for generators
        count += 1

    
    for number in gen(10, step=2):
        print(number)                      # 