#!/usr/local/bin/python3.8

print ('Strings\n')

users_input = input('Enter a message: ' )

print (  'Lowercase:',  users_input.lower() )

print (  'Uppercase:',  users_input.upper() )

print (  'Capitalized:',  users_input.capitalize() )

print (  'Title Case:',  users_input.title() )

print ( 'words:',  users_input.split() )

sorted_words = sorted(users_input.split())

print (  'Alphabetic First Word:',  sorted_words[0] )

print (  'Alphabetic Last Word:',  sorted_words[-1] )