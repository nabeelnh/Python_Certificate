#!/usr/bin/env python

user_input = input("Enter a message: ")

First_character = user_input[0]
Last_character = user_input[-1]
Middle_character = user_input[int(len(user_input) / 2)]
Even_index_characters = user_input[::2]
Odd_index_characters = user_input[1::2]
Reversed_message = user_input[::-1]

print("First character: ", First_character)
print("Last character: ", Last_character)
print("Middle character: ", Middle_character)
print("Even index characters: ", Even_index_characters)
print("Odd index characters: ", Odd_index_characters)
print("Reversed message: ", Reversed_message)
