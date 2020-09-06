#!/usr/local/bin/python3.8

print ('while loop')

# Just like conditions, this is a control flow structure
# Good for: infinit looping, unknown number looping or specific number of time (e.g. count <= 4)

'''
while CONDITION:
    print('<something>')
'''

# Infinit loop
'''
while 1 < 2:
    print ('something')
'''

# while looping requires a condition that will eventually be False  
# or it'll be an infinit loop like above

count = 1

while count <= 3:
    print (count)
    count += 1


# when count = 4 then 4 < 3 will be a False condition and the while loop will break