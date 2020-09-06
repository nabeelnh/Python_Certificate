#!/usr/local/bin/python3.8

name = input('What is your name: ')
colour = input('What is your favourite colour: ')
age = int(input('How old are you today: '))

print (name )
print ('is ' + str(age) + ' year old' )
print ('and his favourite colour is ' + colour )
print ("")

# Making it one line 

##  'end' --> e.g adds space after each comma and puts the next line down to the top

print (name, end=" ")
print ('is ' + str(age) + ' year old', end=" ")
print ('and his favourite colour is ' + colour )

##  'sep' --> e.g adds space after each comma

print (name, 'is', age, 'years old and loves the colour', colour + '.', sep=" ")

print (name, 'is', age, 'years old and loves the colour', colour + '.', sep=": ")  # add : under each separation