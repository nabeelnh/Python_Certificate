#!/usr/local/bin/python3.8

print('Hello, Nabeel')

users_input = input('Enter a message: ')

# First character
print ( 'First character:', users_input[0]  )

# Last character
print ( 'Last character:', users_input[-1]  )

# Middle character
print ( 'Middle character:', users_input[ int(len(users_input) / 2) ]  )

# Even character
print ( 'Even index characters:', users_input[::2] )

# Odd character
print ( 'Odd index characters:', users_input[1::2] )

# Reversed message
print ( 'Reversed message:', users_input[::-1] )