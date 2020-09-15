#!/usr/local/bin/python3.8

'''
In case you want to use a variable you defined outside of a function (global variable) 
you can do so using the 'global' keyword

Limitation: 
> you cannot use a global variable in a function if the function parameter is the name
of the global variable

Min prod: you can create a new global variable inside a function
'''

########################################
print('BEFORE GLOBAL')
########################################
y = 5

def func(y):
    print('Inner y:', y)
    # global y                      # will error: function parameter = global variable 

func(10)

print('outter y:', y)


########################################
print('\nAFTER GLOBAL\n')
########################################
y = 5

def func(z):
    c = z                           # whatever variable (c) you don't want
    global y                        # you can use the global variable because the parameter is not a global name
    global x                        # creating a new global variable
    y = c                           # manipulating the function to assign a new global variable
    x = 7

print('y before func:', y)

func(10)

print('y after func:', y)
print('x after func:', x)
