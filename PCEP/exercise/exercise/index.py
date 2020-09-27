#!/usr/local/bin/python3.8

users_input = input('Enter a message: ')

print('First character:', users_input[0])
print('The last character:', users_input[-1])
print('The middle character:', users_input[int(len(users_input) / 2)])
print('Even index character:', users_input[::2])
print('Odd index character:', users_input[1::2])
print('message in reversed:', users_input[::-1])

