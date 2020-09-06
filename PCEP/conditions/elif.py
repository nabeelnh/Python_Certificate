#!/usr/local/bin/python3.8


# Remember just like the keyword and and or. The if condition checks the first condition that meets the if condition.
# If your condition is for True, and you to order things based on which True should come first in the sequence.
# The ORDER OF THE CONDITIONS is very important.

print ('elif statement\n')

if 'a' > 'b':
    print ('First condition was True\n')
elif 'c' < 'd':
    print ('Second condition was True\n')
else:
    print ('None of the conditions were True\n')


name = input('Please enter your first name: ')

if len(name) >= 6:
    print ('You have a long first name')
elif len(name) == 5:
    print('Your name is exactly 5 characters long - Nice!')
elif len(name) >=4:
    print('Your name is 4 characters long')
else:
    print ('Your name is short')
