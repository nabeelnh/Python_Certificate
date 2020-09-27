#!/usr/local/bin/python3.8

temp_f = float(input('What temperature (in Fahrenheit) would you like converted to Celsius? '))

temp_c = (temp_f - 32)  * 5 / 9

temp_c = round(temp_c, 2)

print (temp_f, 'F is', temp_c, 'C')
