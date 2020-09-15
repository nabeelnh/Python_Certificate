#!/usr/local/bin/python3.8

def gen_range(stop, start=1, step=1):       
    count = start
    while count <= stop:
        yield count                        
        count += step


generator = gen_range(10)        

# LISTIGN
print ( list(generator) )

### This isn't always helpful because we may have an infinit loop in the generator. 

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

fib = gen_fib()
print ( next(fib) )                 # 1
print ( next(fib) )                 # 2

# print ( list(fib) )               # infinit list (due to infinit loop) - problem/Killed

# SOLUTION - LIMIT THE LOOP
fib = gen_fib()
output = [ next(fib) for each_element in range(50)][-1]           

'''
[-1] means getting the laste itteration for that [] request
next(fib) at the start means return that
'''

print ( output )                                                  # generators make itterations so quick
