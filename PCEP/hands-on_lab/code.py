#!/usr/local/bin/python3.8

names = []

print (names)

names.append('Nabeel')
names.append('Seif')
names.append('Mum')

print (names)

names = names + ['amina', 'usama', 'samiha']

print (names)

del names[3]

print (names)

names_reversed = list(reversed(names))

print (names_reversed)

names.insert(3, 'amina_2')

print (names)

the_originals = names[0:3]

print (the_originals)