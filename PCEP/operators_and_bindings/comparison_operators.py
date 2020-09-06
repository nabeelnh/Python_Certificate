#!/usr/local/bin/python3.8

# You cannot compare INTEGERS and STRINGS

# Greater than (>) and less than operators (<)
print (1 < 2)       # True
print (5 < 10)      # True
print (10 < 5)      # False

print (5 <= 10)     # True      (5 is either less than 10 *OR* equal to 10. One condition is true, so result is True )
print (5 >= 10)     # False     (both conditions are False)
print (2.0 >= 2)    # True      (both conditons are True)

### Works with strings too
print ('a' < 'b')       # True      (by order of alphabetic letter)
print ('a' > 'b')       # False

##### you can combine letters   (it is like each letter is assign a value a = 1, b =2 ...etc)
print ('aa' < 'ba')     # True
print ('aa' <= 'ba')    # True

# The true value of a string can be found using the ord function
print ( ord('a') )      #  97
print ( ord('b') )      #  98
# hence 'a' < 'b'

print ( ord('A') )      #  65   Capitals have a different value to lower case


# EQUAL SIGN (==)
### Since we already use '=' for assignment of variables, we use == to mean equal instead

print ( 1 == 1 )        # True
print ( 1.0 == 1 )      # True


# Identity Operator (is)
### It will only return True if things are *exactly* identical 
### The identity operators work based on the id of the object, 
### and most of the basic types in Python are immutable (meaning they cannot be changed)

print ( 1 is 1 )        # True
print ( 1 is 1.0 )      # False 

print ( 'a' is 'a' )            # True
print ( 'a' is not 'a' )        # False

# how it works behind the scenes (another way of writing it)
print ( 'a' is 'a' )            # True
print ( id('a') == id('a') )    # True

print ( 'a' is not 'a' )        # False
print ( id('a') != id('a') )    # False

# lists have different identities even if they look the same because things can be added to them e.g.
### i.e. they are NOT mmutable - they can be change

print ( [] is [] )      # False
