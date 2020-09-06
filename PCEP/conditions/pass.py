#!/usr/local/bin/python3.8

print ('pass condition')

# PASS keyword is a non-operational statement. It doesn't do anything but it allows us to define the else statement without writing anything

name = input('Enter your name: ')

if name == 'bill':
    print ('Hello bill')
else:
    pass                                    # pass = do nothing