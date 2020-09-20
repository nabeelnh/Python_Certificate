#!/usr/local/bin/python3.8

import random

users_input = int(input('How points should we add: '))

def determine_pi(n):
    a_circle = 0
    a_square = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        rad = x**2 + y**2
        if rad <= 1:
            a_circle += 1
        a_square += 1
    
    return 4 * a_circle/a_square

print(determine_pi(users_input))
