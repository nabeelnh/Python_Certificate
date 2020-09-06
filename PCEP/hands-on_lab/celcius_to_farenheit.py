#!/usr/local/bin/python3.8

print ('Hello')

temperature_f = float(input('What temperature (in Fahrenheit) would you like converted to Celsius? '))

celsius = (temperature_f - 32) * 5 / 9

print (temperature_f, 'F is', round(celsius, 2), 'C', sep=" ")

# or

print (temperature_f, 'F is', round(celsius, 2), 'C')


