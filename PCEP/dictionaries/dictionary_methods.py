#!/usr/local/bin/python3.8

print ('Dictionary Methods')

ages = { 'Kevin': 69, 'Michael': 98 }

print (ages)

print ( ages.keys() )               # gives just the KEYS

print ( list( ages.keys() ) )       # To make the list clear (as we previously did with list(reversed(<list>)) )

print ( list( ages.values() ) )     # gives just the VALUES

print ( list( ages.items() ) )      # gives KEYS : VALUES
#                                   list of Tuples  (alternative of creacting dictionaries)