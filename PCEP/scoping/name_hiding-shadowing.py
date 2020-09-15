#!/usr/local/bin/python3.8

'''
name hiding aka shadowing, shows us that even if a variable is assinged a different thing
inside a function, only when the function is called will it's assigned value have meaning.
Otherwise the variable assigned outside of the function will be used.
'''

y = 5

def set_y(y):
    print ('Inner y:', y)

set_y(10)                       # Inner y: 10

print('Outter y:', y)           # Outter y: 5