#!/usr/local/bin/python3.8

#print ('conditons')

users_input = int(input('Enter an integer value: '))

# calculate = users_input % 3

if users_input % 3 == 0 and users_input % 5 == 0:
    print ('FizzBuzz')
elif users_input % 3 == 0:
    print ('Fizz')
elif users_input % 5 == 0:
    print ('Buzz')
else:
    print (users_input)
