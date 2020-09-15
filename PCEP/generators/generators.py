#!/usr/local/bin/python3.8

# Generators: allow you to build functions that behave like iterators.

########################################
# EXAMPLE
########################################

def gen_range(stop, start=1, step=1):       # start=1 and step=1 are defaults
    count = start
    while count <= stop:
        yield count                         # yield is like a return for generators
        count += step

generator = gen_range(5)                    # set the stop value. aka gen_range(5, start=1, step=1)


'''
unlike ranges and normal while loops, a generator loop will stop completely
under each loop and will need to be called.
'''
print ( next(generator) )                   # 1
print ( next(generator) )                   # 2
print ( next(generator) )                   # 3
print ( next(generator) )                   # 4
print ( next(generator) )                   # 5
# print ( next(generator) )                 # error - it's out of the range: 5


########################################
# PRATICAL APPLICATION
########################################
print('\nPractical Application:')           

for each_number in gen_range(10, step=2):
    print(each_number)                      # this is an alternative of calling the gen each time
