#!/usr/local/bin/python3.8

users_input = int(input('How many values should we process: '))


for number in range(1, users_input + 1):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)



