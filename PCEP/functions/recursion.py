#!/usr/local/bin/python3.8

# Recusion - you can call your function within the same function

'''
Fibonacci sequence:
1, 1, 2, 3, 5, 8, 13 ...

f(n) = f(n - 2) + f(n - 1)

f(5) = f(3) + f(4)
f(5) = f(1) + f(2) + f(2) + f(3) 
f(5) = 1 + f(0) + f(1) + f(0) + f(1) + f(1) + f(2)
f(5) = 1 + 0 + 1 + 0 + 1 + 1 + f(0) + f(1)
f(5) = 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1
f(5) = 5
'''

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    return fib(n - 2) + fib(n - 1)      # function within a function - will give us the  result

output = int(input('What number would you like to convert to Fibonnaci? '))

print( 'The value is: ', fib(output) )