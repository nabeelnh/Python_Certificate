#!/usr/bin/env python

user_input = int(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))

Celsius = round(((user_input - 32) * 5 / 9), 2)

print(user_input, 'F is', Celsius, 'C')