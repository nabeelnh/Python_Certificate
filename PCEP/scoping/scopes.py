#!/usr/local/bin/python3.8

'''
The variables and objects that we're working with are only accessible within certain scopes.

When we say that we're working in a different "scope" in Python, we mean that we're within the 
boundaries of a function or a class. This is important because while within the body of a 
function or class, the variables that we create are not automatically accessible outside of that context.
'''

#################################
print('Without Scope:')
#################################
'the variables at the top are accessible to the rest of the script'
if 1 < 2:
    x = 5

while x < 6:
    print(x)            # 5
    x += 1

print(x)                # 6 (as it exited the loop at 6) 


#################################
print('\nWith Scope:')
#################################
del x                   # make x undefined 
def setting_x():
    x = 5

setting_x()

while x < 6:            # the value of x is unknown
    print(x)            
    x += 1

print(x)                # name 'x' is not defined

'''Summary: If you define a variable inside a function, you do not have access to it outside
of the function. 
'''